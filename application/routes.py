from application import app
from flask import request, redirect, flash, url_for, jsonify, render_template
from application import db
from .route_func import fpMatch

@app.route("/")
def home():
    return  {"status": "success", "message": "Connected to server 1"}
@app.route('/api/log',methods=["GET"])
def log():
    id=request.get("t_id")
    kp=request.get("kp")
    desc=request.get("desc")
    print("data received from main server")
    print("id:",id)
    print("kp:",kp)
    print("desc:",desc)
    return {"success":"true"}
    # eUser=db.fing1.find_one({"fid":id})
    # if eUser:
    #     #match the segment retrieved with the incoming segment using match algo
    #     return {"success":"true"}
    # else:
    #     return {"success": "false"}
