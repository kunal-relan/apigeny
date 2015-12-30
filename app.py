from flask import Flask,request,Response,session
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo import Connection
import os
import requests

app = Flask(__name__)
FlaskJSON(app)
app.config["CACHE_TYPE"] = "null"
app.secret_key = 'Fuckedupworld'



connection = Connection('localhost',27017)
db = connection.apigeny

@app.route('/')
def hello():
	return "hello"

@app.route('/signup',methods=['POST'])
def main():
		data = request.get_json(force=True)
		user_exists = db.users.find({'email':data['email']}).count()

		if user_exists == 0:
			insert_userdata = db.users.insert(data)
			session['user'] = os.urandom(24).decode('utf-8', errors='ignore').encode('utf-8')
			result = json.dumps({"error" : "none","session_key":session['user'],"result":"success"})
			resp = Response(response=result,status=200,mimetype="application/json")
			return(resp)
		else : 
			result = json.dumps({"error" : "none","result":"user exists"})
			resp = Response(response=result,status=200,mimetype="application/json")
			return(resp)

@app.route('/login',methods=['POST'])
def login():
	data = request.get_json(force=True)
	user_exists = db.users.find({"email":data['email'],"password":data['password']}).count()
	if user_exists > 0:
		result = json.dumps({"error" : "none","session_key":session['user'],"result":"success"})
		resp = Response(response=result,status=200,mimetype="application/json")
			
		return(resp)
	else :
		result = json.dumps({"error" : "none","session_key":[],"result":"Username/Password Wrong"})
		resp = Response(response=result,status=200,mimetype="application/json")
		return(resp)

	



if __name__ == '__main__':


    app.run(host= '0.0.0.0' , port=5000 , debug=True)
