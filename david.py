import random
import json
import sys
import torch
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from DavidUI import Ui_Dialog
from brain import neuralNetwork
from brain2 import Bag_Of_Words,token_size
from flask import *
from flask import Flask, request, jsonify
from flask_sslify import SSLify
app = Flask(__name__)
sslify = SSLify(app)


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


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.Main()

    # @app.route('/')
    def index(self):
        return "David- A personal Assistant"

    # @app.route('/Main', methods=['POST'])
    def Main(self):
        
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
                    self.reply = random.choice(intent["response"])
                
                    if "time" in self.reply:
                        Say("Sir the time is:")
                        NonInputExecution(self.reply)
                        
                    
                    elif "date" in self.reply:
                        Say("Sir the date is :")
                        NonInputExecution(self.reply)

                    elif "day" in self.reply:
                        Say("Sir today is :")
                        NonInputExecution(self.reply)

                    elif "wikipedia" in self.reply:
                        Say("wait a second sir i'm fetching the result that you want")
                        InputExecution(self.reply, result)
                    

                    elif "google" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir I am searching on google for this")

                    elif "YouTube" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening you tube for you...")
                    
                    elif "Open My Game website" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening your game website for you...")

                    elif "facebook" in self.reply:
                        InputExecution(self.reply, result)
                        # Say("sir as per your order i'm opening your facebook account.....")

                    elif "instagram" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening your instagram account....")

                    elif "twitter" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening your twitter account.....")

                    elif "chat GPT" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening chat GPT for you.....")

                    elif "browser" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening browser for you....")

                    elif "notepad" in self.reply:
                        InputExecution(self.reply, result)
                        Say("sir as per your order i'm opening notepad for you....")

                    elif "IP address" in self.reply:
                        InputExecution(self.reply, result)

                    elif "open camera" in self.reply:
                        InputExecution(self.reply, result)

                    elif "command prompt" in self.reply:
                        InputExecution(self.reply, result)

                    elif "Temperature" in self.reply:
                        InputExecution(self.reply, result)

                    elif "Shut Down" in self.reply:
                        InputExecution(self.reply, result)

                    elif "where is" in self.reply:
                        InputExecution(self.reply, result)

                    elif "spotify" in self.reply:
                        InputExecution(self.reply, result)


                    elif "switch the window" in self.reply:
                        InputExecution(self.reply, result)

                    elif "coding profile" in self.reply:
                        InputExecution(self.reply, result)

                    elif "maximize" in self.reply:
                        InputExecution(self.reply, result)

                    elif "minimise" in self.reply:
                        InputExecution(self.reply, result)

                    elif "close" in self.reply:
                        InputExecution(self.reply, result)
                    
                    elif "tell me about" in self.reply:
                        InputExecution(self.reply, result)

                    else:
                        Say(self.reply)
        # return jsonify({'response': 'your response here'})




class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Iron_Template_1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/somes/Downloads/giphy.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/initial.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Health_Template.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/B.G_Template_1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Code_Template.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/somes/Downloads/a064a7f04f9ecbf99cc543f1ba976adb69949e71_hq.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Jarvis_Gui (1).gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Hero_Template.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/Earth_Template.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/DAVID GUI/__1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)

        timer.start(1000)
        StartThread.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)    
if __name__ == "__main__":
    StartThread = MainThread()
    WishMe()
    # app.run(ssl_context=("C:\\ProgramData\\chocolatey\\bin\\self_signed_cert.pem", "C:\\ProgramData\\chocolatey\\bin\\self_signed_key.pem"))
    while True:
        app = QApplication(sys.argv)
        David = main()
        David.show()
        exit(app.exec_())
