from flask import Flask
from flask import render_template,request
from pathlib import Path
import glob
import shutil

app = Flask(__name__)
all_list =[]
num_count = 0

@app.route('/')
def hello(name=None):
    p = Path("static/image/input")
    all_list = list(p.glob("*.jpg"))
    app.logger.debug(all_list)
    shutil.copy(all_list[0],"static/image/temp/temp.jpg")
    
    return render_template('hello.html', name=name)

@app.route('/next' ,methods=['POST'])
def rank():
    if request.method == "POST":
        res = request.form["bt"]
    return res

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)