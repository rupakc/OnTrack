from flask import Flask, render_template, request, session
import warnings

warnings.filterwarnings("ignore")


# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True


@app.route("/", methods=['GET', 'POST'])
def namelist():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000)
