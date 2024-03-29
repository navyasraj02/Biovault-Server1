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
    """data_array1 = np.array(data["data_array1"])
    data_array2 = data["data_array2"]
    data_string = data["data_string"]
    print(data_array1,data_array2,data_string)"""
        #kp=request.get("kp")
    #desc=request.get("desc")
    """print("data received from main server")
    print("id:",id)
    print("kp:",kp)
    print("desc:",desc)"""
    return {"success":"true"}
    # eUser=db.fing1.find_one({"fid":id})
    # if eUser:
    #     #match the segment retrieved with the incoming segment using match algo
    #     return {"success":"true"}
    # else:
    #     return {"success": "false"}
