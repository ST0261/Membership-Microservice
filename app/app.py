from Membership_handler.membership_handler import membership_router

from flask import Flask


app = Flask(__name__)           #Creating an App instance

app.register_blueprint(membership_router)


@app.route("/")
def hello():
    return "Membership server"

if __name__ == "__main__":      #On running python app.py
    #Initialized db
    #Start app
    app.run('0.0.0.0',debug=False)         #Run the flask App