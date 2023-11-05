import random
import json
import torch
from brain import neuralNetwork
from brain2 import Bag_Of_Words,token_size

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = neuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# From here we start to write the code for my personal assistant......


Name = "David"

from listen import Listen
from Speak import Say
from taskexecution import NonInputExecution
from taskexecution import InputExecution
from taskexecution import WishMe




if 1:
    WishMe()

def Main():
    
    sentence = Listen()
    result = str(sentence)
    if sentence == "bye":
        exit()

    sentence = token_size(sentence)
    X = Bag_Of_Words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _ , predicted = torch.max(output,dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["response"])
            
                if "time" in reply:
                    Say("Sir the time is:")
                    NonInputExecution(reply)
                    
                
                elif "date" in reply:
                    Say("Sir the date is :")
                    NonInputExecution(reply)

                elif "day" in reply:
                    Say("Sir today is :")
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    Say("wait a second sir i'm fetching the result that you want")
                    InputExecution(reply, result)
                   

                elif "google" in reply:
                    InputExecution(reply, result)
                    Say("sir I am searching on google for this")

                elif "YouTube" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening you tube for you...")

                elif "facebook" in reply:
                    InputExecution(reply, result)
                    # Say("sir as per your order i'm opening your facebook account.....")

                elif "instagram" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening your instagram account....")

                elif "twitter" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening your twitter account.....")

                elif "chat GPT" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening chat GPT for you.....")

                elif "browser" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening browser for you....")

                elif "notepad" in reply:
                    InputExecution(reply, result)
                    Say("sir as per your order i'm opening notepad for you....")

                elif "IP address" in reply:
                    InputExecution(reply, result)

                elif "open camera" in reply:
                    InputExecution(reply, result)

                elif "command prompt" in reply:
                    InputExecution(reply, result)

                elif "Temperature" in reply:
                    InputExecution(reply, result)

                elif "Shut Down" in reply:
                    InputExecution(reply, result)

                elif "where is" in reply:
                    InputExecution(reply, result)

                elif "spotify" in reply:
                    InputExecution(reply, result)


                elif "switch the window" in reply:
                    InputExecution(reply, result)

                elif "personal code" in reply:
                    InputExecution(reply, result)
                    

                

                # elif "State Drive" in reply:
                #     InputExecution(reply, result)
                #     Say("sir as per your order i'm opening your solid state drive....")

                else:
                    Say(reply)

while True:
    Main()




        





