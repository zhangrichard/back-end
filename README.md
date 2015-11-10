# back-end
The back-end for the HexHack touch table project.

### 1. pull the repo

### 2. add settings.py
### 3. Set up your local database
``` 
mysql -u root -p
```
```
CREATE DATABASE hexhack;
```
make sure it fits the settings.py 


### 4. Migrate the database
```
python manage.py migrate
```
### 5. Launch the server
```
python manage.py runserver
```

### work flow
