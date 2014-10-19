Hello! Anyone can contribute to this open-sourced project that connects people studying web development via ad-hoc google hangouts.

Here's how you can set up this app on your own machine:

1. Make sure python is installed on your machine.

2. Install virtualenv. 

```
$ sudo easy_install virtualenv
```

3. This step creates a new python virtual environment called "codebuddies-flask."

```
virtualenv —-no-site-packages codebuddies-flask
```

4. Move into the codeboddies-flask folder you just created. 

```
$ cd codebuddies-flask
```

5. This is what you type to activate the virtualenv. Later on, when you want to get out of the virtualenv, type $ deactivate.

```
$ source bin/activate
```

6. Fork the repo by clicking on the "fork" button on the upper right-hand corner. Next, run $git clone {{PATH}}.git on the repo you forked so that you can push to your own copy of the repo on your own github profile.

Now you need to install a couple of dependencies within your app. Run the following: 

```
$ pip install flask==0.10.1

$ pip install wtforms

$ pip install flask_wtf

$ cd app

$ python run.py
```

Remember to run ```$ git pull``` frequently. Please submit a pull request if you'd like to submit any changes.

Join the community at codebuddies.org if you run into any trouble. The project is all organized by volunteers. :)