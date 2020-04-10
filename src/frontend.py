import os
from datetime import date
import requests
from flask import Flask, jsonify
import json

trivia_address = os.getenv('TRIVIA_ADDRESS')
f_debug = os.getenv('DEBUG')
f_host = os.getenv('HOST')
f_port = os.getenv('PORT')

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_trivia():

	#getting date format (day-name, dd month-name yyyy)
	fdate = date.today().strftime('%A, %d %B %Y')

	#getting the trivia related to the date
	try:
		r = requests.get(f'{trivia_address}/v0/trivia')
		r.raise_for_status()
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

	payload = json.loads(r.text)
	trivia = payload['trivia']
	
	return f'Today is {fdate}\n\n<br/><br/>FUN FACT:\n<br/>{trivia}'

@app.route('/healthcheck', methods = ['GET'])
def get_health():

	return jsonify({'status': 'OK'}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':

	if trivia_address is None:
		print ("please input the trivia server host address into \"TRIVIA_ADDRESS\" environment variable")
	else:
		app.run(debug=f_debug.title(),host=f_host,port=f_port)