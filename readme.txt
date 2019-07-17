Description:
------------
There is a table called task in MySQL that has Task_ID (UNIQUE INTEGER), Robot_ID (UNIQUE INTEGER),
Task_Name (VarChar), Issued_Time (TIME), Scheduled_Time (TIME), Status (VARCHAR) fields. There are 5 robot who have 10 tasks in various stats of 
SCHEDULED, ACTIVE, COMPLETED, PREEMPTED, REJECTED. The status is changed in the server based on some condition, then the task list has to be send 
to client. 

Solution:
---------
To solve this I used Web-Socket. There will be a thread running in the background which check the conditio and update the status and then send the 
tasks list to client.

My Approch:
-----------
1. All the tasks of robot is stored in a table called task in MySQL
2. All task has issued time and scheduled time(my asumption: when this task will change the status)
3. Create a Web-Socket connection between server and client.
4. A thread will run in the background in server which check and update the status of a task based on the scheduled time. Status will be updated only in schedule time
5. The updated task list will be sent to client.

Technology & Framworks:
-----------------------
Backend:- Python, Flask, Flask-Socket IO, MySQL
Frontend: HTML, JQuery, Socket.io

Steps:
------
1. Create a REST API to get the task lists in Python & Flask
2. Create a frontend in HTML to display the tasks list
3. Call the REST API to get all task
4. Display the task list
5. Create Web-Socket connection between server-client
5.1. Integrate Flask-SocketIO with Python code
5.2. Integrate Socket.io with HTML & JQuery
5.3. Make connection with the REST API server from the frontend
6. On connect run a thread in background which check and update the status of the task
6.1. Send the updated task list to client
7. On receve the task list, update the task list table 

Installation instruction:-
--------------------------
Required:: Python, MySQL

1. This project can be installed on any architecture Windows, Linux, MacOS. One need a Python environment, it can be installed in host machine as well as in virtual environment (recommended). Please follow this link to install virtual environment (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

2. Activate the virtual environment

3. Please install all the required package from the 'requirements.txt' by following command:
pip install -r requirements.txt (Link: https://pip.pypa.io/en/stable/user_guide/)

4. Restore the SQL file included

5. Run the python project by running the bellow command:
python run.py

6. Open the index.html file in any mordern web browser that support Web-Socket

7. Wait and watch the status is changed automatically, there is no need to refresh the browser or click any button.

8. You can change the scheduled time to get the result immediately - optional 
