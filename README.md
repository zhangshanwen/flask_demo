# flask_demo

flask demo 

export FLASK_DEMO_SETTINGS=./config/settings.cfg

if you watch "ImportError: No module named 'mysql'
" ,you can "pip install mysql-connector" and restart you application

# migration
## https://sqlalchemy-migrate.readthedocs.io/en/latest/versioning.html
- create migrations  ```migrate create migrations "flask demo" ``` 
- create version_control```python migrations/manage.py version_control mysql+mysqlconnector://root:123456@127.0.0.1:3306/test migrations ```
- show version ```python migrations/manage.py db_version mysql+mysqlconnector://root:123456@127.0.0.1:3306/test migrations```
- create manage```migrate manage manage.py --repository=migrations --url=mysql+mysqlconnector://root:123456@127.0.0.1:3306/test```
- show version with manage ```python manage.py db_version```
- create script ``python manage.py script "add_user_table"``
- upgrade ```python manage.py upgrade```
- downgrade ```python manage.py downgrade```
