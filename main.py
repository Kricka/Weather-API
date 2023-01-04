from flask import Flask, render_template
import pandas as pd
import numpy as np

app=Flask(__name__)

stations=pd.read_csv("data/stations.txt",skiprows=17)
stations2=stations[['STAID','STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html",data=stations2.to_html())

@app.route("/api/v1/<station>/<date>/")
def about(station,date):
    filename="data/TG_STAID" + str(station).zfill(6)+ ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature=df.loc[df['    DATE']== date]["   TG"].squeeze()/10
    return{ "station":station,
            "date": date,
            "temeperature":temperature
            }

if __name__=="__main__":
    app.run(debug=True,port=5001)