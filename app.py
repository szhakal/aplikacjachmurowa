from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact3')
def contact3():
    return render_template("contact3.html")
    
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about1')
def about():
    return render_template('about1.html')
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/error_not_found') 
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404) 
    response.headers['X-Something'] = 'A value'
    return response

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('505.html'), 505


