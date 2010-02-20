====== ======================== ========================================
Method URL                      What it does
====== ======================== ========================================
GET    /modelname/              Lists model instances, using filters
                                like ?key=value1&key=value2

GET    /modelname/search        displays a search form

GET    /modelname/id            displays a readonly instance

GET    /modelname/edit/id       displays an edit form

POST   /modelname/update/id     updates an instance and redirects

POST   /modelname/upsert        Updates or inserts an instance and
                                redirects

GET    /modelname/upsert        Draws a form to do an upsert.

GET    /modelname/upsertform    Draws a form to do an upsert.

GET    /modelname/create        displays an insert form

GET    /modelname/insertform    displays an insert form

GET    /modelname/remove/id     displays a form that posts to
                                /model/delete/id

POST   /modelname/insert        inserts a new record and redirects

POST   /modelname/delete/id     deletes a record and redirects

GET    /modelname/bulk/edit     display a bulk edit ui

POST   /modelname/bulk/update   performs a bulk update and redirect

GET    /modelname/bulk/create   display a bulk insert form

POST   /modelname/bulk/insert   performs a bulk insert and redirect

POST   /modelname/bulk/delete   performs a bulk delete and redirect
====== ======================== ========================================
