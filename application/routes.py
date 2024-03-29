from application import app
from flask import request, redirect, flash, url_for, jsonify, render_template
from application import db
from .route_func import fpMatch
import numpy as np
import msgpack
@app.route("/")
def home():
    return  {"status": "success", "message": "Connected to server 1"}
@app.route('/api/log',methods=["POST","GET"])
def log():
    data=request.json
    print(data)
    #data = msgpack.loads(data)
    length = data['data']['len']
    description = data['data']['descrip']
    user_id = data['data']['user_id']
    retrieveddesc=0 #retieve descriptiopn from 
    #code to retieve data from mongodb and match
    score=fpMatch.fingerprint_segment(description,retrieveddesc)
    
    """print("data received from main server")
   """
    return {"success":"true", "score":score}
    # eUser=db.fing1.find_one({"fid":id})
    # if eUser:
    #     #match the segment retrieved with the incoming segment using match algo
    #     return {"success":"true"}
    # else:
    #     return {"success": "false"}
@app.route('/api/reg')
def reg():
    #code to recieve data from the server insert to mongo db with user id
    data=request.json
    print(data)
    #data = msgpack.loads(data)
    length = data['data']['len']
    description = data['data']['descrip']
    user_id = data['data']['user_id']
    return

