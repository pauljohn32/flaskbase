
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
pip3 install flask-wtf
pip3 install email-validator
pip3 install import flask_mail
pip3 install PyJWT


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


##
# (venv) pauljohn@dellap-20:~/GIT/flask/pj_flask/base$ flask db init
# OS environment development
# OS environment development: development
# fname app.db
# basedir /home/pauljohn/GIT/flask/pj_flask/base
#   Creating directory /home/pauljohn/GIT/flask/pj_flask/base/migrations ...  done
#   Creating directory /home/pauljohn/GIT/flask/pj_flask/base/migrations/versions
#   ...  done
#   Generating /home/pauljohn/GIT/flask/pj_flask/base/migrations/script.py.mako ...  done
#   Generating /home/pauljohn/GIT/flask/pj_flask/base/migrations/alembic.ini ...  done
#   Generating /home/pauljohn/GIT/flask/pj_flask/base/migrations/README ...  done
#   Generating /home/pauljohn/GIT/flask/pj_flask/base/migrations/env.py ...  done
#   Please edit configuration/connection/logging settings in
#   '/home/pauljohn/GIT/flask/pj_flask/base/migrations/alembic.ini' before
#   proceeding.
# (venv) pauljohn@dellap-20:~/GIT/flask/pj_flask/base$ flask db migrate -m "users table"
# OS environment development
# OS environment development: development
# fname app.db
# basedir /home/pauljohn/GIT/flask/pj_flask/base
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.autogenerate.compare] Detected added table 'user'
# INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
# INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
#   Generating /home/pauljohn/GIT/flask/pj_flask/base/migrations/versions/d3c75d580f
#   bd_users_table.py ...  done
# (venv) pauljohn@dellap-20:~/GIT/flask/pj_flask/base$ flask db upgrade
# OS environment development
# OS environment development: development
# fname app.db
# basedir /home/pauljohn/GIT/flask/pj_flask/base
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.runtime.migration] Running upgrade  -> d3c75d580fbd, users table


Test that manually. This DID work, but after revision of the app, it
does not anymore.  Need to find out why

(venv)$ python3
from app import db
from app.models import User
u = User(username='pauljohn32', email='pauljohn32@freefaculty.org', super=True)
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



With bootstrap

pip3 install import flask_bootstrap



Testing outgoing mail, flask shell


export MAIL_SERVER=smtp.dreamhost.com
export MAIL_USE_TLS=0
export MAIL_PORT=587
export MAIL_USERNAME=pauljohn32@freefaculty.org
export MAIL_PASSWORD='xxxx!@'



from flask_mail import Message
from app import mail
msg = Message('test subject', sender="pauljohn32@freefaculty.org", recipients=['pauljohn@ku.edu'])
msg.body = "asdf asdfka sdfjlas jaksdlf jasdklf"
msg.html = "<h1>HTML inside here</h1>"
mail.send(msg)
