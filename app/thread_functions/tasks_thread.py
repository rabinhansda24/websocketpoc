import logging
import re
import json
import time
import datetime
import schedule
from app.functions.tasks import get_all_tasks
from app import db, cursor, socketio
from datetime import datetime as dt


def task_scheduler():
    print("---Thread started---")
    status_ref = ['SCHEDULED', 'ACTIVE', 'COMPLEATED', 'PREEMPTED', 'REJECTED']
    tasks, status = get_all_tasks()
    while True:
        for task in tasks:
            print("in thread::", task['task_name'])
            task_id = task['task_id']
            issued_time = task['issued_time']
            scheduled_time = task['scheduled_time']
            st = task['status']
            scheduled_time = scheduled_time[1:-1]
           
            str_time = str(datetime.datetime.now().time())
           
            tmp = str_time[0:str_time.find('.')] 
            
            if len(scheduled_time) == 7:
                scheduled_time = '0' + scheduled_time
            
            print(tmp, scheduled_time)
           
            if tmp == scheduled_time:
                print("found::", task['task_name'])
                index = status_ref.index(st)
                new_status = status_ref[index + 1]
                sql1 = "UPDATE tasks SET status= '%s' WHERE task_id = %d" % (new_status, task_id)
                print(sql1)
                cursor.execute(sql1)
                db.commit()
                res, status = get_all_tasks()
                print(res)
                socketio.emit('get_tasks_response', {"data": json.dumps(res)}, namespace='/api/v1.0/tasks')
                
            

        time.sleep(1)
    print("---Thread finish---")