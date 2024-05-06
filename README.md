# Backend

### Install
Clone the repo.
</br>
Then install dependencies:
```
pip install -r requirements.txt
```

### Configure
Firstly, copy `config/.env.default` file to `config/.env`,  then fill entries.
</br></br>
Compile __*.po__ files:
```
django-admin compilemessages
```

### Run
If it is going to run on production, do not forget to set `DEBUG=False` in `config/.env`.
```
python manage.py runserver 0.0.0.0:<PORT>
``` 
> change the \<PORT\> for actual port number. 8080 recommended.

### Usage
There will be instructions soon...

### Development
Make Messages
```
django-admin makemessages -i env -a
```
