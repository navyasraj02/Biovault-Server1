from application import app
from flask import request, redirect, flash, url_for, jsonify, render_template
from application import db
from .route_func import fpMatch
import numpy as np
import pymongo
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
    retrieveddesc=0 
    kp2=0#retieve descriptiopn from 
    #code to retieve data from mongodb and match
    score=fpMatch.fingerprint_segment(description,retrieveddesc,length,kp2)
    
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
    try:
        insert_result = db.fing1.insert_one({"length": length, "description": description, "user_id": user_id})
        return {"success": True, "message": f"Data inserted with ID: {insert_result.inserted_id}"}, 201  # Created status code
    except pymongo.errors.PyMongoError as e:
        return {"success": False, "message": f"Error inserting data: {str(e)}"}, 500  # Internal Server Error

    return

