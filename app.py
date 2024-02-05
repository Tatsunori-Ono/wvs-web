from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Define the routes and their corresponding names
routes = [
        ("/about", "ABOUT"),
        ("/news", "NEWS"),
        ("/calendar", "CALENDAR"),
        ("/resources", "RESOURCES"),
        ("/contact", "CONTACT"),
]

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/")
def home():
    return redirect(url_for("about"))

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
