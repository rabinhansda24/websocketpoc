from gevent import monkey
monkey.patch_all()
import json
import time
from app import app, socketio, thread, thread_lock
from flask_socketio import emit
from flask import request, make_response, jsonify
from app.functions.tasks import get_all_tasks
from app.thread_functions.tasks_thread import task_scheduler


@app.route('/')
def hello():
    return "Hello, World!"

@socketio.on('get_tasks', namespace='/api/v1.0/tasks')
def getAllTasks(message):
    res, status = get_all_tasks()
    emit('get_tasks_response', {'data': json.dumps(res)})

@socketio.on('connect', namespace='/api/v1.0/tasks')
def test_connect():
    print("----Client Connected------")
    global thread
    ms = {
        "Message": "Connected to server"
    }
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(task_scheduler)
    emit('get_tasks_response', {"data": json.dumps(ms)})

@socketio.on('disconnect', namespace='/api/v1.0/tasks')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app, debug=True)

