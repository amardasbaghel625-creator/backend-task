from flask import Flask
from modules.rest_api.comment_router import register_comment_routes

app = Flask(__name__)
register_comment_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
