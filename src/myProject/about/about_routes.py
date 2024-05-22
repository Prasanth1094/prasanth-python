from flask import Blueprint

about_routes=Blueprint('about_routes', __name__)

@about_routes.route('/about')
def about():
    return 'About page loaded'

