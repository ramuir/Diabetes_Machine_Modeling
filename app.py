from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from forms import DiabetesForm
from flask import flash, redirect
from flask_wtf import FlaskForm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

random_forest = joblib.load("./Models/RF_Model.sav")
decision_tree = joblib.load("./Models/Decision_Tree_Model.sav")
# clean_df = pd.read_csv("./Data_csv/cleaned_data.csv")
# clean_df = pd.get_dummies(clean_df)
# X = clean_df[[  'A1c','BMI','Age','HDL Chol','Weight', 'Diastolic BP', 'waist/hip ratio']]
# y = clean_df['Diabetes_No diabetes'].values.reshape(-1, 1)
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42,stratify=y)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send(output=sum):
    
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        num4 = request.form['num4']
        num5 = request.form['num5']
        num6 = request.form['num6']
        
        operation = request.form['operation']

        if operation == 'randomforest':
            arr_num = np.array([num1,num2,num3,num4,num5,num6])
    
            output = random_forest.predict(arr_num.reshape(1,-1))

            if output == [0]:
                output = 'High Risk'
            else:
                output = 'Low Risk'

            return render_template('index.html', sum=output)



        elif operation == 'decisiontree':
            arr_num = np.array([num1,num2,num3,num4,num5,num6])
            output = random_forest.predict(arr_num.reshape(1,-1))
            
            if output == [0]:
                output = 'High Risk'
            else:
                output = 'Low Risk'
            
            return render_template('index.html', sum=output)

        else: render_template('index.html')


        


if __name__ == '__main__':
    app.run(debug=True, port = 5044)