#Disini memakai Templating
from flask import Flask, render_template #Menggunakan templating dengan render_template()
#memungkinkan penggunaan file HTML terpisah dan pengiriman data dinamis ke tampilan.

app2 = Flask(__name__)

@app2.route("/")
def templating():
    angka = 100 #Membuat variable yang berisi data 100
    return render_template("index.html", nilai=angka) #Lalu mengirimkan data nya ke view/tampilan

if __name__ == "__main__":
    app2.run(debug=True)