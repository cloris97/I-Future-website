# from flask import Flask
# application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"

# if __name__ == "__main__":
#     application.run(host='0.0.0.0')

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_us():
    return render_template('aboutUs.html')

@app.route('/product')
def product():
    return render_template('product.html')