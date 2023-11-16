from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def root ():
    return "bienbenidos"

from alumnos_docentes import alumnos_docentes 

@app.route("/alumnos_docentes")
def getAlumnos():
    return jsonify (alumnos_docentes)


## BUSCAR UN ALUMNO
@app.route("/alumnos_docentes/<string:alumno_name>")
def getalumno(alumno_name):
    alumnofound = [alumno for alumno in alumnos_docentes if alumno ["Nombre"] == alumno_name]
    if (len(alumnofound) > 0):
        return jsonify ({"alumno_docentes": alumnofound[0]})

## AGREGAR UN ALUMNO 
@app.route("/alumnos_docentes", methods=["POST"])
def addalumno():
    alumno = request.json
    alumnos_docentes.append(alumno)
    return jsonify({"mensaje": "alumno agregado satisfactoriamente", "alumnos_docentes":alumnos_docentes})

## Actualizar UN ALUMNO
@app.route("/alumnos_docentes/<string:alumno_name>", methods=["PATCH"])
def patchalumno(alumno_name):
    alumno_found = [alumno for alumno in alumnos_docentes if alumno["Nombre"] == alumno_name]
    if len(alumno_found) > 0:
        alumno_actualizado = {}
        for key, value in request.json.items():
            alumno_actualizado[key] = value
        alumno_found[0].update(alumno_actualizado)
        return jsonify({
            "mensaje": "Alumno Actualizado satisfactoriamente",
            "alumno_docentes": alumno_found[0]
})
    
## ELIMINAR UN ALUMNO
@app.route("/alumnos_docentes/<string:alumno_name>", methods=["DELETE"])
def eliminalumno(alumno_name):
    alumnosfound = [alumno for alumno in alumnos_docentes if alumno["Nombre"] == alumno_name]
    if len(alumnosfound) > 0:
        alumnos_docentes.remove(alumnosfound[0])
        return jsonify({
            "mensaje": "Alumno Eliminado",
            "alumnos_docentes": alumnos_docentes
})

if __name__ == "__main__":
    app.run(debug=True )
