# AdaptReady

### How to run the code

1. Run confirm `pip install -r requirments.txt`
2. Open terminal
3. Run `python Deployment-flask/app.py`
4. Open your browser and enter `http://127.0.0.1:5000/`

### Explanation of Jupyter Notebook

1. Download and extract the dataset in the main directory
2. Use the movie dataset to create training and test data
3. Clean and preprocess the data
4. Download and extract Glove embedding from this website (https://nlp.stanford.edu/projects/glove/) and download this zip (https://nlp.stanford.edu/data/glove.42B.300d.zip)
5. Tokenize the data 
6. Use glove embedding as a pretrained embedding for the model
7. Create a model with embedding layer as the initial layer and 
add LSTM layer
8. Train the model
9. Evaluate the model on Test Dataset
