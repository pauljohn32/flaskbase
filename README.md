# What is this?

This is a bare-bones base app that includes all features than any
professionally serious Flask app should have. The version of the app
in `1-base` has all of the features we might need to get started. It
has the "app factory" setup, blueprints, authentication, password
reset, out-going email messages, error logging.  I use flask env
to set environment for configurations.

All of my folders provide fully working applications. Because
I use blueprints to separate the work, it should be possible for
other people to cut/paste sections together. 

The only thing `1-base` it does not have is multi-factor authentication. My
colleague showed me how to implement MFA as well and I might add it. I
might not because the only type of phone app I know to configure is
Google's Authenticator.  In my work, I may be required to use
the RSA_token generator.

# Why do this?

I needed the basic app components without any distractions.  The
Flask tutorials typically invest a lot of effort in "how to write
a blog" and I just don't need that.

I want the boilerplate that all Flask apps need, and an empty spot where
the application should go.

# How did I end up here?

The two best guides for serious Flask app work are

1. The Mega Flask Tutorial, by Miguel Grinberg

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

2. Creating Your First Flask Application (on Hackers and Slackers), by Todd Birchard

https://hackersandslackers.com/your-first-flask-application

The first of them is more comprehensive, while in the latter I find
much insightful commentary and good advice about avoiding common
errors.  The Mega Flask tutorial is very good, but my critique is that
it builds up from a basic level and so, by step 10 or so, you have to
tear apart what you did at the beginning and replace it with the best
practice code.  Birchard's guide is quicker to move to the best
practice. It has less wasted effort.  However, it may make it more
difficult for a beginner. If you ever want to incorporate javascript
into your Flask app, the second one makes more sense.


These other tutorials are just OK. 

https://realpython.com/flask-connexion-rest-api

I've found a ton of tutorials, but many simply implement the "bad"
approach featured in the first segments of the Mega Flask tutorial, so
they do more harm than good. 


# What to do

If you found this, test your setup with the first app.

1. The basic "Hello World" Flask app is offered in folder 0-hello_world.

Then run the second one.

2. The base app, the one I truly use to start a Flask project, is in
1-base.

3. I plan to write more applications based on 1-base, check back.
Priority 1 is embedding a Python Dash/Plotly app.

https://hackersandslackers.com/plotly-dash-with-flask
