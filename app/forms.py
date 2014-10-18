from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ProposeNewHangout(Form):
	hangout_id = IntegerField('Status')
	title = TextField('title', validators=[DataRequired()])
	hangout_date = DateField('hangout_date (mm/dd/yyyy)',validators = [DataRequired()], format='%m/%d/%Y')
	level = SelectField('level', validators = [DataRequired()], choices = [('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced')])
	language = SelectField('language', validators = [DataRequired()], choices = [('1', 'Javascript'), ('2', 'HTML/CSS'), ('3','Python'), (
		'4', 'Ruby-on-Rails'), ('5', 'Git'), ('6', 'Data Structures and Algorithms')])
	description = TextField('description', validators = [DataRequired()])
	status = IntegerField('Status')