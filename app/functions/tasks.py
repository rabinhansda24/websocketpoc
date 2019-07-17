import pymysql
import datetime, json
from app import db, cursor

 
def get_all_tasks():
    sql = "SELECT * FROM tasks"
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        data = []
        for rec in result:
            task = {
                'task_id': rec[0],
                'robot_id': rec[1],
                'task_name': rec[2],
                'issued_time': json.dumps(rec[3], default=str) ,
                'scheduled_time': json.dumps(rec[4], default=str),
                'status': rec[5]
            }
            data.append(task)
        
        status = 200
        res = data

    except Exception as e:
        print("Error: unable to fetch data.")
        print(e)
    
    return res, status