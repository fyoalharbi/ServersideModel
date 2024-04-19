from uuid import uuid4
from flask import Flask, make_response, request, jsonify
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials


app = Flask(__name__)

@app.route('/')
def index():
    return 'heeodujam'


if __name__ == '__main__':
    app.run()

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.Client()
voice_ref = db.collection('recordings')

@app.route('/verify', methods=['POST', 'GET'])
def verify():
    try:
        user = request.json['users']
        voice_ref.document(user).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error occured: {e}"


##@firestore.transactional
#def get_session_data(transaction, session_id):

    
"""

def identifyVoice(voice_path):
    voice = 

@app.route('/list', methods=['GET'])
def read():




@app.route('/delete', methods['GET', 'DELETE'])
def delete():

"""