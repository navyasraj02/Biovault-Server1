from application import app
from flask import request, redirect, flash, url_for, jsonify, render_template
from application import db
from .route_func import fpMatch

@app.route("/")
def home():
    
    return  {"status": "success", "message": "Connected to server 1"}
