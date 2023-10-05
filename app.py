#source: https://medium.com/@sharma.tanish096/sentiment-analysis-using-pre-trained-models-and-transformer-28e9b9486641
from utils import get_all_data, get_wells_fargo_data
import random
#%%
wells_fargo_data = get_wells_fargo_data()

#%%
from flask import Flask, render_template

app = Flask(__name__)

complaints = list(wells_fargo_data["Consumer complaint narrative"].dropna())
random.seed(0)
random.shuffle(complaints)
complaint_index = 0

@app.route("/")
def index():
    return render_template("index.html", complaints=complaints)

if __name__ == "__main__":
    app.run()
