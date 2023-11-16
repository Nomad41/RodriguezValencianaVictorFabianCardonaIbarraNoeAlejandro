from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def root ():
    return "bienbenidos"

from alumnos import alumnos 

@app.route("/alumnos")
def getAlumnos():
    return jsonify (alumnos)


## BUSCAR UN ALUMNO
@app.route("/alumnos/<string:alumno_name>")
def getalumno(alumno_name):
    alumnofound = [alumno for alumno in alumnos if alumno ["Nombre"] == alumno_name]
    if (len(alumnofound) > 0):
        return jsonify ({"alumno": alumnofound[0]})

## AGREGAR UN ALUMNO 
@app.route("/alumnos", methods=["POST"])
def addalumno():
    alumno = request.json
    alumnos.append(alumno)
    return jsonify({"mensaje": "alumno agregado satisfactoriamente", "alumnos":alumnos})


if __name__ == "__main__":
    app.run(debug=True )
