from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('client_ui.html')

@app.route("/servo/<id>")
def servo(id):
     client.publish("servo"+tankID,id)
    return redirect('/')
    

@app.route("/move/<id>")
def move(id):
    client.publish("move"+tankID,id)
    return redirect('/')

@app.route("/shoot/")
def shoot():
    return redirect('/')

@app.route("/picture/")
def picture():
    client.publish("picture"+tankID,"*")
    return redirect('/')


# run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
