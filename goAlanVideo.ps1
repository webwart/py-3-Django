# Author: RKW
# Date:	220222
# Description: This is a powershell script to start Alan S. Video Django App in \03_src\python-Django\djproject_AlanSimpson
# Usage: a) Find link "AlanVideo", right click, EXECUTE W. POWERSHELL 
# amini <--1> n-it Django Ami

Write-Host "--Start Alan S. Video Django Application and VScode/dj_AlanSimpson --"
Write-Host "------------------------------------------------------------------"

# Start Django App
Start-Process -FilePath 'http://127.0.0.1:8000/'
.\.env\Scripts\activate
Set-Location .\djproject_AlanSimpson
python manage.py runserver

# Start-Sleep -Seconds 3
# Start-Process microsoft-edge:http://127.0.0.1:8000 -WindowStyle maximized
