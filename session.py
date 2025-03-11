from flask import Flask, session #Jika ingin pakai session, import dulu

app4 = Flask(__name__)

#Karena memakai Sessi, kita butuh yg namanya Secret Key
app4.config["SECRET_KEY"] = "HEY2003"  #Untuk isi nya bebas

#Memparsing nilai dari URL untuk meng set nilai session
@app4.route("/halaman/<int:nilai>")
def session_1(nilai):
    session["nilai_1"] = nilai
    return "Berhasil mengset nilainya"

#Lalu tampilkan di halaman 
@app4.route("/halaman/lihat")
def view_session_1():
    try:
        data = session["nilai_1"]
        return "Nilai yang telah di set adalah = {}".format(data)
    except:
        return "Anda tidak memiliki nilai session lagi"

#Lalu di sini membuat logout/destroy
#Biasanya ini untuk menghapus session agar tidak bisa di akses lagi
@app4.route("/halaman/logout")
def logout_session_1():
    session.pop("nilai_1")
    return "Berhasil Logout/Menghapus Session"


#Cara mencoba nya di Web :
#Ketikan di URL nya http://127.0.0.1:5000/halaman/ <- di sini masukan nilai nya
#http://127.0.0.1:5000/halaman/232 <- Misal nya seperti ini
#Lalu jika ingin melihat nilai nya http://127.0.0.1:5000/halaman/lihat 

#Untuk Logout
#Otomatis akan menghapus nilai yang tadi kita masukan
#http://127.0.0.1:5000/halaman/lihat <- Jika kita akses ini , akan menampilkan pesan tidak memiliki session, karena session nya sudah terhapus
#Lalu jika ingin logout http://127.0.0.1:5000/halaman/logout


if __name__ == "__main__":
    app4.run(debug=True)