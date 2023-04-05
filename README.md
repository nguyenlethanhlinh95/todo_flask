## About

This is project use to study FrameWork Django.

## How to Run

### Install Python on Wondow 10

https://www.python.org/downloads/


### Install virtual venv on Window 10

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

### Initial venv on local

```
py -m venv venv
```

### Active virtual environment

Please use powershell if you use venv on window :)

```
.\venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt

```

### How to start project development

```
flask --app .\app.py --debug run

```


### Migration

If you not have a directory migrations in project, you can run command first here

```
flask db init

```

Run this command to apply file migrations

```
flask db migrate -m "add created_at and updated_at columns"
```


apply version migrate script to DB

```

flask db upgrade

```


rollback migration

```

flask db downgrade

```



References: https://flask-migrate.readthedocs.io/en/latest/