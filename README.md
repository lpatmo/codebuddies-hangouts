Hello! We're building a better Google Hangout scheduler tool for people learning web development. We're using python/flask. Anyone can contribute to this open-sourced project, which is entirely run by volunteers.  

Here's how you can set up this app on your own machine:

###Make sure python is installed on your machine.

###Install virtualenv. 
```
$ sudo easy_install virtualenv
```

###This step creates a new python virtual environment called "codebuddies-flask."
```
virtualenv —-no-site-packages codebuddies-flask
```

###Move into the codeboddies-flask folder you just created. 
```
$ cd codebuddies-flask
```

###This is what you type to activate the virtualenv. Later on, when you want to get out of the virtualenv, type $ deactivate.
```
$ source bin/activate
```

###Fork the repo by clicking on the "fork" button on the upper right-hand corner. Next, run $git clone {{PATH}}.git on the repo you forked so that you can push to your own copy of the repo on your own github profile.

Now you need to install a couple of dependencies within your app. After you $ cd into the 'app' directory, run the following: 

```
$ pip install -r requirements.txt
```

Remember to run ```$ git pull``` frequently. Please submit a pull request if you'd like to submit any changes.
