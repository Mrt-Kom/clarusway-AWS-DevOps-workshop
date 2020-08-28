from flask import Flask

app=Flask(__name__) 

@app.route("/")
def head():
    return "Hello World"

@app.route("/second")
def iki():
    return "This is the second Page"

@app.route("/third/subthird")
def uc():
    return "Hello This is <h1>3.</h1> <em>Page</em>"

@app.route("/fourth/<string:id>")
def dort(id):
    return f"Id of this page is {id}"

@app.route("/fifth")
def bes():
    return "<h1>5555</h1>"  

if __name__ == "__main__":
    app.run(debug=True) #hatalari bize gosterecek sekilde tanimladik