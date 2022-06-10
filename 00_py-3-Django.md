# Folder - py-3-Django

Here I do learn and test Django related topics. Most of the folders are projects from tutorials.

## Overview

1. djproject_AlanSimpson  --OKAY--
This is a Udemy course based on Django 2. I learned to use class based views. I can use it as a framework for CRUD based applications.

2. Focus on: Test driven django on youtube.

3. Focus on: prototype fund (Medicines Patent)
   - Digital Ocean and uberspace (mysql test)
   - Content

## Goals

1. Basic - learn Django with Bootsrap --OKAY--
2. Django REST Api, React or Angular , HTMX
3. Django testing
[Automated Tests - Day 6 - Django Bootcamp](https://www.youtube.com/watch?v=5E_xLmQXOZg)

## Django Testing Series

[Django Testing - Intro. to testing in Django-](https://www.youtube.com/watch?v=swEjbCW9XDY)   7:44
[Django Testing - Model Testing Introduction](https://www.youtube.com/watch?v=GBgRMdjAx_c)
[Django Testing Tutorial - What Is Testing? #1](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
4. Django GIS
[https://www.youtube.com/playlist?list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ](https://www.youtube.com/playlist?list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ)
5. Django deployment on uberspace, digital ocean (App, Linux Server, Kubernetes), heroku
6. Django in enterprises vs Spring
7. Test for prototype.de, finacial modelling, hybiom, biologika
8. Job Market monitor, dev/job-workspace

## Developemnt und Dsign decision

- I have a git ripo for /djproject_AlanSimpson
- open VScode from 04_src/Python-Django/ Select .env . OPEN Terminal New and select powershell, which will activate the .env.
- test for sqlite, mysql (uberspace) , digital ocean (postgree)
- target Win10 , uberspace , digital ocean.
- conda is not suitable for Django development.
- target Django 3.2 and Python 3.9 / 3.10
- I do not use the django plug-in for VScode since it prevents Emmet to work, however, this can be fixed.

## Situation, Reasoning , and nexts tings to do ---

1. Start: 08-09-2021 new , Precurser: dd-mm-yyyy name 
2. What are the resources (time, finance, energy) ? 1-2 h/day, no finance, middle)
3. What has been done ? Have SP to create a .env with multiple projects. Started muliple tutorials, , installed Django on ubersapce, digital ocean, downloaded Django Documentation (Caliber)
4. What did not work ? env_Django does only work with the cmd terminal in VScode

5. What are Concepts, Diagrams, Reasoning, Outlook.

>N: Git set-up , uberspace deployment, do the Django Doc polls tutorial.

## Prerequits for SPs ---

- What intepreter / virtuell machine / packages / modules / files / folders
- Do I have git ? Which server repository ?
- Where is this code synced to ? How ?
- Does is run on Win10 , ubespace , android ?

>SP: Document structure and procedure

``` text
USE---- name of structure to use
CREAT-- folder, file, object etc.  
COPY--- "01_ProjectTemplate.md" into new \folder\ and change
     -- the of the file to 00_<Name of folder>.md
VERB--- documention of set-up, SP and progress (Journal section)  
```

>Creating an environment

``` text
OPEN---- Terminal
CLI----- movde to the folder, where I want to create my environment. 
TYPE---- py -3.10 -m venv .env
```

>SP: Adding packages to the environment

``` text
TYPE
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt
```

>SP: Updating package in the environment

``` text
TYPE---- python -m pip install --upgrade django
TYPE---- python -m pip install Django==3.2.13
```

>SP: Upgrade python in an environment [YVI](https://www.youtube.com/watch?v=y6xdIumaEy4)

``` text
ACTIVATE---- python virtual environment
TYPE-------- py -3.10 --version     # check what version I have before upgrade
             py -3.9 --version
DOWNLOAD---- Newest python version
INSTALL----- Downloade python version
TYPE-------- py -3.10 -m venv --upgrade (path/toMy/.env)  # Does not work since I do not have the permission apperently.
TYPE-------- py -3.10 --version
             py -3.9 --version      # check what version I have after upgrade


PS C:\Users\raine> py
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.executable)
C:\Program Files\Python310\python.exe
```

>SP: Delete git from a folder and from

``` text
OPEN------- git-bash or Windows Terminal in folder with .git.
TYPE------- git remote remove origin
DELETE----- .git folder
OPEN------- github.com account
GOTO------- repositor you want to delete
CLICK------ Setting
GOTO------- Danger Zone
CLICK------ Delete Repository 


## References ---

1. Guideline: Set-up a development environment, which works within the folder where it is living. Use always relative path.
2. [Markdown Guide](https://www.markdownguide.org/) -> Markdown Syntax and related Software.
3. [GIThub flavored Markdown GFM](https://github.github.com/gfm/#what-is-github-flavored-markdown-) -> I use GSM specification, which is very detailed.  
4. Guideline .md: To create a new line, I use two spaces at the end of the line.
5. [Djagno Tutorial for Beginners 2021, Programming with Mosh, youtube](https://www.youtube.com/watch?v=rHux0gMZ3Eg) This course is the first houer of a longer course. I saw the entire youtube video.
6. [Python Django Web Framework - Full Course for Beginners, freeCodeCamp.org, youtube](https://www.youtube.com/watch?v=F5mRW0jo-U4) This course is based on a course from [Coding for Entrepreneurs](https://www.codingforentrepreneurs.com/). The course dives into different concepts of python. Has a nice Course Content. The code can be found [here](https://github.com/codingforentrepreneurs/Try-Django-3.2). He uses MAC, django 2.0.7, python 3.6. Editor: Sublime Text.

>N: True ? Win10 scritp/activate , Linux bin/activate  -> 0:22.27 6-Settings

7. [Djgaon 1.4 Workshop, Deutsch](http://www.django-workshop.de/index.html)
8. [Django Admin Site Series, youtube, playlist](https://www.youtube.com/watch?v=c_S0ZQs81XQ&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO)
9. [Django ORM Mastery Series](https://www.youtube.com/watch?v=XbOUjyC--Ao&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=2)
10. [Python Django 7 Hour Course, Discord-like app, Traversy Media, Denis Yvy, youtube](https://www.youtube.com/watch?v=PtQiiknWUcI&t=94s)
11. [Python-Django learning Path, Very Academy, Github](https://github.com/veryacademy/django-learning-pathway)
12. [Python-Django, freecodecamp, GOOGLE API](https://www.youtube.com/watch?v=_vCT42vDfgw)

## Journal (today on TOP --OKAY--)

### FRI 03-06-2022

-1- I tried C:\Users\Public\03_src\py-3-Django\a1_DJP006_eCommerce-V2 on Onedrive, which worked, but I prefer to work with git to sync code. See SP

### THU 21-04-2022

-1- Installed latest version of pyhton, Django 3, 4, Sphinx
-2- Updated the >SP: to deal with environments.

``` text
PS C:\Users\Public\03_src\py-4-Django> py -3.10 --version
Python 3.10.4
PS C:\Users\Public\03_src\py-4-Django> py -3.10 -m venv .env
PS C:\Users\Public\03_src\py-4-Django> ls

    Directory: C:\Users\Public\03_src\py-4-Django

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          21.04.2022    17:05                .env
d----          15.03.2022    14:43                doc-Django-4
-a---          21.04.2022    14:41           2089 00_py-4-Django.md

PS C:\Users\Public\03_src\py-4-Django> .env\Scripts\Activate.ps1
(.env) PS C:\Users\Public\03_src\py-4-Django>
```


### TUE  02-12-2021

-1- I creatd the 01_LearningPath.md file, which is based on Very Academies github file.
//PUB/03_src/python-django/01_LearningPath.md

-2- I will focus on DJ003-Core-ORM-Mastery.

### TUE  24-11-2021

-1- Automate EDGE and Django start - I made a PS script, however I cannot switch between the switches since after running "python manage.py runserver" the settings are such that the first application, which I did run with the file, will be started.
[Automate Edge use](https://stackoverflow.com/questions/65971109/powershell-and-microsoft-edge-automation)
>N: Look in to the way I have organised .env folder. Maybe I have to make a .env for each project.

-2- Django Rest Frameworke - I started with the Very Academy tutorial. \DRF_VeryAcademy

-3- Learning path - I focus on learning everytin from Very Academy. There is a nice learning path on his git-hub page. I started already with. I became member, but as RivesRolle !! I canceled immediately, but I am now member until 24.12.2021.

1. ORM Mastery - see ref 9. above. I use the /JsonModel_ORM-VeryAcademy/
Created folder finished PL01 - What is the Django ORM.
>N: Get code

2. Pytest Masteray - /pytest_VeryAcademy/ 
created folder, finished 3 tutorial but had a hard time to follow. I need more background.
>N: get code

3. Django Rest Framework - /DRF_VeryAcademy >N: get code
created folder started 1 video, but feel I need to do the ORM Mastery first.
>N: get code

4. Django - Ecommerce Project v2
Outlook

- Test first approach
- Django Templating , Django DRF , Django Graph QL 
- Docker and PostgreSQL Database

Project Brief

1. Online store capabilities selling various branded merchandise
2. Customer interactins - product comments / reviews
3. Website keyword search form with robust search and filter functionality
4. Live chat hels desk (Django channels)
5. Customer coupon system
6. Customer portal

Database Tables

1. 


### TUE  23-11-2021
-1-  aaJsonModel - How can I upload data in to complex data schemas using Django.
 
-2- RestFul API- UnternehensDjango-Xi 
[Learn Django Rest Framework, Very Academy, youtube](https://www.youtube.com/watch?v=soxd_xdHR0o&list= )
>N: 40:00

-3- Compare Django Tutorials - feecode camp vs. Very Academy  vs. 


### FRI  19-11-2021
-1- Data upload into Django databases- This command allowed me to export the data from djproject videos.video database table.

``` text bash
python manage.py dumpdata videos.video --indent 4 -o dump2.json  
```

>N: Try to upload .json data with _> python manage.py loaddata dump2.json.  Test the use of "pk": 55,  variable.


### TUE  09-11-2021
-1- Documentation ¦ Microsfot Virutal Academy Django Documentation - I removed the video recordings form "Django in the Real World" Kursleiter: Susan Ibach, Christopher Harrison Veröffentlicht:16 December 2015
Christopher talks a lot and the Django version is too old. However, it was a good introduction. They used Visual Studio Community,  which I do not use anymore.
There was another Django vidoe  series, which I deleted. I learned from these videos in 2016.
[Christopher Harrison, Django, Microsfto, website](https://developer.microsoft.com/en-us/advocates/christopher-harrison)
[Susan Ibach, made videoswith Ch.Harrisson, website](https://susanibach.wordpress.com/)

### MON  08-11-2021

-1- A possible learning path
[Python (PL) - Beginners (VScode, py 3.9), Very Academy youtube, Zander](https://www.youtube.com/watch?v=uIyh06z6wyI&list=PLOLrQ9Pn6cazZScthXI-gMQv-YrDUMnlY)
[Python Async (PL) - Beginners+](https://www.youtube.com/watch?v=7LU1npoPmcg&list=PLOLrQ9Pn6caw9TyTdCQGJuUAqtRxPfPRd)
[Python Code Challange (PL) - Beginners](https://www.youtube.com/watch?v=esHMjvP2-hs&list=PLOLrQ9Pn6cayQKCYhGH4FLTgIWTUI9yx7)
[Python Lamda - Intermedia (PL)](https://www.youtube.com/watch?v=yetjswpSAsA&list=PLOLrQ9Pn6caws6aPJoCD_UmWRE91257Xm)
[Python Excel (PL), Very Academy youtube, Zander](https://www.youtube.com/watch?v=bI68wnoINwc&list=PLOLrQ9Pn6cawzy79Yu5Tg4GgpVe9azwpK)

[Django - Ecomerce v2 (Win10, py 3.9, Django 3.2) (PL), Very Academy youtube, Zander](https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh)
[Django Selenium](https://www.youtube.com/watch?v=XnSQ6sRGKzI&list=PLOLrQ9Pn6cazIlOgYD8w4t_aRoaPb_kmS)
[Django Pytest Mastery (PL), Very Academy youtube, Zander](https://www.youtube.com/watch?v=LYX6nlECcro&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY)

### TUE  02.11.2021
-1- Emmet and Django Plug-in - Today I learned that the Django plug-in blocks the use of Emmet.  I deinstalled the Django plug-in therefore. However, there  is a way to use both, for which I have to add some lines of configuration into the settings.json file. see Django plug in introductions.  

### THU  07-10-2021
-1- This a nice tutorial from CodingEntrepreneurs [Try Django 3.2, (PL), youtube](https://www.youtube.com/watch?v=SlHBNXW1rTk&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL)

-2- DigitalOcean, Django, Ubuntu, Gunicorn. I shall use this tutorial during my 60 day trial. It might be base for my own Django server.

### MON  13-09-2021

-1- I tryed to run the UnternehmensDjango_iX application. I need the crispy_forms module. More importently 
    I learned how to manage config/requirements for deployment and development.

### WED  08-09-2021

-1- I decided to participate in prototype fund. I will use the Django framework to propose a project.

-2- I want to have a set-up to with VScode to github to uberspace.

### THU  18-03-2021
-1- Created this document 
I created the folder earlier, this year when I started to work on deployment in on Digital Ocean.

-2- Django in Enterprise article iX.
I downloaded the code and documents from this article. Christian Leubner, 1.12.2020 iX
/https://www.heise.de/ratgeber/Django-Erweiterungen-Anwendungen-unternehmenstauglich-machen-mit-wenig-Aufwand-4970925.html 

### SUN  22-02-2020   ---

-1- file .md  
Updated this .md file.

-2- python¦Sion-Desk¦Naples-Lab
I want to learn how to work on two different computers on python code, which I later use on the ubserspace server.










	
	
