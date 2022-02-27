#Data imports
import re
import json
import numpy as np

#ML imports
import keras
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences

#Api imports
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

#Load the model
model = keras.models.load_model("model.h5")

#Load the tokenizer
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

#Clean the given review text
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result
def clean_further(string):
    result = string.lower()
    result = re.sub(r"(\.|\(|\))"," ",result)
    result = re.sub(r"\s{1,}"," ",result)
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    review = [x for x in request.form.values()]
    #clean the review
    review = remove_tags(review[0])
    review = clean_further(review)
    #Tokenize the review
    tokenized_indices = tokenizer.texts_to_sequences([review])
    reviews_list_idx = pad_sequences(tokenized_indices, maxlen=150, padding='post')
    #predict the sentiment
    review_prediction = model.predict(reviews_list_idx)[0][0]

    if review_prediction >= 0.5:
        prediction_sentiment = "Positive"
    else:
        prediction_sentiment = "Negative"

    prediction_score = round(review_prediction*10)

    return render_template('index.html', prediction_text='The review is {} with a sentiment score of {}'.format(prediction_sentiment,prediction_score))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)