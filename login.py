from flask import Flask, render_template, request, url_for, session, redirect

app6 = Flask(__name__)
app6.config["SECRET_KEY"] = "Ikram2003"

@app6.route("/", methods=["POST", "GET"])
def login():
    #Mengecek apakah sudah login atau belum
    if "email" in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        #Isi dari variable email dan password yaitu ['email] ['password] harus sesuai dengan (name) yang ada di html
        email = request.form['email']
        password = request.form['password']

        #Jika email dan password benar
        if email == 'ikram@gmail.com' and password == 'ikr2003':
            session['email'] = email #Simpan identitas email di dalam session
            return redirect(url_for('home'))
        
        #Jika email dan password salah
        else:
            return redirect(url_for('login'))
    
    #Jika belum login dia akan mengarahkan ke login
    return render_template("login.html")

@app6.route("/home")
def home():
    #Mengecek apakah sudah login atau belum
    if "email" in session:
        pesan = "Anda sukses login!" #Variable yang berisi data pesan sukses
        return render_template("home.html", pesan=pesan)#Lalu kirim variable pesan yang berisi data tersebut ke html
    else:
        return redirect(url_for('login'))

@app6.route("/about")
def about():
    #Mengecek apakah sudah login atau belum
    if "email" in session:
        return render_template("about.html")
    else:
        return redirect(url_for('login'))

@app6.route("/contact")
def contact():
    #Mengecek apakah sudah login atau belum
    if "email" in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('login'))
    
@app6.route("/logout")
def logout():
    session.pop("email", None) #Menghapus email , walaupun tidak ada dengan menambahkan (None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app6.run(debug=True, port=8080)
