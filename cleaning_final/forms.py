from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class DiabetesForm(FlaskForm):
    A1c = FloatField('A1c', validators = [DataRequired(float())])
    Glucose = FloatField('Glucose', validators = [DataRequired(float())])
    Systolic = FloatField('bp.2s', validators = [DataRequired(float())])
    Height = FloatField('Height', validators = [DataRequired(float())])
    Age = FloatField('Age', validators = [DataRequired(float())])
    WHratio = FloatField('bp.2s', validators = [DataRequired(float())])
    


    submit = SubmitField('Get Checked')






 


