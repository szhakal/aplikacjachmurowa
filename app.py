from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/error_not_found') 
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404) 
    response.headers['X-Something'] = 'A value'
    return response


