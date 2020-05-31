
import sys
from flask import Flask, render_template
sys.path.append("models")
from AccuracyScore import getAccuracyScore
 
app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html', message=getAccuracyScore())
 
@app.errorhandler(404)
def page_not_found(e):
    
    return render_template('404.html', title="404 - Flask project"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')