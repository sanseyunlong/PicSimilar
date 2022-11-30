from flask import Flask, render_template, request, flash, redirect, url_for, make_response
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename

import CleanAll
import DownPic
import Key
import OrcPic
from SQLite import SQLite
import SpiderPic
from ComparePic import ComparePic
from UploadPic import UploadPic

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))
uploadDir = os.path.join(basedir, 'static/uploads')


@app.route('/', methods=['POST', 'GET'])
def process():
    global image,ans
    if request.method == 'POST':
        CleanAll.main()
        f = request.files.get('selectfile')
        if not os.path.exists(uploadDir):
            os.makedirs(uploadDir)
        if f:
            filename = secure_filename(f.filename)
            types = ['jpg', 'png', 'tif']
            if filename.split('.')[-1] in types:
                uploadpath = os.path.join(uploadDir, filename)
                f.save(uploadpath)
                flash('上传加载成功！', 'success')
                image,ans = OrcPic.pic_sb1("./static/uploads/{}".format(filename))
                a = UploadPic(key=Key.get_access_token_compare(), image=image)
                a.upload()
                lists = SpiderPic.main(ans)

                dict1, dict2 = ComparePic(key=Key.get_access_token_compare(), lists=lists).res()
                print(dict2)

                b = SQLite(dict1, dict2)
                b.create_table()
                b.insert_data()
                result2 = b.open_data()
                for ret in result2:
                    DownPic.img_info(ret,dict2[ret])
                b.close_sql()
                a.dalete()
                if request.form['submit'] == '上传':
                    return render_template('base.html', ans=ans, imagename=filename,result2=result2)
            else:
                flash('无法识别文件格式!', 'danger')
        else:
            flash('没有选择文件！', 'danger')
    return render_template('base.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8987,debug= True)

