from flask import Flask, render_template #index.html yi calistirmak icin 

app= Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html",number1=12,number2=234)

@app.route("/second")
def second():
    return render_template("yeni.html", hazirlayan = "ABC")
if __name__=="__main__":
    app.run(debug=True)