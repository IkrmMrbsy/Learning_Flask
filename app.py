from flask import Flask

#Inisialisais Object nya 
app1 = Flask(__name__)

#Membuat Routing nya
@app1.route("/index")
def index():
    return "<h1>Hallo World</h1>"

#Untuk menjalankan aplikasi flask nya
if __name__ == "__main__":
    app1.run(debug=True)