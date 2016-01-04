from flask import Flask,request,Response,session
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo import Connection
import os
import requests
from flask.ext.cors import CORS,cross_origin



app = Flask(__name__)
FlaskJSON(app)
app.config["CACHE_TYPE"] = "null"
app.secret_key = 'Fuckedupworld'
app.config['CORS_HEADERS'] = 'application/json'
CORS(app)
# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#   return response


connection = Connection('localhost',27017)
db = connection.apigeny

@cross_origin()
def hello():

	return "hello"

@app.route('/signup',methods=['POST'])
@cross_origin()
def main():

		data = request.get_json(force=True)
		user_exists = db.users.find({'email':data['email']}).count()

		if user_exists == 0:
			insert_userdata = db.users.insert(data)
			session['user'] = os.urandom(24).decode('utf-8', errors='ignore').encode('utf-8')
			# response.headers.add('Access-Control-Allow-Origin', '*')
			result = json.dumps({"error" : "none","session_key":session['user'],"result":"success"})
			return result, 200 , {'Content-Type': 'application/json; charset=utf-8'}
		else : 
			result = json.dumps({"error" : "none","result":"user exists"})
			# response.headers.add('Access-Control-Allow-Origin', '*')
			return result, 200 , {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/login',methods=['POST'])
@cross_origin()
def login():
	data = request.get_json(force=True)
	print data
	user_exists = db.users.find({"email":data['email'],"password":data['password']}).count()
	if user_exists > 0:
		session['user'] = os.urandom(24).decode('utf-8', errors='ignore').encode('utf-8')
		
		result = json.dumps({"error" : "none","session_key":session['user'],"result":"success"})
		resp = Response(result,status=200,mimetype="application/json; charset=utf-8")
		print(result)	
		return result, 200 , {'Content-Type': 'application/json; charset=utf-8'}
	else :
		result = json.dumps({"error" : "none","session_key":[],"result":"Username/Password Wrong"})
		resp = Response(result,status=200,mimetype="application/json; charset=utf-8")
		return result, 200 , {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/url',methods=['POST'])
@cross_origin()
def load():
	data = request.get_json(force=True)
	url = data['url']
	method = data['method']
	if method == 'GET':
		headers = data['headers']



	



if __name__ == '__main__':


    app.run(host= '0.0.0.0' , port=5000 , debug=True)
