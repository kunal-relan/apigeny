from flask import Flask,request,Response,session,render_template
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pymongo import Connection
import os
import requests
from flask.ext.cors import CORS,cross_origin
import httplib2



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

@app.route('/')
@cross_origin()
def hello():
	return render_template('index.html')

	return "hello"

@app.route('/signup',methods=['POST'])
@cross_origin()
def main():

		email = request.values['email']
		password = request.values['password']
		user_exists = db.users.find({'email':email}).count()

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

@app.route('/login',methods=['POST','GET'])
@cross_origin()
def login():
	if request.method == 'POST':

		email = request.values['email']
		password = request.values['password']
		print data
		user_exists = db.users.find({"email":email,"password":password}).count()
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
	else:
		return render_template('index.html')	
			

@app.route('/url',methods=['POST'])
@cross_origin()
def load():
	# data = request.get_json(force=True)
	# url = data['url']
	# method = data['method']
	# if method == 'GET':
	# 	headers = data['headers']
	h = httplib2.Http(".cache")
	resp, content = h.request("http://52.77.217.150/search_auto","GET",headers={'Authorization':'something'})
	return content





	



if __name__ == '__main__':


    app.run(host= '0.0.0.0' , port=5000 , debug=True)
