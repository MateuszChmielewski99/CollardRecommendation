from flask_restful import reqparse

recommend_args = reqparse.RequestParser()

recommend_args.add_argument('algorithm', type=str, required=True)
recommend_args.add_argument('distance', type=str, required=True)
recommend_args.add_argument('divideByFirst', type=bool, required=True)
recommend_args.add_argument('divideBySecond', type=bool, required=True)
recommend_args.add_argument('divideByThird', type=bool, required=True)
recommend_args.add_argument('groupNumber', type=int, required=True)
recommend_args.add_argument('userId', type=str, required=True)
recommend_args.add_argument('normalizeData', type=str, required=True)