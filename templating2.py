from flask import Flask, render_template

app3 = Flask(__name__)

@app3.route("/")
def templating():
    #Memakai Looping
    #Membuat array 
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

    #Membuat condtion/ if-else
    suasana = "senang"
    return render_template("index2.html", value=hari, value2=suasana) #(value) bisa di ganti dengan nama apapun, tidak harus value

#Membuat route untuk halaman Contact
@app3.route("/contact")
def contact():
    return render_template("contact.html")

#Membuat route untuk halaman About
@app3.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app3.run(debug=True)