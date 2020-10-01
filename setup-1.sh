
virtualenv -p /usr/bin/python3.8 venv

source venv/bin/activate

Any minimally reasonable app will require these, so
install them now

pip3 install flask
pip3 install python-dotenv
pip3 install flask-sqlalchemy
pip3 install flask-migrate
pip3 install flask-shell
pip3 install flask-login

# No need to do this because I have dotenv file
# export FLASK_APP=hello_world.py

flask run


Hello World

├── app
│   ├── __init__.py
│   └── routes.py
├── .flaskenv
└── hello_world.py


Base (base folder)


Take files as they are, then initialize database with migration


(venv)$ flask db init
(venv)$ flask db migrate -m "users table"
(venv)$ flask db upgrade


Test that manually

(venv)$ python3
from app import db
from app.models import User
u = User(username='paulj2', email='pj@freefaculty.org')
db.session.add(u)
db.session.commit()
users = User.query.all()
[print(u.id, u.username) for u in users]

Simpler convenience methd using flask-shell package

(venv)$ flask shell
>>> u = User(username='paulj', email='pej@freefaculty.org')
>>> db.session.add(u)
>>> db.session.commit()
>>> users = User.query.all()
>>> [print(u.id, u.username) for u in users]
