from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('point_predict.pickle','rb')) # Set the trained model

# Set number to every genre
dic = {'만화':2,
        '소설/시/희곡':3,
        '경제경영':4,
        '어린이':5,
        '건강/취미/레저':6,
        '에세이':7,
        '과학':8,
        '유아':9,
        '예술/대중문화':10,
        '인문학':11,
        '수험서/자격증':12,
        '좋은부모':13,
        '자기계발':14,
        '외국어':15,
        '사회과학':16,
        '청소년':17,
        '가정/요리/뷰티':18,
        '컴퓨터/모바일':19}

# First page
@app.route('/')
def home():
    return render_template('home.html')

# Redirect to the predeiction page when information is entered and 'submit' is clicked
@app.route('/predict', methods=['GET','POST'])
def prediction():
    ranking = request.form['ranking']
    rating = request.form['rating']
    genre = request.form['genre']
    
    # Get ranking, rating information and initialize genre values to 0
    li = [[int(ranking), float(rating)] + [0]*18]

    # Put 1 to selected genre
    li[0][dic[genre]] = 1

    # Pass all information to the model and get the predicted sales point
    prediction = model.predict(li)

    return str(prediction)
    

if __name__ == '__main__':
    app.run(debug=True)
