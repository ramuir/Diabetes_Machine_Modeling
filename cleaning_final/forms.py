from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class DiabetesForm(FlaskForm):
    Height = StringField('Height', validators = [DataRequired()])
    BMI = StringField('BMI', validators = [DataRequired()])
    A1c = FloatField('A1c', validators = [DataRequired(float())])
    HDL= StringField('HDL', validators = [DataRequired()])
    Glucose = StringField('Glucose', validators = [DataRequired()])
    Cholesterol = FloatField('Cholesterol', validators = [DataRequired(float())])


    submit = SubmitField('Get Checked')






 


