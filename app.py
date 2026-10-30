from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio_de_sesion.html')

@app.route('/pagina_principal')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/lugares')
def lugares():
    return render_template('lugares.html')

@app.route('/ubicaciones')
def ubicaciones():
    return render_template('ubicaciones.html')

@app.route('/horarios')
def horarios():
    return render_template('horarios.html')

@app.route('/resenas')
def resenas():
    return render_template('resenas.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True) 
