from flask import Flask, render_template, request, session

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

#Parsing nilai int
#Mengambil langsung data dari URL dan menggunakan nya di dalam aplikasi kita
@app3.route("/parsing/<int:nilai1>")#Jika URL yang di input bukan bertipe int dia akan error 404
def parsing1(nilai1):
    #Bagian {} adalah placeholder dalam string
    #.format() akan menggantikan {} dengan nilai variable (nilai1)
    #Intinya digunakan untuk memasukan nilai variable ke dalam teks string
    return "Nilainya adalah : {}".format(nilai1)

#Parsing nilai String
@app3.route("/parsing2/<string:nama>")
def parsing2(nama):
    return "Nama saya adalah : {}".format(nama)

#Argument Parser
#Menggunakan query parameter
#Mengambil data dari parameter query setelah tanda ? di URL
@app3.route("/parsing3")
def parsing3():
    data = request.args.get("nilai2")#Mengambil nilai query (nilai2)
    return "Nilainya adalah : {}".format(data)


if __name__ == "__main__":
    app3.run(debug=True)