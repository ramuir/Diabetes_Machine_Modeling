from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DiabetesForm(FlaskForm):
    A1c = StringField('A1c', validators = [DataRequired()])
    Glucose = StringField('Glucose', validators = [DataRequired()])
    BPSystolic = StringField('bp.2s', validators = [DataRequired()])
    Height = StringField('Height', validators = [DataRequired()])
    Age = StringField('Age', validators = [DataRequired()])
    WHratio = StringField('waist/hip ratio', validators = [DataRequired()])
    # WHratio = StringField('waist/hip ratio', validators = [DataRequired()])


    submit = SubmitField('Get Checked')






 


