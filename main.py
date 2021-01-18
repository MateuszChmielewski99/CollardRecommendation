from flask import Flask
from flask_restful import Api
from controllers.recommendation.RecommendationController import RecommendationController

app = Flask(__name__)
api = Api(app)


api.add_resource(RecommendationController, '/api/recommend')

if __name__ == "__main__":
    app.run(debug=True, port=7200)
