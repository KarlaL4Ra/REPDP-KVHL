from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

registros = []

@app.route("/", methods=["GET", "POST"])
def index():
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        hora_entrada = request.form["hora_entrada"]
        hora_salida = request.form["hora_salida"]

        # Calcular minutos de duración
        minutos = None
        if hora_entrada and hora_salida:
            h1 = datetime.strptime(hora_entrada, "%H:%M")
            h2 = datetime.strptime(hora_salida, "%H:%M")
            minutos = int((h2 - h1).total_seconds() / 60)

        nuevo = {
            "fecha": request.form["fecha"],
            "empresa": request.form["empresa"],
            "origen": request.form["origen"],
            "transportista": request.form["transportista"],
            "contenedor": request.form["contenedor"],
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida,
            "minutos": minutos
        }

        registros.append(nuevo)

    return render_template("index.html", registros=registros, fecha_hoy=fecha_hoy)


from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

registros = []

@app.route("/", methods=["GET", "POST"])
def index():
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        hora_entrada = request.form["hora_entrada"]
        hora_salida = request.form["hora_salida"]

        # Calcular minutos de duración
        minutos = None
        if hora_entrada and hora_salida:
            h1 = datetime.strptime(hora_entrada, "%H:%M")
            h2 = datetime.strptime(hora_salida, "%H:%M")
            minutos = int((h2 - h1).total_seconds() / 60)

        nuevo = {
            "fecha": request.form["fecha"],
            "empresa": request.form["empresa"],
            "origen": request.form["origen"],
            "transportista": request.form["transportista"],
            "contenedor": request.form["contenedor"],
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida,
            "minutos": minutos
        }

        registros.append(nuevo)

    return render_template("index.html", registros=registros, fecha_hoy=fecha_hoy)


if __name__ == "__main__":
    app.run(debug=True)