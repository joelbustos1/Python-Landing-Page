from flask import Flask, render_template

app = Flask("my-first-website-python")

@app.route("/")             #tener diferentes rutas
def hello_world():
    return render_template("index.html")

@app.route("/example")
def example_route():
    return "Esto es una pagina de ejemplo"

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/gtx1660")
def gtx1660():
    return render_template("gtx1660.html")

@app.route("/rtx2060")
def rtx2060():
    return render_template("rtx2060.html")

@app.route("/rtx3060")
def rtx3060():
    return render_template("rtx3060.html")

@app.route("/ryzen5")
def ryzen5():
    return render_template("ryzen5.html")

@app.route("/i51400")
def i510400():
    return render_template("i51400.html")

@app.route("/i3")
def i3():
    return render_template("i3.html")


"""@app.route("/<name>")
def return_with_dynamic_content(name):
    return render_template("name.html", contenido = name, lorem = "Test Text")
"""

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port='5000')   #debug = true es que estoy en fase de desarrollo aun



