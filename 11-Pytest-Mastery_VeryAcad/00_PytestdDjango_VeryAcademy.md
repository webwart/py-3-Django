# 00_PytestDjango_VeryAcademy.md - Learn how to do testing with pytest for Django

Here I do learn how to test Django related topics. I follow a tutorial from the youtube channel "Very Academy". After I completed Alan Simpson Django CRUD tutorial I would like  to become better in testing and debugging with VScode.

## Goals

1. Finish the tutorial and learn how to do testing with pytest for Django 
2. Learn what to with testing during Django deployment to uberspace, digital ocean or heroku
3. Learn how apply to for prototype.de, finacial modelling, hybiom, biologika
4. Decide if I want also do TestDrivenDjango_HarryPercival

## Developemnt und Dsign decision

- I have a git ripo for /PytestDjango_VeryAcademy- test for sqlite, mysql (uberspace) , digital ocean (postgree)
- target Win10 , uberspace , digital ocean.
- Pytest 6.2.3, Win10, Django 3.2, Python 3.9
- I do not use the django plug-in for VScode since it prevents Emmet to work, however, this can be fixed.


## Situation, Reasoning , and nexts tings to do ---

1. Start: 02-11-2021 new , Precurser: dd-mm-yyyy name 
2. What are the resources (time, finance, energy) ? 1-2 h/day, no finance, middle)
3. What has been done ? 
-- Finished tutorial 2
4. What did not work ? 

5. What are Concepts, Diagrams, Reasoning, Outlook.




## Prerequits for SPs ---

- What intepreter / virtuell machine / packages / modules / files / folders
-- open VScode from 04_src/Python-Django/ Select .env . OPEN Terminal New and select powershell, which will activate the .env.
- Do I have git ? Which server repository ?
>N: 
- Where is this code synced to ? How ?

- Does is run on Win10 , ubespace , android ?
-- Runs on Win10 sofar

- What usr pwd em ad do I use
Created superuser amin<<<<>>>a@gum.co<>>>>ner7it/DE_DjAd


 

>SP: Document structure and procedure

``` text
Typ
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt

USE----name of structure to use
CREAT--folder, file, object etc.  
COPY---"01_ProjectTemplate.md" into new \folder\ and change
     --the of the file to 00_<Name of folder>.md
VERB---documention of set-up, SP and progress (Journal section)  
```

>SP: Get started

``` text
OPEN      >Ref: 8
FIND      last video tutorial I was working on (see Journal)
ACTIVATE  .env by opening a new terminal.
```

## References ---

1. Guideline: Set-up a development environment, which works within the folder where it is living. Use always relative path.
1. [VScode Windows Key Bindings](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
2. [Markdown Guide](https://www.markdownguide.org/) -> Markdown Syntax and related Software.
3. [GIThub flavored Markdown GFM](https://github.github.com/gfm/#what-is-github-flavored-markdown-) -> I use GSM specification, which is very detailed.  
4. Guideline .md: To create a new line, I use two spaces at the end of the line.
5. [Djagno Tutorial for Beginners 2021, Programming with Mosh, youtube](https://www.youtube.com/watch?v=rHux0gMZ3Eg) This course is the first houer of a longer course. I saw the entire youtube video. 
6. [Python Django Web Framework - Full Course for Beginners, freeCodeCamp.org, youtube](https://www.youtube.com/watch?v=F5mRW0jo-U4) This course is based on a course from [Coding for Entrepreneurs](https://www.codingforentrepreneurs.com/). The course dives into different concepts of python. Has a nice Course Content. The code can be found here: https://github.com/codingforentrepreneurs/Try-Django-3.2. He uses MAC, django 2.0.7, python 3.6. Editor: Sublime Text.
>N: True ? Win10 scritp/activate , Linux bin/activate  -> 0:22.27 6-Settings 
7. [Djgaon 1.4 Workshop, Deutsch ](http://www.django-workshop.de/index.html)
8. [Playlist - Pytest Mastery with Django](https://www.youtube.com/watch?v=LYX6nlECcro&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY)


## Journal (today top)

###  02-11-2021
-1- Started the tutorial / playlist.

-2- Tutorial has a play list on youtube. I assume that  the order is top to down, since no numbers are given.

01-Gentle Introduction, Setup and Start Testin (19:13)
02-Indroducing Fixtures and Fixture Factory (32:49)


#### 02-Indroducing Fixtures and Fixture Factory (32:49)


1. Start a new Django Project
2. Test folder structures
3. Installation Pytest-django   6:50 A wrapper for pytest.
4. Pytest Test Discovery
5. Creating our first tests
6. Running test with PyTest
6.1. Understanging the Testing Output
6.2 Report Options
6.3 Specifying test to run
6.4 Using Pytest Mark - 16:50 a way to add meta data to a test.
6.5 Adding meta data to tests.  skip and xfail 


#### 02-Indroducing Fixtures and Fixture Factory (32:49)

1. Arrange, Act delivers a reponse, Assert tests response against an expected outcome.
2. Fixturs are functions used in the arrange phase. Fixtures are used to feed data to the tests such as database connections, URLs to test and input data. Fixtures  have a scope see test.ex1.py. `@pytest.fixture(scope="session")` means the fixture is run once and the data is used for all test in the sesion. Without this scope, the fixture is run for each test again.
3. 8:21  Fixtures can be at the begginin or end of a test
4. Moving fixtures to conftext.py
5. 20:55 Complicated examples
6. 23:00 Nice showing of using SQL lite
7. 25:00 inner functions / nested functions

### THU 04-11-21

#### 03 Fixture Replacement: Factory Boy & Faker

Pytest is a popular python test automation framework. Here we look at replacing Pytest fixtures with Factory Boy in a Python Django project. Factory Boy as a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex objects. In this tutorial we intergrade Factory boy into our small app and take a look at some of the more common features.

Arrange - connect to a database
Act - save dat to a database
Assert - test

4:24 replaces  previous code in conftest.py with factory boy.
4:45 install pytest-factory boy  and faker  [Blog post from Rocio Aramberri](https://schegel.net/posts/simplied-django-tests-with-pytest-and-pytest-factoryboy/) and [Read the docs: factoryboy](https://factoryboy.readthedocs.io/en/stable/)
8:07 Start with refactoring
12:00 he has a video about faker at VeryAcademy
16:00 build() a user (not added to the database) . Now we create() a user, which is added to the database
19:10 building a new model 


>N: #### 04Towards Parametrizing Fixtures and Test Functions


