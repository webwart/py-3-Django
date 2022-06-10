# This is powershell script to start django Alan Simpson.

Write-Host "Start Dja Alan Simpson"
Get-Location
.\.env\Scripts\activate
Set-Location .\djproject_AlanSimpson
python manage.py runserver
Start-Sleep 5
Start-Process microsoft-edge:http://127.0.0.1:8000 -WindowStyle maximized