## Step1-At root
python -m venv fastapi-env
## Step2-At root
.\fastapi-env\Scripts\activate  [say yes to the workspace folder]
## Step3-At root
pip install fastapi uvicorn gunicorn numpy
## Step4-
pip freeze > requirements.txt 
- Take a snapshot of all the currently installed Python packages in my virtual environment and write them to a file called requirements.txt
## Setp5-
pip install -r requirements.txt 
- to reproduce the lib setup

------------------Run Project--------------
# Startup Command - 
python -m uvicorn src.fast-api-app.main:app --host 0.0.0.0 --port 8000

Other Startup Command to try
uvicorn src.fast-api-app.main:app
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.fast-api-app.main:app --bind 0.0.0.0:8000

=======

uvicorn src.fast-api-app.main:app --reload
uvicorn server
main refers to the main.py file.
app refers to the FastAPI instance created in main.py
--reload enables automatic reloading of the server when you make changes to your code

Local:
http://127.0.0.1:8000/
{"Hello":"FastAPI World"}

http://127.0.0.1:8000/name/Guest
{"Hello":"Guest"}

http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/docs
