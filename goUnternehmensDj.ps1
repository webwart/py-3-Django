# Author: RKW
# Date:	220222
# Description: Powershell script starts Unternehms iX Django App in /03_src\python-Django\UnternehmensDjango_iX
# Usage: a) Find link "UnternehmDj" on Destop, right click, EXECUTE W. POWERSHELL 
# root <,mn> root


Write-Host "--Start Unternehmens iX Dj Application --"
Write-Host "-----------------------------------------"

# Start Django App
Start-Process -FilePath 'http://127.0.0.1:8001/'
.\.env\Scripts\Activate.ps1
Set-Location .\iX_django-master
python manage.py runserver 8001

# Start-Sleep 5
# Start-Process microsoft-edge:http://127.0.0.1:8000 -WindowStyle maximized