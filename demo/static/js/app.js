/**
 * Created by qibo on 6/18/14.
 */

//var app = angular.module("App", ['ui.bootstrap', 'monospaced.qrcode']);
var app = angular.module("App", ['ui.bootstrap']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('<*');
  $interpolateProvider.endSymbol('*>');
});

app.controller("AppCtrl", function($scope, $element, $http) {
    $http.get("/api/players").success(function(data){
        $scope.players = data.objects;
    });

    $scope.newPlayer = {};
    $scope.addNewPlayer = function(){
        var p = angular.toJson($scope.newPlayer);
        console.log(p);
        $http.post("/api/players", p).success(function(data){
           $scope.players.push(data);
        });
    };
});

//login controller
app.controller("UserCtrl", function($scope, $element, $http) {
    $scope.user = {};
    $scope.alerts = [];

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    $scope.login = function(){
        var user = angular.toJson($scope.user);
        console.log(user);
        $http.post("/login", user).success(function(data){
            msg = {type: 'warning', msg: data};
            $scope.alerts.push(msg);
        });
    };
});

//register controller
app.controller("RegisterCtrl", function($scope, $element, $http){
    $scope.user = {};
    $scope.alerts = [];
    $scope.path = "test";

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    $scope.register = function () {
        $scope.alerts.length = 0;   // clear alerts
        if($scope.user.password != $scope.re_password) {
            msg = {type: 'danger', msg: 'passwords does not match'};
            $scope.alerts.push(msg);
        } else {
            var user = angular.toJson($scope.user);
            console.log(user);
            $http.post("/api/users", user).success(function(data){
                msg = {type: 'warning', msg: data.path};
                $scope.alerts.push(msg);
                $scope.path = data.path;

                var qrcode = new QRCode("qr");
                qrcode.makeCode(data.path);
            });
        }
    };
});
