from flask import Blueprint, render_template

about_routes=Blueprint('about_routes', __name__)

@about_routes.route('/about')
def about():
    return 'About page loaded'

