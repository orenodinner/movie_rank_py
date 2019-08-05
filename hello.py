#!/home/dinner/photo_rank_py/venv/bin/python3


from flask import Flask
from flask import render_template,request
from pathlib import Path
import glob
import shutil
import split
import os


app = Flask(__name__)


all_list =[]
num_count = 0

p = Path("static/movie/input")
all_list = list(p.glob("*.mp4"))
app.logger.debug(all_list)


@app.route('/')
def hello(name=None):
    global num_count
    global all_list
    #shutil.copy(str(all_list[num_count]),"static/image/temp/temp.jpg")
    input_path = str(all_list[num_count])
    
    return render_template('hello.html', all_list = all_list)

@app.route('/good')
def good(name=None):
    global num_count
    global all_list
    #shutil.copy(str(all_list[num_count]),"static/image/temp/temp.jpg")
    input_path = str(all_list[num_count])
    p = Path("static/movie/good")
    all_list = list(p.glob("*.mp4"))
    app.logger.debug(all_list)
    return render_template('hello.html', all_list = all_list)

@app.route('/midle')
def midle(name=None):
    global num_count
    global all_list
    #shutil.copy(str(all_list[num_count]),"static/image/temp/temp.jpg")
    input_path = str(all_list[num_count])
    p = Path("static/movie/midle")
    all_list = list(p.glob("*.mp4"))
    app.logger.debug(all_list)
    return render_template('hello.html', all_list = all_list)


@app.route('/next' ,methods=['POST'])
def rank(name=None ):
    global num_count
    global all_list
    if request.method == "POST":
        res = request.form["bt"]
        res_list = res.split(",")
     #   file_name = request.form["file"]
        if res_list[0] =="good":
            move_path = "static/movie/good/"
        elif res_list[0]  == "midle":
            move_path = "static/movie/midle/"
        elif res_list[0]  == "bad":
            move_path = "static/movie/bad/"
            pass                
        file_name = os.path.basename(res_list[1])
        if os.path.exists(move_path + file_name):
            shutil.move(res_list[1],"static/movie/del/")
        else:
            shutil.move(res_list[1],move_path)
        p = Path("static/movie/input")
        all_list = list(p.glob("*.mp4"))
        app.logger.debug(all_list)
    return render_template('hello.html', all_list = all_list)

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)