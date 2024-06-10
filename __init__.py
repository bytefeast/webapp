import os

from flask import Flask, render_template, request, redirect, url_for

import YoutubeTags
from YoutubeTags import videotags


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():

        if request.method == 'GET':
            date = request.args.get('nm1')
            print(date)
            if(date != None):
                findtags = videotags(str(date))  # Mkbhd's Video
                return render_template('index.html' , data=findtags)

        return render_template('index.html')


    @app.route('/result', methods=['GET', 'POST'])
    def result():

        if request.method == 'GET':
            date = request.form.get('nm1')
            findtags = videotags("https://www.youtube.com/watch?v=RTbrXiIzUt4")  # Mkbhd's Video

            print(findtags)

            return render_template('result.html', data=findtags)
        print("fds")
        return render_template('result.html')


    return app