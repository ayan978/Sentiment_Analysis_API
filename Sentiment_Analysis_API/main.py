from fastapi import FastAPI
import uvicorn
from classifier import Classifier
import logging
from input_class import input_class

app = FastAPI()  #creating instance to run the app
classifier = Classifier()  #creating instance of the classifier class


@app.get("/")   
def root():  #Handling root url with the function root()
    return {"Root": "root_url"}


@app.post("/analyze")  
def analyze_output(data: input_class):  #Function to process the post the POST request at /analyze and show the prediction by the model
    try:
        data = data.dict()
        input = data['text']  #Will take input as the binding value of the 'text' key in the dictionary named 'data'
        result = classifier.get_sentiment_output(input)  #Storing the sentiment analysis result produced by the pretrained model inside 'result' variable 
        return result
    
    except Exception as e:
        logging.error("Something went wrong")  #Handling the exception for any kind of invalid request of server error
        

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
    
 


