# Django im Unternehmen - iX article von Christian Leubner

Der Artikel zeigt with man Django in einer Unterhemensumgebung einsetzten kann. 
Es gibt ein Beispiel, in dem verschiedene Apps genutz werden.
Dies sollte eine gute Übung sein um die Integration von veschiedene Module in Django zu lernen.

>Ref: 
Article is in \PUB-Biblio\CT-Topics\Python\ix20-12-120_DjangoUnternehmen_iX.docx and ./doc_article/
Orginal code ist in \03_src\LIBS\Python\ix20-12-120_DjangoUnternehmen
Working code ist in \03_src\python\_UnternehmensDjango

## Settings

1. Start application with WinTerminal and script
2. Login with root root


## Journal  (today is top)

### TUE 2022-02-22

-1- with powershell script I  open this application on port:8001

### MON  13-09-2021

-1- I used conda/env_Django to run the applicatiion. MonduleNotFoundError: No module named 'crispy_forms'.
    crispy_forms is a module, which is probably installed with the requirements from file ./requirements/base.txt.

>N: Install requirements and make sure to get grispy-forms.

-2- I learn from this code here how to manage configuration/requirements for deployement and development. 