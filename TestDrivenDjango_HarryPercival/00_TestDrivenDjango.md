# 00_05_devTTDMiPub.md

# 00_TstDrivenDjango_HarryPercival The testing goat

Introduction - This is a tutorial based on the book of Harry Percival. I learn to use git, geckodriver for testing, testing with Python/Django.

History - I have started probably in 2017 to work with this book. The files moved through several directories. This directory moved a around a bit. I on Milano Public , has a git , moved from 05_devTTDMilPub (deleted) to here.

## Goals

1. What do I want to learn / develop / produce ? I learn the to use git, testing, Django.
2. Where is it used in production ? I want to submit it to the prototypefund competition
3. Timeline / Deadline ? 30-09-2021
4. Deliverable ? Uberspace Django installation and git-repo.
5. I want to learn how to work on two different computers on python code, which I later use on the ubserspace server.


## Situation, Reasoning , and nexts tings to do

1. Start: dd-mm-yyyy new , Start: dd-mm-yyyy name of precurser project
2. What has been done ? On Naples_Lab: conda/env_django, geckodriver intstalled 
3. What did not work ? 
4. What are the resources (time, finance, energy) ? time 10 x 8, 0 CHF, 50%
5. What are Concepts, Diagrams, Reasoning, Outlook ? I need to learn how to keep my secrets out of the git repository.

>N: Create git-repo and install on U7/Hybiom 

>N: What does this mean.I created the /note/ directory where I have the code from TDD goat. I use there a locl git repo.
Here I want to use github repo.

## Prerequits for SPs

- What intepreter / virtuell machine / packages / modules / files / folders ? conda env_Django
- Do I have git ? Which server repository ? --
- Where is this code synced to ? How ? --
- Does is run on Win10 , ubespace , android ? Win10, U7

>SP: Document structure and procedure

``` text
USE----name of structure to use
CREAT--folder, file, object etc.  
COPY---"01_ProjectTemplate.md" into new \folder\ and change
     --the of the file to 00_<Name of folder>.md
VERB---documention of set-up, SP and progress (Journal section)  
```

## References

1. Guideline: Set-up a development environment, which works within the folder where it is living. Use always relative path.
2. [Markdown Guide](https://www.markdownguide.org/) -> Markdown Syntax and related Software.
3. [GIThub flavored Markdown GFM](https://github.github.com/gfm/#what-is-github-flavored-markdown-) -> I use GSM specification, which is very detailed.  
4. Guideline .md: To create a new line, I use two spaces at the end of the line.
5. Harry Parcival's book - Test driven development with python. http://chimera.labs.oreilly.com/books/1234000000754/index.html

## Journal:

### TU 14-06-2016

-1- Open the filezilla and go to /home/webwart/dev/MyDjangoProject/polls. This gives you immediately an ideawhere I am.  I am probably somewhere in the part3 – Write views that actually do something
I have to remember that some changes I need to make are sometime in the directory
/home/webwart/dev/MyDjangoProject/MyDjangoProject. Especially in the files url.py and settings.py

### TUE 19-12-2017
OPEN	www.github.com  account webwart.  
CREATE	Repository webwart/gitTDDtest  
OPEN	Git bash on Milano  
TYPE	git init in \PUB\devTddMilPub\gitTTDtest  
CREATE	aFileOnMil.py  
TYPE	$ git add aFileOnMil.py  

```
	$ git commit -m 'Commit 1 for aFileOnMil.py '
	$ git status
	 On branch master
	 nothing to commit, working tree clean
	$ git remote add origin https://github.com/webwart/gitTDDtest.git   # tells git where distant repo is
	$ git push -u origin master
	$ git status
	 On branch master
	 Your branch is up to date with 'origin/master'.

	 nothing to commit, working tree clean
	$ exit
```

I then added this file (00_gitTTDtest.txt) to the repo on Mil and www.github.com.

### SUN  12-05-2019

-1- I renamed this file from 00_gitTTDtest.txt to 00_05_devTddMilPub

-2-	Eventually this directory will be deleted and the content goes in the 03_src or 04_dev directory.

### MON 28-12-2020

-1- For what ever reason I had this folder in the 05_dev. Since it is a learning project, I moved it to 03_src.

-2- The TDD django project is still at 1.11v for djnagon. I will try to go through it with the latest djangon version 3.11. Here I can see how to update a project.
https://docs.djangoproject.com/en/3.1/howto/upgrade-version/

-3-	I used django-admin _superlist . to start over again. 

-4- Downloaded geckodriver for win64 and placed it  env_NuDjBs/script folder. in same env i installed conda install selenium.

### MON 02-01-2021

-1-	Today I finished section 04. In VScode I start Django dev-server and can change html, thereafter test with test_functional, which is using selenium. I also learned that without running the Django dev-sever I can run test.py. The functional tests are interestig since I manupilate Firefox browser, which I might be able to use for job-workbench.

### MON 05-01-2021

-1- Here another explanatinon how I can use functiona and unit test with Django server

a) Django server running:
I can start Django server and do a manuel test, then perform the functional test and the unit test.
>ANKI: Django server , manual test (any browser), functional test (firefox) ,  unit test

b) Django server stopped:
When I stop the Djnago server I can **not** run the functional test, since it is like a user operating the webbrowser (in my set-up firefox). Since the Django server is not running the web-browser cannot connect to a web-site. Consequently, the test will fail with “Message: Reached error page: …. However the unit test (test.py) will still work.
>ANKI: Django server , unit test

### FRI 22-01-2021

-1- After almost two weeks I checked back and I almost remebered nothing. However, I found with >N where I left. I hope I can soon reserve time to pick up. 

### WED 08-09-2021

-1- Again I lost 8 month to finish this. However, I picked it up today as a code base for prototypefund.

-2- I renamed superlist eFolder to _superlist. --OKAY--

-3- I noticed that I have two .md files in this eFolder. gitTTDtest copy.md I will move to the devOps

-4-	The /note/ might be left over from another object and can be deleted.

>OK: Check if /note/ can be deleted. 

-5- I have currently no geckodrive installed.

>N: Install geckodrive and add it to the path. --OKAY--SAT 11-09-2021-- 

### SAT 11-09-2021

-1- Installed geckodriver in /Programm/Data and have it on system path.c

### SAT 13-09-2021

-1- I deleted the /note/

-2-	Decided to start all over again. Either I use the files I have already created or I will start a new Django project.

