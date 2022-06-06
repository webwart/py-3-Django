# Folder - DJ003_eCommerce-V2.md

Folder to learn about Django and follow the tutorial from Very Academy.

NOTE: I will try to use MS-onedrive to go throught the tutorial

## 01 - Database Design ( 02:10:32 )

vid = EbLEyM9SyZQ

list  = PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh

(https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh)

I finished this video. He explains in detail the design of the database.

## 02 - Inventory database development towards a test ( 5:10:33 )

27.10.2021 • Welcome to the Django E-commerce project version 2. In this Django tutorial we focus developing an inventory app. The purpose of the inventory app database is to maintain the data that is needed to support online retail sales and stock inventory management. In this tutorial we focus on deploying the database design developed in the first tutorial. 

For timeline see: 02-InventoryDbTestFirstApproach.docx

Downloaded the code from github. I got stuck with the password (see note.md)

Youtube ID Video = YVID = https://youtu.be/s3HuIRD5sUY

YVIDPL = https://youtu.be/s3HuIRD5sUY?list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh

YPL = https://www.youtube.com/playlist?list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh

>N: Find solution for password and watch the video.

### TUE 2022-05-17

-1- Installed .venv folder on onedrive.I added django to the .venv

>N: (10:07 Set-up the testing environment.)[https://youtu.be/s3HuIRD5sUY?list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&t=614]

pytest-django
pytest-factoryboy
pytest-selenium

Two approaches to create test data. a) Data fixtures b) factoryboy.

With Selenium I do functional testing. e.g. Test log-in .

Test folder structure. Pytest finds all files starting with **test**

Superuser admin *%admin+" PWD-E nervi45_Eval

IN \a1_DJP006_eCommerce-V2\ecommerce\dashboard\tests\test_selenium_dashboard.py the database is reset after each function. However, I can also set-up the database for the entire testing process. I will learn this in the next phase.

Create a db_admin_fixture.json file as fixture, which is basically data whic is uploaded to the django db. In this case I add a admin user to the table auth_user.I have now a test, where I open the Django log-in page and Selenium typs in the username and password. Django validates the typed in data and grants a log-in.

Xander uses [BLACK](https://black.readthedocs.io/en/stable/the_black_code_style/index.html) , which I installe with pip `install black`. BlACK is a formatter like autopep8 and yapf. Xander has a tutorial about this.

### Phase 2

Preview: BUild inventory app , Test first approach - creating models , Factory Boy.

>N: Find VScode Xander tutorial.

[Start with Phase 2](https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2&t=5036s)

Created 6 test for the category model , learned `pytest -m "not selenium"` to exclude a test. Factory boy to create data.

[Category model develpment](https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2&t=6828s)

1.  `pip install django-mptt` 
2.  rainer and nervi56-Eval are happy. The username and password created with Selenium do not work.
3.  python manage.py dumpdata inventory.category --indent 4 > new.json
4.  pytest -m "not selenium" -rP   # shows more output

A very **important** learning is that pytest, seleniu, fixtures do not alter the db permanently. 

I will use rainer as superuser (see credentials above)

Xander recommand to create the records manually since we use MPTT to create parent/child database. This is funny, since the databasse is then filled already with  records. I am aware tha the data loaded with thte fixturs.json file will be used only for pytest. 

[02:25:38 - Loading data fixtures - creating a custom command](https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2&t=8726s)

Created ecommerce/demo/ app, where I will/can keep all fixtures.Advantage: I can remove it from my application, once I ready to delploy. I can easily remove sqlite.db and migration file and run it again.

### Phase 3

[02:36:35 - Devloping the product table tests](https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2&t=9395s)

He used the method to get .csv data into a .json format suitable for upload to django, with the loaddata command.

[03:20:25 - Developing the product factory](https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2&t=12025s)

### MON 07-06-2022

-1- I moved the directory back to /03_src/py-3-Django/ on NapRai and SioRai. I also did set-up a git-hub repo py3dj

## 03 - Django E-commerce Product Filter Prototype ( 3:49:55 )

01.12.2021 • Welcome to part 3 of the Python Django E-commerce project version 2. In this Python Django tutorial we focus developing our understanding of Django queries and build a product filtering prototype. The purpose of the inventory app database is to maintain the data that is needed to support online retail sales and stock inventory management.

>N: Create MS-Word doc with timeline