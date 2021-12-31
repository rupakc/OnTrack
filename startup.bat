@echo off
SET frontend=C:\Users\rupachak\Documents\GitHub\OnTrack\Frontend\app.py
SET backend=C:\Users\rupachak\Documents\GitHub\OnTrack\Backend
SET mongodb_path=C:\Users\rupachak\Downloads\mongodb-win32-x86_64-2008plus-ssl-3.7.8\mongodb-win32-x86_64-2008plus-ssl-3.7.8\bin\mongod.exe
start cmd /k %mongodb_path%
start cmd /k python %frontend%
cd %backend%
python app.py runserver 0.0.0.0:8000
