from flask import Blueprint, render_template

home_routes=Blueprint('home_routes', __name__)

@home_routes.route('/')
def home():
    return 'Home page loaded'

