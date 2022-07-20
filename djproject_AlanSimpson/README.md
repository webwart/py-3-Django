# djproject_AlanSimpson 

I test the use of the github READ.md file. I followed the tutorial from Alan Simpson and  adapted the code to my needs. 


## set-up

[Alan Simpson Web Site](https://alansimpson.me/)
[Udemy Course Page for Django 2 Tutorial by Alan Simpson](https://www.udemy.com/course/hands-on-django-2/)
[Alan Simpson Gitrepo for Django Tutorial](https://github.com/AlanSimpsonMe/django2-starter-kit)

I do run the commands on Sion-Des and Naples-Lab. db.sqlite3 is not saved by Github. 




I use /PUB/04_src/Python-Django/.env  On Naples-Lap this py 3.9

Auflistung der Ordnerpfade
Volumeseriennummer : C20B-F222
C:.
└───_djproject   # Webseite / Projectname
    └──
    
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       17.04.2020     21:05                _djproject      #  here we have the url.py file which is looked up by the web-server
-a----       17.04.2020     21:16            127 00_djprojecct.md
-a----       17.04.2020     21:14         131072 db.sqlite3
-a----       17.04.2020     20:59            651 manage.py

django-admin startproject _djproject
cd .\_djproject\
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

### 05-Video-AS_Apps

1. An App is  portable unit of functionality. Name it withlower-case characters no special characters. The name should be plural (posts) of the Apps main model (Post).
2. Allways two steps to adding an App: a) python manage.py startapp <appname> b) Add app name to INSTALLED_APPS in settings.py.
3. Create allpages in which I will have css , images , javascript , basehtml
4. TYPE: python manage.py startapp allpages , then add to _djprojecct/settings.py
5. TEST:  python manage.py runserver  
''' python
INSTALLED_APPS = [
    'allpages.apps.AllpagesConfig'
'''
### 06-Video-AS_Apps
Created the following folder structure:  
(env_numAiDjango) PS C:\Users\Public\03_src\python\_djproject> tree allpages
Auflistung der Ordnerpfade
Volumeseriennummer : C20B-F222
C:\USERS\PUBLIC\03_SRC\PYTHON\_DJPROJECT\ALLPAGES
├───migrations
│   └───__pycache__
├───static
│   └───allpages
│       ├───css
│       ├───images
│       └───javascript
└───__pycache__

### 07-Video-AS_Aptps
created stylesheet.css file

### 08-Video-AS_Apps
Google fonds

Headings: Montserrat
Body Text: Source Sans Pro
Code Samples: Source Code Pro

### 09 Define your Site-Wide Picture and Colors
Used paint.net to prepare pictures.
Used the color.adobe.com wheel to select a color combination with Hex codes.
Sion-Des:\djproject\allpages\static\allpages\css\stylesheet.css
Sion-Des:\djproject\allpages\static\allpages\images\djangopony.png

>N: Update oneDrive

### 10 A Master Template

Created HTML file in _djprojct/allpages/templates/allpages/base.html

### 11 Add Header, Footer, Navigation

``` html
<body>
    <Header>Haeder</Header>
    <nav>Nav
    </nav>
    <main>
    </main>
    <footer>Footer</footer>
</body>
``` 

### 12 add Front Awesome and Bootstrap CDN link
Into the header of base.html I added the links

### 13 Master the Django Template Language
Used in .html files. Executed on the server
{% executable code %}
{{ variables }}   -> Vriable is replaced by the contents of the variable.
{#  comments #}

added code to base.html to find the _djproject/static in which link to /allpages/css/stylesheet.css

### 14 Create your Site's Home Pages

Used {% extends base.html %} to make .html pages. This brings all the tags and content from base.html

{% block maincontent %}
    page content (tags and text) go here
{% end block maincontent %}

### 15 Logo and Socia Media 

In need to use {% static .....} to link to the static/image or static/css folder. I added a logo, the stylesheet, and Social media link

### 16 Create my first view

1. client request -> urls.py -> views.py (gathers the data to fill into the template)-> template.html 
2. Each view is a function or a cloass. Here we use functions. If there is no content: def home_view(request): return render(request, 'path/t0/xxx.html)
3. The /templates/ folder is assume. No need to show in the path.

### Direct Trafic17 url.py
1. The first urls.py always seen by the request is in the project folder  -djproject/_djproject/urls.py
2. add this line to the URL patter list: path('about/', views.about_view, name='allpages-about'),

### 18. stylesheet.css
1. Added css code for header, footer, and nav bar.
2. >!!: The body { backbround-color: yellow } did not work !!
3, >IMPORTANT: To see the changes in the CSS in the browser, I used CTRL-RELOAD !!

### 19. background stylesheet.css
1. Reference to a website where  I can generated a gradien of color and obtain the CSS code
2. >!!: I could not change backbround color, gradien, or add the background picture. !!

### 20. Create your Site-Wide Navigation Bar 

1. Go to base.html to manage NAV bar.
2. Needed to adjust stylesheet.css to bring NAV bar to the right.

### 21 Understanding HTTP Status Codes

Well not much very new information. 

### 22 Create a Favicon

[Favicon Generator ](https://favicon.io/)

### 23 Pass Titles to Pages with DJango Template Language

### 24 Create your git files Easy Way

### 25 Upload your site to github

### 26 Retrieve your code from github

### Creating Django Models ( 2 Std. 44 Min.)

### 27 Make your First Model

Explains tables ; Sets github enables = false in VS Code .json file (Settings) ; python manage.py startapp videos and add to settings.py; 4:10 creating a model ; Models Take care of the primery key ; I type or copied text from github Alan Simpson ; Made migration

``` powershell

(.env) PS C:\Users\Public\03_src\python-Django\djproject_AlanSimpson> python manage.py makemigrations
Migrations for 'videos':
  videos\migrations\0001_initial.py
    - Create model Video
(.env) PS C:\Users\Public\03_src\python-Django\djproject_AlanSimpson> python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, videos
Running migrations:
  Applying videos.0001_initial... OK
(.env) PS C:\Users\Public\03_src\python-Django\djproject_AlanSimpson> 


```

### 28 Access your Data from the Admin Account

I have three ways to add Data:
1. Manually with Django Admin
2. Upload from Spreadsheet
3. Use third party tool.


In /videos/admin.py I need  to only. Now I can log-in as a super  user and add records.

``` python
from videos.models import Video
# Register your models here.

#Allows you to access database through the Admin page
admin.site.register(Video)

```

### 29 Import from CSV or Excel to SQL Tables

``` SQL
INSERT INTO videos_video SELECT null, title, author, description, youtube_vid, stars_count, category_id, skill_level_id, 1, datetime('now'), datatime('now') from YouTubeVideos
```

This module was difficult. a) I could not use the unique= True b) when I removed the contrain, the tabel vidoes_video moved the "title" column, whic was  probably due to the fact that I had to do migrations again. However, I got also experience In diealing with makemigrations  and the migrate command.

### 30 From Database to Web Page

in view.py he usess class and not functions. 

### 31 Directing Traffic to Videos

Use /videos/urls.py file with the include statement  in _djproject_AlanSimpson/urls.py
GO TO   localhost/video/list , video alone is nothing.

### 32 Formatting Database Date (Output)

I could use bootstrap classes for list with Data. Code for a list with  <ul> <li>. Explains use of sqllit plug-in (Very nice !) . Explains the youtube 11 character link. 3:18 Code to add a link. 4:30 Code adding a table,  see video_list_m4s20-AddTable.html. 6:50 Code , no hyperlink , each row is clickable. 8:00 adding CSS 

### 33 Showing Video Thumbnails

Make VideoThumbsView class in videos/views.py. Remember to use new template_name  othewiseit will look for video_list.html. Change urls.py, views.p 2:00 changing video_thumbs.html 5:50  CSS

### 34 Filtering Data

Using category_id to select for video-categories and to display the videos from the category. 5:00 Select category in allpages/index.html. 6:00 Adding buttons to allpages/index.  >N:  9:00 change object_lis name, which is another default variable provided by Django.

### 35 Create a page for Watching Videos

Use of DetailView class, Got code from https://alansimpson.me/  6:20 be carefule to use  'detail/<int:pk>' which links to the id  field in the videos_video table of th db. In urls.py. 8:00 Changes to video_thumbs.html . In there I keep the link to the youtube site. 10:20 CSS.
>N: The size of the video window is too small. I might have to do with the CSS iframe.

>N: ### 36 Avoid a Lot of Coding with Generic Editing View


## References

/03_src/python/django-AlanSimpson
............../_djproject

[VideoTutorial](https://www.udemy.com/course/hands-on-django-2/) -> Alan Simpson's video tutorial on Udemy
[SuperUser](https://djangowaves.com/tag/tips-tricks/)  ->  Has an article about superuser


##  Journal (today DOWN)

### SUN  19-04-2020
-1- set-Up¦Naples-Lab¦OneDrive-Rai¦Sion-Des
I have starte with Allan simpson on Sion-Des . With git I get all the files on Naples-Lab, but not db.sqlite3 which is ignored by gitignor.
I also started a set-up Onedrive.
>N: Check if I have on Naples-Desk also Django 3.0. ? Find out how to deal with it since the tutoriala and überspace uses Django 2.0.

### FRI  01-05-2020
Until now I learned how to use html templates and link them together. Now I will learn how to 

### WED  06-05-2020
Added Python Django to the launch file.
>N: 18 Make things pretty

### MON  01-06-2020
-1- Naples
I did clone from git /python/. Creted in anaconda the env_NumAiDjBs environment. In VScode I did run: manage.py migrate , manage.py runserver. Then I created the superuser.

``` text
.> manage.py migrate
.> manage.py runserver
.> manage.py createsuperuser --username=amin_Nap --email=rainer.warth@hotmail.ch
```

-2- Naples
I advanced with Alan Simpson UDemy Django class
>N: 20 Intenal Links

-3- Naples
Created Desktop icon which open conda ps shell  in /03_src/python/ and activate env_NumAiDjBs. For SP see
python.md.

### MON  28-12-2020
-1- I refactored files and folders. I moved the Alan Simpson final version of the project to. 
\Public\03_src\python\_djproject_AlanSimpson\doc

### WED  27-01-2021
-1- I forked djproject_AlanSimpson, so I have porject I can use for the django deployment tutorial. I created a new repo on github and added a requirements file to the project.

The requirements.txt file did not work on the digital ocean server.

This project has its own repo on github. I can use VScode or git bash.

### SUN  03-10-2021

-1- Django¦Refactor¦.env ---- I created the .env environment. The djproject_AlanSimpson is no in /PUB/04_src/python-Django. This folder has the same set-up as /PUB/05_src/14_Django/. This allows me to test Django techniques in the same set-up which use for the deployement from /05_dev/ 

### WED 13-10-2021

-1- Django¦Table HTML¦Database¦Table CSS --- I nicely progressed. In module 32. I had several version of video_list.html, where I the code where deleted from one version to another. To document this  I made for each stade a file.
