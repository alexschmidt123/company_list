# company_list
flask app to show company information

How to use:

1. Download the file and unzip it
2. Open MySQL Workbench and create a new schemas named "company_schema"
3. Open the configuration file at company_list\flask_app\config\mysqlconnection.py and modify user and password to match your local database at line 6 and line 7
4. Open the terminal, and type "cd [unzipped folder's path]" 
5. Check whetehr your PC is equipped with "pipenv". If not, you can google it. There are many methods to install "pip" and "pipenv" on the Internet.
6. Type "pipenv install flask PyMySql" in terminal. This step is to install necessary python packages.
7. Type "pipenv shell" to activate the environment. 
8. Type "python server.py" to activate flask app
9. Open the browser and open the address "http://localhost:5000/". The flask app works at port:5000.

Finish all steps and you can have access to this flask app.