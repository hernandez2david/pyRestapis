from flask import Flask
from flask import jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/ciscoapp')
def ciscoapp():
    return "This is for telephony, for example"

@app.route('/hidden')
def hidden():
    secret1 = {
        "Area51" : "There are not aliens there",
        "Kennedy" : "It was Russia",
        "TimeNow": str(currentDT)
    }

    return jsonify(secret1)

@app.route('/Time')
def times():
    currentDT = datetime.datetime.now()
    currentMonth = currentDT.month
    currentDay = currentDT.day
    currentHour = currentDT.hour
    curentMinute = currentDT.minute
    secret1 = {
        "Area51" : "There are not aliens there",
        "Kennedy" : "It was Russia",
        "TimeNow": str(currentDT)
    }
    timeSectioned = {
        "TimeNow": str(currentDT),
        "Month": str(currentMonth),
        "Day": str(currentDay),
        "Hour": str(currentHour), 
        "Minute":str(curentMinute),
        "Secret" : secret1
    }

    return jsonify(timeSectioned)

if __name__ == "__main__":
    app.run(debug = True)