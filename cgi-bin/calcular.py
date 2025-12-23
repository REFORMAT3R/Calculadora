#!C:/Users/VAIO/AppData/Local/Programs/Python/Python39/python.exe

import cgi
import re

print("Content-Type: text/html\n")
form = cgi.FieldStorage()

expresion = ""
if "expresion" in form:
    expresion = form.getvalue("expresion")

print("<!DOCTYPE html>")
print("<html lang='es'>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<title>Resultado</title>")
print("</head>")
print("<body>")
print("<h1>Resultado</h1>")

if expresion == "":
    print("<p>Error: no se ingresó ninguna expresión</p>")
else:
    expresion = expresion.replace(" ", "")
    patron = r'^[0-9+\-*/().]+$'

    if not re.match(patron, expresion):
        print("<p>Error: expresión inválida</p>")
    else:
        try:
            resultado = eval(expresion)
            print(f"<p>Expresión: {expresion}</p>")
            print(f"<p>Resultado: {round(resultado, 2)}</p>")
        except:
            print("<p>Error al calcular la expresión</p>")

print("<br>")
print("<a href='/calculadora/html/index.html'>Volver</a>")
print("</body>")
print("</html>")