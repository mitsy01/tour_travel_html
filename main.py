from flask import Flask

from routes.tour import tour_route
from models.tour import Tour
from models.base import create_db

app = Flask(__name__)
app.register_blueprint(tour_route)


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=5100)