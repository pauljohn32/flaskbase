
virtualenv -p /usr/bin/python3.8 venv

source venv/bin/activate

pip3 install flask
pip3 install python-dotenv


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
