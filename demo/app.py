from demo import app, db, manager
from models import Player

db.create_all()
manager.create_api(Player, methods=["GET", "POST", "DELETE"])


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run()
