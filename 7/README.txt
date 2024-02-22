Очень полезно:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
https://www.webforefront.com/django/setupinitialdatadjangomodels.html

// write each time after changing models
// first command tracks all models' changes, the second one applies changes to database
manage.py makemigrations
manage.py migrate

// сделать пустую миграцию: (затем добавил в operations hard-coded SQL scripts)
manage.py makemigrations --empty app

2. settings.py, urls.py, models.py, migrations 0003
3. admin.py
Списки отображения:
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F_%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%B2

4. app folder: urls.py, views.py; index.html
5. app folder: forms.py, views.py, urls.py; patient_form.html
6. views.py, urls.py, patient_detail.html, person_detail.html
7. init.sql, clear.sql, migrations 0001 0003, views.py, urls.py, patient_confirm_delete.html

!!! Как пересоздать бд !!!
(полезно, если накосячишь: чисть таблицу django_migrations в SQLite Browser)
Отменяем последнюю миграцию и применяем ее снова
https://howchoo.com/django/how-to-rerun-a-django-migration/

Фейковый откат к миграции ДО той, что нужно выполнить повторно:
manage.py migrate --fake app 0002
Выполнение целевой миграции:
manage.py migrate app 0003
Готово (в данном случае не нужно делать закомменченное ниже)
// Откат обратно к последней миграции:
// manage.py migrate --fake app 0003
