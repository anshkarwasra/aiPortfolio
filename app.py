from flask import Flask, request, redirect, render_template

from datetime import datetime
from joblib import load
from werkzeug.utils import secure_filename
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle
app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "C:\\Users\\anshk\\Downloads\\Programming\\hackathon project\\HPCopyZip\\HPCopy\\model_images"

import google.generativeai as genai
import os

# AIzaSyBkpmK74q4CeYIlUmSX7TXEd76S86ISExA
# set API_KEY=<AIzaSyBkpmK74q4CeYIlUmSX7TXEd76S86ISExA>

genai.configure(api_key='AIzaSyBkpmK74q4CeYIlUmSX7TXEd76S86ISExA')

model = genai.GenerativeModel('gemini-1.5-flash')

regressor = load("model.joblib")

def preProcess(row):
    with open('le_brand.pickle','rb') as f:
        le_brand = pickle.load(f)
    with open('le_model.pickle','rb') as f:
        le_model = pickle.load(f)
    with open('scaler.pickle','rb') as f:
        scaler = pickle.load(f)
    row["Car Brand"] = le_brand.transform([row["Car Brand"]])
    row["Car Model"] = le_model.transform([row["Car Model"]])
    row = scaler.transform([row])
    print(row)
    return row

@app.route('/textgen', methods = ['GET', 'POST'])
def textgen():
    response = "Hi, how can I help you today?"
    user_input = "Hi!"
    if request.method == 'POST':
        user_input = request.form.get("textgen") 
        response = (model.generate_content(user_input)).text 
    return render_template('textgen.html', port=6000, response=response, user_input = user_input)


@app.route('/image', methods = ["GET", "POST"]) 
def uploader():
    # Upload the file and print a confirmation.

    # Prompt the model with text and the previously uploaded image.
    response = "No response yet."
    if request.method == "POST":
        
        f = request.files['file1']
        f.save(os.path.join(app.config['UPLOADER_FOLDER'], secure_filename(f.filename)))
        query = request.form.get("user_query")
        sample_file = genai.upload_file(path=f"C:\\Users\\anshk\\Downloads\\Programming\\hackathon project\\HPCopyZip\\HPCopy\\model_images\\{f.filename}",
                            display_name="an image")
        
        try:
            response = model.generate_content(sample_file, query)
            print(response.text)
            return render_template('image.html', response = response.text)
        except Exception as e:
            return render_template('image.html',response="opps something went wrong")
    return render_template('image.html',response=response)

@app.route('/')
def route():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')


@app.route('/carprice',methods=['GET','POST'])
def caarprice():
    response = "nothing to say yet."
    if request.method == "POST":
        carBrand=  request.form.get("car_brand")
        carModel = request.form.get("car_model")
        df = pd.read_csv("data.csv")
        df = df.drop("Unnamed: 0",axis=1)
        try:
            row = df[df['Car Brand'] == carBrand]
            row = row[row['Car Model']== carModel]
            response = round(regressor.predict(preProcess(row.iloc[0]))[0] /10)
        except Exception as e:
            response = "sorry we don't have data for that car"
            print(e)

    return render_template("model.html",response=response)

if __name__ == "__main__":
    app.run(debug=True)