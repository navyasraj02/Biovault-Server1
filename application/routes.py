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
    #print(data)
    #data = msgpack.loads(data)
    length = data['data']['len']
    description =np.array( data['data']['descrip']) #feature set segment
    user_id = data['data']['user_id']
    query = {"user_id": user_id}
    result = db.fing1.find_one(query) #retrieve stored feature set from database

    # print("Type incoming data: ",type(description))
    if result is None:
        print("Result none")
    # else:    
    #     print("Type ret data: ",type(result["description"]))
    if isinstance(result["description"], list):
        rdescription = np.array(result["description"], dtype=np.float32)
    else:
        rdescription = result["description"]
    rlength= result["length"]
     #retrieved data and the arrived data are matched
     
    #code to retieve data from mongodb and match
    score=fpMatch.fingerprint_segment(description,rdescription,length,rlength)
    print("Score: ",score)
    """print("data received from main server")
   """
    
    try:
        return {"success":True,"score":score},201        
    except pymongo.errors.PyMongoError as e:
        return {"success": False}, 500  # Internal Server Error
    
@app.route('/api/reg',methods=["POST","GET"])
def reg():
    #code to recieve data from the server insert to mongo db with user id
    data=request.json
    #print(data)
    #data = msgpack.loads(data)
    length = data['data']['len']
    description = data['data']['descrip']
    user_id = data['data']['user_id']
    #description= np.array(description, dtype=float32)
    try:
        insert_result = db.fing1.insert_one({"length": length, "description": description, "user_id": user_id})
        print("Data stored successfully")
        return {"success": True, "message": f"Data inserted with ID: {insert_result.inserted_id}"}, 201  # Created status code
    except pymongo.errors.PyMongoError as e:
        return {"success": False, "message": f"Error inserting data: {str(e)}"}, 500  # Internal Server Error

    

