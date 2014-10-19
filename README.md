Hello! Anyone can contribute to this open-sourced project that helps people schedule hangouts more easily with each other. 

Here's how you can set up this app on your own machine:

1. Make sure python is installed on your machine.

2. $ sudo easy_install virtualenv
Install virtualenv. 

3. virtualenv —-no-site-packages codebuddies-flask
This step creates a new python virtual environment called "codebuddies-flask"

4. cd codebuddies-flask
Move into the codeboddies-flask folder you just created. 

5. $ source bin/activate
This is what you type to activate the virtualenv. Later on, when you want to get out of the virtualenv, type $ deactivate.

6. Fork the repo by clicking on the "fork" button on the upper right-hand corner. Next, run $git clone {{PATH}} on the repo you forked. 

Now you need to install a couple of dependencies within your app. Run the following: 

7. $ pip install flask==0.10.1

8. $ pip install wtforms

9. $ pip install flask_wtf

10. $ cd app

11. $ python run.py

Remember to run $ git pull frequently. Please submit a pull request if you have any changes. 