import os
from datetime import date
import requests
from flask import Flask, jsonify

b_debug = os.getenv('DEBUG')
b_host = os.getenv('HOST')
b_port = os.getenv('PORT')

app = Flask(__name__)

@app.route('/v0/trivia', methods = ['GET'])
def get_trivia():
	
	# getting today's date in numerical format
	today = date.today()

	# requesting the trivia related to the date
	try:
		r = requests.get(f'http://numbersapi.com/{today.month}/{today.day}/date')
	except requests.exceptions.HTTPError as errh:
		print ("Http Error:",errh)
		raise SystemExit(errh)
	except requests.exceptions.ConnectionError as errc:
		print ("Error Connecting:",errc)
		raise SystemExit(errc)
	except requests.exceptions.Timeout as errt:
		print ("Timeout Error:",errt)
		raise SystemExit(errt)
	except requests.exceptions.RequestException as err:
		print ("OOps: Something Else",err)
		raise SystemExit(err)

	return jsonify({ 'trivia' : r.text })

@app.route('/healthcheck', methods = ['GET'] )
def get_health():

	return jsonify({'status': 'OK'}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':

    app.run(debug=b_debug.title(),host=b_host,port=b_port)