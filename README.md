# flask_demo


- copy config 
```
cp config/settings.json.exmple  config/settings.json
```
- create database 
```
create database flask_demo charset=utf8mb4;
```

if you met "ImportError: No module named 'mysql'
" ,you can try "pip install mysql-connector" and restart you application

# migration
## https://sqlalchemy-migrate.readthedocs.io/en/latest/versioning.html
- create version control ```python manage.py version_control```
- show version with manage ```python manage.py db_version```
- create script ``python manage.py script "add_user_table"``
- upgrade ```python manage.py upgrade```
- downgrade ```python manage.py downgrade```

# docker
docker build  -t flak_demo . --no-cache
docker run -d — name flak_demo -p 5000:5000 flak_demo:latest

# continue to update….

