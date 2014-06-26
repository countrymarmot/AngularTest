/**
 * Created by qibo on 6/18/14.
 */

var app = angular.module("App", []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('<*');
  $interpolateProvider.endSymbol('*>');
});

app.controller("AppCtrl", function($scope, $element, $http) {
    var app = this;
    $http.get("/api/player").success(function(data){
        app.players = data.objects;
    });

    $scope.newPlayer = {};
    app.addNewPlayer = function(){
        var p = angular.toJson($scope.newPlayer);
        console.log(p);
        $http.post("api/player", p).success(function(data){
           app.players.push(data);
        });
    };
});
