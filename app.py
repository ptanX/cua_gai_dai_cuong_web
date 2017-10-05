from flask import Flask, render_template, redirect, send_from_directory
import os
import mlab
from mongoengine import Document, StringField
mlab.connect()
app = Flask(__name__)
app.config["DEBUG"] = True
# 1. connect to mlab
# 2. Add data
# 3. get data for render_template


class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

girl_types = GirlType(name="Gái tiểu thư",
    image="https://via.placeholder.com/400x200",
    description="Thích gọn gàng sạch sẽ, giỏi nghệ thuật, thích đến nơi sang chảnh ...")
#girl_types.save()

g= [
    {
        "name": "Gái tiểu thư",
        "image": "https://via.placeholder.com/400x200",
        "description":"Thích gọn gàng sạch sẽ, giỏi nghệ thuật, thích đến nơi sang chảnh ...",
    },
    {
        "name": "Gái ngoan",
        "image": "https://via.placeholder.com/400x200",
        "description":"Tính bình dị, trẻ như học sinh, già như công sở. Cẩn thận, chăm học. Hay xuất hiện ở thư viện L'espace",
    },
    {
        "name": "Gái ngoan",
        "image": "https://via.placeholder.com/400x200",
        "description":"Thích gọn gàng sạch sẽ, giỏi nghệ thuật, thích đến nơi sang chảnh ...",
    },
]
@app.route('/')
def index():
    return render_template('index.html', girl_types = GirlType.objects())
@app.route('/favico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/school')
def school():
    return redirect("http://techkids.vn/")

app.run()
