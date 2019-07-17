from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
import pymysql
from threading import Lock
from dbconfig.dbconfig import config

async_mode = None

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

db = pymysql.connect(
    config["DB_HOST"], 
    config["DB_USERNAME"], 
    config["DB_PASSWORD"], 
    config["DB_NAME"]
)

cursor = db.cursor()

if cursor:
    print("DN connect successfully!")