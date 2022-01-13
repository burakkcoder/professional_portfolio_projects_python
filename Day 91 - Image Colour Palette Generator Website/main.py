from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, flash
import colorgram
from PIL import *
from werkzeug.utils import secure_filename
import os

rgb_colors = None
hex_colors = None

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    

def rgb_to_hex(rgb):
    return ('{:X}{:X}{:X}').format(rgb[0], rgb[1], rgb[2])

def delete_uploads():
    for_delete = os.listdir("./static/uploads")
    for x in for_delete:
        os.remove(f"./static/uploads/{x}")

@app.route("/")
def index():
    global rgb_colors
    global hex_colors
    rgb_colors = None
    hex_colors = None
    delete_uploads()
    return render_template("index.html")

@app.route("/colors", methods=["GET","POST"])
def colors():
    if request.method == "POST":
        delete_uploads()
        upload_file()
    global rgb_colors
    global hex_colors
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("colors.html", files=files, rgb_colors = rgb_colors, hex_colors = hex_colors)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global rgb_colors
    global hex_colors
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        rgb_colors = []
        colors = colorgram.extract(file, 10)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            rgb_colors.append(new_color)
        hex_colors = []
        for color in rgb_colors:
            hex_colors.append(rgb_to_hex(color))
    return redirect(url_for("colors"))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)