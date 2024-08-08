from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create a route
@app.route('/')
def index():
    cras= ["abc","def"]
    return render_template('blog.html', cras=cras)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


# create custom error page

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)
 