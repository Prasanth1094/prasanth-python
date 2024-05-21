from flask import Flask
from src.myProject.home.home_routes import home_routes
from src.myProject.about.about_routes import about_routes
from src.myProject.contact.contact_routes import contact_routes

app = Flask(__name__)
app.register_blueprint(home_routes)
app.register_blueprint(about_routes)
app.register_blueprint(contact_routes)

if __name__ == "__main__":
    app.run(port=5000,debug='true')