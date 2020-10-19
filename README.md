# What is this?

This is a bare-bones base app that includes all features than any
professionally serious Flask app should have. It has authentication,
password reset, out-going email messages, error logging. The version
of the app in `1-base` has all of the features we might need, except
possibly for multi-factor authentication. My colleague showed me how
to implement MFA as well and I might add it.

# Why do this?

Simply put: |
   I want to out out all of the crap from standard tutorials about creating a blog!

I want the boilerplate that all Flask apps need, and an empty spot where
the application should go.

# How did I end up here?

The two best guides for serious Flask app work are

1. The Mega Flask Tutorial, by Miguel Grinberg

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

2. on Hackers and Slackers, by Todd Birchard

https://hackersandslackers.com/your-first-flask-application

The first of them is more comprehensive, while I gained many valueable
tidbits, filling in little gaps in the latter.  If you ever want to incorporate
javascript into your Flask app, the second one makes more sense.  The 
Mega Flask tutorial is very good, but my critique is that it builds up
from a basic level and so, by step 10 or so, you have to tear apart
what you did at the beginning and replace it with the best practice code.
Birchard's guide is quicker to step to the best practice, but that
may make it more difficult for a beginner.


These other tutorials are just OK. 

https://realpython.com/flask-connexion-rest-api

I've found a ton of them,
but many simply implement the "bad" approach featured in the 
first segments of the Mega Flask tutorial, so they do more harm than good.


I worked through many Flask app tutorials. Much energy was wasted on details
about creating a blog website or doing something else that does not
concern me.

# What to do

1. The basic "Hello World" Flask app is offered in folder 0-hello.

2. The base app, the one I truly use to start a Flask project, is in
1-base.

3. I plan to write more applications based on 1-base, check back.
Priority 1 is embedding a Python Dash/Plotly app.

https://hackersandslackers.com/plotly-dash-with-flask
