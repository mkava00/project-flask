
import sys
from flask import Flask, render_template
sys.path.append("models")
from AccuracyScore import getAccuracyScore
import pickle
 
app = Flask(__name__)
 

@app.route('/')
def index():
    
    return render_template('index.html', message=getAccuracyScore())
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')