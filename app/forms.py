from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ProposeNewHangout(Form):
	hangout_id = IntegerField('Status')
	title = TextField('title', validators=[DataRequired()])
	hangout_date = DateField('hangout_date (mm/dd/yyyy)',validators = [DataRequired()], format='%m/%d/%Y')
	level = SelectField('level', validators = [DataRequired()], choices = [('1', '1'), ('2', '2'), ('3', '3')])
	language = SelectField('language', validators = [DataRequired()], choices = [('1', '1'), ('2', '2'), ('3','3'), (
		'4', '4'), ('5', '5'), ('6', '6')])
	description = TextField('description', validators = [DataRequired()])
	status = IntegerField('Status')