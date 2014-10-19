from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class ProposeNewHangout(Form):
	hangout_id = IntegerField('Status')
	title = TextField('title', validators=[DataRequired()])
	hangout_date = DateTimeField('hangout_date (mm/dd/yyyy)',validators = [DataRequired()], format='%Y-%m-%d %H:%M:%S')
	level = SelectField('level', validators = [DataRequired()], choices = [('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
	language = SelectField('language', validators = [DataRequired()], choices = [('Javascript', 'Javascript'), ('HTML/CSS', 'HTML/CSS'), ('Python','Python'), (
		'Ruby-on-Rails', 'Ruby-on-Rails'), ('Git', 'Git'), ('Data Structures and Algorithms', 'Data Structures and Algorithms')])
	description = TextField('description', validators = [DataRequired()])
	status = IntegerField('Status')