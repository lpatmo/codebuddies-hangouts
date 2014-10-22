We (all volunteers) are building a better Google Hangout scheduler tool for people who to find study partners and talk code/learn web development together. This application is built in python/flask. Anyone can contribute to this open-sourced project.

##Background
[http://www.codebuddies.org](http://www.codebuddies.org)

##Installation 

Here's how you can set up this app on your own machine:

####Make sure python is installed on your machine.

####Install virtualenv. 
```
$ sudo easy_install virtualenv
```

####This step creates a new python virtual environment called "codebuddies-flask."
```
virtualenv —-no-site-packages codebuddies-flask
```

####Move into the codeboddies-flask folder you just created. 
```
$ cd codebuddies-flask
```

####This is what you type to activate the virtualenv. Later on, when you want to get out of the virtualenv, type $ deactivate.
```
$ source bin/activate
```

####Fork the repo by clicking on the "fork" button on the upper right-hand corner. Next, run $git clone {{PATH}}.git on the repo you forked so that you can push to your own copy of the repo on your own github profile.

Now you need to install a couple of dependencies within your app. After you $ cd into the 'app' directory, run the following: 

```
$ pip install -r requirements.txt
```

####To run the app, type the following and then copy/paste the resulting URL into your browser.
```
$ python run.py 
```

Remember to run ```$ git pull``` frequently. Please submit a pull request if you'd like to submit any changes.
