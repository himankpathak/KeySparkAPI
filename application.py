from flask import Flask, redirect, url_for, request
import requests 
import ast

app = Flask(__name__)


@app.route('/detect/<text>')
def detect(text):
	URL = "https://translation.googleapis.com/language/translate/v2/detect"
	# defining a params dict for the parameters to be sent to the API 
	PARAMS = {'q':str(text),'key':"AIzaSyBhRXPP_QgXqyT4wbY-SZU9118RPBHw01s"} 
	  
	# sending get request and saving the response as response object 
	r = requests.post(url = URL, data = PARAMS) 
	  
	# extracting data in json format 
	data = r.json() 
	return str(ast.literal_eval(str(data))['data']['detections'][0][0]['language']);

@app.route('/translate/<text>/<source>/<dest>')
def translate(text,source,dest):
   # api-endpoint 
	URL = "https://translation.googleapis.com/language/translate/v2/"
	# defining a params dict for the parameters to be sent to the API 
	PARAMS = {'q':str(text),'source':str(source),'target':str(dest),'key':"AIzaSyBhRXPP_QgXqyT4wbY-SZU9118RPBHw01s"} 
	  
	# sending get request and saving the response as response object 
	r = requests.post(url = URL, data = PARAMS) 
	  
	# extracting data in json format 
	data = r.json() 
	return str(ast.literal_eval(str(data))['data']['translations'][0]['translatedText']);


if __name__ == '__main__':
	app.run(debug = True)
