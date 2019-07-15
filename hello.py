from flask import Flask
from flask import render_template,request
from pathlib import Path
import glob
import shutil

app = Flask(__name__)


all_list =[]
num_count = 0

p = Path("static/image/input")
all_list = list(p.glob("*.jpg"))
app.logger.debug(all_list)


@app.route('/')
def hello(name=None):
    global num_count
    global all_list
    #shutil.copy(str(all_list[num_count]),"static/image/temp/temp.jpg")
    input_path = str(all_list[num_count])
    
    return render_template('hello.html', input_path=input_path)

@app.route('/next' ,methods=['POST'])
def rank(name=None):
    global num_count
    global all_list
    if request.method == "POST":
        res = request.form["bt"]
        if res =="good":
            move_path = "static/image/good/"
        elif res == "midle":
            move_path = "static/image/midle/"
        elif res == "bad":
            move_path = "static/image/bad/"
            pass                
        shutil.move(str(all_list[num_count]),move_path)
        num_count = num_count +1
        #shutil.copy(str(all_list[num_count]),"static/image/temp/temp.jpg")
        input_path = str(all_list[num_count])

    return render_template('hello.html', input_path = input_path)

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)