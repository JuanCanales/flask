# importamos las librerias
from flask import Flask, render_template, request

app = Flask (__name__)

# asociamos rutas de  url path con la funcion que respondera. 
# en este caso retornara un html (que ha de estar en templates)
@app.route("/")
def index():
    return render_template("index.html")

# en este caso retornara un html (que ha de estar en templates)
@app.route("/form")
def formulario():
    return render_template("formulario.html")

# recibe los datos de un formulario con POST, recupera el parametro enviado en el formulario y lo reenviamos a contacto.html
@app.route("/contacto", methods=["POST"])
def contacto_function():
    nombre = request.form.get("nombre")
    return render_template("contacto.html", parametro1 = nombre)

# en este caso retornara un html que le hemos pasado una variable, esa variable estara referenciada en el html
# ademas a ese html le hemos añadido sentencia de logica , un if y un for pasandole 2 parametros diferentes
@app.route("/nombreciudad")
def nombreciudad():
    ciudad = "Barcelona"
    numeros = [1,2,3,4,5]
    #ciudad = "London"
    return render_template("ciudad.html", city = ciudad, num = numeros)

# en este caso retornara una frase en ingles
@app.route("/en")
def index_en():
    return "Hello world"

# en este caso retornara una frase en spanish
@app.route("/es")
def index_es():
    return "Hola mundo"

# en este caso retornara un saludo al nombre pasado como parametro en el path
@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return f"Hola {nombre}"

# esto se pone para activar el debug, y no tenga que hacer stop-restart del servidor para ver los cambios, pero no funciona
if __name__ == "__main__":
    app.run(debug=True)

