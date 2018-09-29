from flask import Flask, redirect, url_for, request
import requests 
import ast

app = Flask(__name__)


@app.route('/detect/<text>')
def detect(text):
	URL = "https://translation.googleapis.com/language/translate/v2/detect"

	PARAMS = {'q':str(text),'key':"ENTER_KEY_HERE"} 
	  
	r = requests.post(url = URL, data = PARAMS) 
	  
	data = r.json() 
	return str(ast.literal_eval(str(data))['data']['detections'][0][0]['language']);

@app.route('/translate/<text>/<source>/<dest>')
def translate(text,source,dest):

	URL = "https://translation.googleapis.com/language/translate/v2/"

	PARAMS = {'q':str(text),'source':str(source),'target':str(dest),'key':"ENTER_KEY_HERE"} 
	  
	r = requests.post(url = URL, data = PARAMS) 
	  
	
	data = r.json() 
	return str(ast.literal_eval(str(data))['data']['translations'][0]['translatedText']);


if __name__ == '__main__':
	app.run(debug = True)
