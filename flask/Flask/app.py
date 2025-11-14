from flask import Flask
'''create an instance of flask and name it app'''
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to our web page,we are creating an app"
if __name__=="__main__":
    app.run(debug=True)