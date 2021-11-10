from flask import Flask, render_template, request
from Controlador_bd import Conexion
from Controlador_correo import Correo


app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('login.html')


@app.route('/registro', methods=['POST'])
def registro():
    if request.method=='POST':
        #Conexión a la base de datos
        bd = Conexion()
        bd.conectar()

        #Trae datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        correo = request.form['correo']
        
        #Mete datos a la bd
        bd.enviar_datos(nombre,apellido,correo,fecha_nacimiento)
        
        #Envía correo
        cc = Correo()
        cc.enviar_correo(correo, bd.get_id_completo())

        #Cierra base de datos
        bd.cerrar_bd()

    return render_template('respuesta_registro.html')

@app.route('/confirmacion/<usuario>/')
def confirmacion(usuario):
    #Se recibe el link con el dato usuario
    return render_template('confirma_registro.html', user_id=usuario)

@app.route('/ingresa_password', methods=['POST'])
def ingresa_password():
    if request.method=='POST':
    #Conexión a la base de datos
        bd = Conexion()
        bd.conectar()
        password = request.form['password']
        id_completo = request.form['id_completo']
        print(id_completo)
        print(password)
        bd.insertar_password(password, id_completo)
    return render_template('respuesta_confirmacion.html')
    
if __name__ == '__main__':
    app.run(port = 3000 ,debug = True)

