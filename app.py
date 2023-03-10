from flask import *

app = Flask(__name__)


# index
@app.route('/index')
@app.route('/index.html')
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


# about
@app.route('/about.html')
@app.route('/about')
def about():
    return render_template('about.html')


# contact
@app.route('/contact.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')


# project
@app.route('/project.html')
@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/service.html')
@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/team.html')
@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/testimonial.html')
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@app.route('/show/<imgString>')
def show(imgString):
    srcImage = '/static/img/' + imgString +'.jpg'
    # "/static/img/qallpeach.jpg
    return render_template('show.html', srcImage=srcImage)


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True, port=3000)
