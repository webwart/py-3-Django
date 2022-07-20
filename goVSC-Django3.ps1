# Author: RKW
# Date:	220222
# Description: This is a powershell script to start Start VScode 03_src/py-3-Django
# Usage: a) Find link "VSC-Django3" on Destop, right click, EXECUTE W. POWERSHELL 
##


Write-Host "-- Start VScode 03_src/py-3-Django --"
Write-Host "------------------------------------"

# Start VScode
Set-Location C:\Users\Public\03_src\py-3-Django
code .

# Start Django App
# Start-Process -FilePath 'http://127.0.0.1:8000/'
# .\.env\Scripts\activate
# Set-Location .\djproject_AlanSimpson
# python manage.py runserver

# Start-Sleep -Seconds 3
# Start-Process microsoft-edge:http://127.0.0.1:8000 -WindowStyle maximized
