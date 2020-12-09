from main_app.config import Config
from main_app import create_app
# Initialize the Flask application


app = create_app(config_class=Config)

if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
