import os
from flask import Flask, render_template
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD']= True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau.html")

@app.route("/jupyterdata")
def jupyterdata():
    return render_template("jupyterdata.html")

@app.route("/story")
def story():
    return render_template("story.html")





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
