# Folder - DJ003-Core-ORM-Mastery.md -  

I want to use a database schema, which I can use for the revenu fix, fee, invest project. The core will by a company database. I will learn from Very Academy ORM Tutorial.

## Goals

1. What do I want to learn ? ORM from Django
2. Where is it used in production ? All Django project
3. Timeline / Deadline ? until the end of 2021
4. Deliverable ? Revenue Fix database

## Situation, Reasoning , and nexts tings to do

1. Start: 15-11-2021 
2. What has been done ? Added ORM Tutorial to youtube account as playlist.Created this folder
3. What did not work ? --
4. What are the resources (time, finance, energy) ?  2 h/ week
5. What are Concepts, Diagrams, Reasoning, Outlook ? --

>N: Download code, Watch all videos.

## Prerequits for SPs

- What intepreter / virtuell machine / packages / modules / files / folders ? /python-django/.env
- Do I have git ? Which server repository ? NO
- Where is this code synced to ? How ? --
- Does is run on Win10 , ubespace , android ? Win10

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
5. [Django ORM Mastery Series , DJ003-Core-ORM-Mastery](https://www.youtube.com/watch?v=iQF6pln3Gog&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml). Playlist in my youtube mediathek.
6. Overview of VeryAcademy learning path \PUB\03_src\python-Django\01_LearningPath.md

---

## Journal / Outline

### PL01 - Djagno ORM - What is Django ORM ?

[Link](https://www.youtube.com/watch?v=iQF6pln3Gog&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=1)

PL02 - Django ORM - Django OR query

PL03 - Django ORM - How to perform an AND query on a database

PL04 - Django ORM - How to perform aa UNION query on a database

PL05 - Django ORM - How to perform an NOT query on a database

PL06 - Django ORM - Select and Output individual fields

PL07 - Django ORM - Performing raw SQL queries

PL08 - Django ORM - Django bypass ORM! - Performing raw SQL queries without the ORM (:11:56)

The Django ORM series covers a range of common functions that you will perform on a database with Django. In this tutorial we introduce the idea of running your own SQL queries, thus bypassing the Django ORM features. This is an introductory guide to help you get start with the general concepts and structure of building SQL queries outside of the Django ORM.

https://www.youtube.com/watch?v=_TtBxvYwoHY&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=8

### PL09 - Django ORM - Django Model Inheritance Options Introduction - ORM Part-9 (:15:39)

The Django ORM series covers a range of common functions that you will perform on a database with Django. In this tutorial we introduce the idea of model inheritance using 3 options that Django provides, Abstract models
Multi-table model inheritance and Proxy models. I give you an overview of each and provide a small example of how to use each type of inheritance option.

https://www.youtube.com/watch?v=4Xag2FzmN60&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=9

### PL10 - Django ORM - Towards SQL Optimization - Django Debug Toobar Package

Thinking more serious about Python Django means understanding a little more about the performance of our django application. As you might imagine there are many tools and methods to measure performance. Moving into that direction the django-debug-toolbar give us provide some useful information to help us start thinking about database/SQL optimizations.

Django as a powerful framework makes it easy to interact with database - allows you to directly map your object-oriented models to database table structures and in doing so also builds the data and table relationships.

This level of abstraction the ORM provides (although it does a great job) it can cloud our understanding the performance of our application. And as better performance can convert to lower running costs – its an important aspect of our development we need to know more about.  

Starting your journey to database optimization, we need to understand what is happening behind the scenes or more importantly monitor SQL performance. If you have seen the other tutorials in this series we already know that we can collect information about SQL queries that be being executed. In this tutorial, although there are many various ways to log SQL queries, here we take a look at the package django-debug-toolbar – which as you will see provides more than just SQL information. Overall, it provides us some great insights into our application.

https://www.youtube.com/watch?v=riBTlU6iMc4&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=10

>RKW: Could install toolbar with `$ python -m pip install django-debug-toolbar`  
>REF: [Docs for Dj Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)  
>N: Check settings.py file

### PL11 - Django ORM - Python Django Inheritance Optimisation Exercise

In this Python Django tutorial we work through a set of examples to develop a better understanding of Django model inheritance. We try and answer the question of how to design a product table where we may need to have many types of product thus needing to create multiple tables.

00.00 Scenario and problem statement
02:07 Introduction
02:41 Solution 1 - Concrete Classes
06:01 Solution 2 - Multi-table Inheritance
23:14 Solution 3 - Abstract Models
42:50 Solution 4 - django-polymorphic ( needs installation with pip)

[Link](https://www.youtube.com/watch?v=Y4ahqzSs7nIlist=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=11)

### PL12 -  Django ORM - Multiple Database Setup Ex1

Python Django multiple database setup example with 3 databases and 2 applications. In this tutorial we look at Django’s support for interacting with multiple databases. This is a beginners introductory example helping us get familiar with setting up multiple databases with Django.

[Link](https://www.youtube.com/watch?v=g-FCzzzjBWo&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=12)

### PL13 - Django ORM - Transaction Atomicity

Django’s default behaviour is to run in autocommit mode, By default each query is immediately committed to the database, each SQL query gets wrapped in its own transaction and a transaction is automatically committed or rolled back.

A transaction is a sequence of one or more SQL operations that are treated as a unit. All operations should be executed successfully in order to call the transaction successful. Transactions ideally have four properties, commonly known as ACID. This is a standard set of properties aimed to guarantee database transactions are processed reliably which is especially concerned with how a database recovers from any failure.

Atomicity is the defining property of database transactions. Atomic require us to create a block of code within which the atomicity on the database is guaranteed.

[Link](https://www.youtube.com/watch?v=BchP5Mn1IYg&list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml&index=13)
>N: :12:

PL14 -

PL15 -

PL16 -

PL17 -

PL18 -

PL19 -

PL20 -