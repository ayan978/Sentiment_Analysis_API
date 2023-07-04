from setfit import SetFitModel

# The class named classifier is created to calculate the output of the sentiment by using the pretrained model
class Classifier:
    def __init__(self):
        self.model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
    
    #defining function to predict the sentiment analysis using the pretrained sentiment model
    def get_sentiment_output(self, text: str):
        result = {}
        output = self.model([text])
        
        if output == 0:  #If the model's output is 0, it means the sentiment is negative
            result['sentiment'] = 'negative'  #Updating the dictionary with key and value named 'sentiment' and 'negative'

        elif output == 1:  #If the model's output is 1, it means the sentiment is positive
            result['sentiment'] = 'positive'  #Updating the dictionary with key and value named 'sentiment' and 'positive'

        else:  #If the model's output is something other than 0 and 1, it means the sentiment is neutral
            result['sentiment'] = 'neutral'  #Updating the dictionary with key and value named 'sentiment' and 'neutral'

        return result