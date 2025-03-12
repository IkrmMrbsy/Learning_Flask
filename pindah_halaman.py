from flask import Flask, render_template, url_for, redirect

app5 = Flask(__name__)

#Template-Based Routing
@app5.route("/")
def home():
    return render_template("home.html")

@app5.route("/about")
def about():
    return render_template("about.html")

@app5.route("/contact")
def contact():
    return render_template("contact.html")

#Redirection-Based Routing
@app5.route("/go-home")
def redirect_home():
    return redirect(url_for('home'))

@app5.route("/go-about")
def redirect_about():
    return redirect(url_for('about'))

@app5.route("/go-contact")
def redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app5.run(debug=True)