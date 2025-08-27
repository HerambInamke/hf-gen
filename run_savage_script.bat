@echo off
echo Starting SavageScript...
cd %~dp0
call venv\Scripts\activate.bat
python src\savage_script.py
pause
