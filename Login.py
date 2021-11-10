from flask import Flask, render_template, request, session, redirect, url_for
from Controlador_bd import Conexion


app = Flask(__name__)
app.secret_key = 'my_secret_key' #Necesaria para el uso de cookies, dato para encriptar


@app.route('/')
def Index():
    if 'persona_sesion' in session:
        session.pop('persona_sesion')#Elimina las cookies de la sesión
    return render_template('login.html')

@app.route('/solicita_ingreso', methods=['POST'])
def solicita_ingreso():
    if request.method == 'POST':
        bd = Conexion()
        bd.conectar()

        userper_formulario=request.form.get("userper")
        password_formulario=request.form.get("password")
        
        #Halla el registro en el que el usuario y la contraseña coincidan
        sesion = bd.verifica_usuario_password(userper_formulario,password_formulario)
        bd.cerrar_bd()

        if sesion:
            session['persona_sesion'] = bd.get_persona()
            return redirect(url_for('evento_inicio'))
        else:
            return redirect(url_for('Index'))#Busca la url de la función ingreso, no del html

@app.route('/evento_inicio', methods=['GET'])
def evento_inicio():
    bd = Conexion()
    bd.conectar()
    lista_sedes = bd.lista_sedes()
    bd.cerrar_bd()
    return render_template('evento_inicio.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], lista_sedes = lista_sedes, sede_boolean = False, area_boolean = False, deporte_boolean = False)

@app.route('/registra_sede', methods=['GET', 'POST'])
def registra_sede():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    lista_areas = bd.lista_areas(sede_seleccionada)
    #Como se guardó el id de la sede, se trae toda la sede para imprimirla en el html
    info_sede = bd.get_sede(sede_seleccionada)
    bd.cerrar_bd()
    return render_template('evento_inicio.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], sede = info_sede,  sede_boolean = True, area_boolean = False, deporte_boolean = False, lista_areas = lista_areas)
    

@app.route('/registra_area', methods=['GET', 'POST'])
def registra_area():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    area_seleccionada = request.form.get("area")
    
    lista_deportes = bd.lista_deportes(sede_seleccionada, area_seleccionada)
    #Como se guardó el id de la sede, se trae toda la sede para imprimirla en el html
    info_sede = bd.get_sede(sede_seleccionada)
    info_area = bd.get_area(sede_seleccionada, area_seleccionada)
    bd.cerrar_bd()
    return render_template('evento_inicio.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], sede = info_sede,  area = info_area, sede_boolean = True, area_boolean = True, deporte_boolean = False, lista_deportes = lista_deportes)

@app.route('/registra_deporte', methods=['GET', 'POST'])
def registra_deporte():
    #Aquí se verifica no se necesita listar nada, solo se envían valores booleanos para que el html muestre para meter los campos que no se consultan en la BD
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    area_seleccionada = request.form.get("area")
    deporte_seleccionado = request.form.get("deporte")
    
    info_sede = bd.get_sede(sede_seleccionada)
    info_area = bd.get_area(sede_seleccionada, area_seleccionada)
    info_deporte = bd.get_deporte(deporte_seleccionado)
    bd.cerrar_bd()
    return render_template('evento_inicio.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], sede = info_sede,  area = info_area, deporte = info_deporte, sede_boolean = True, area_boolean = True, deporte_boolean = True)

@app.route('/registra_evento', methods=['GET', 'POST'])
def registra_evento():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    area_seleccionada = request.form.get("area")
    deporte_seleccionado = request.form.get("deporte")
    cod_persona = session['persona_sesion'][0]
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")
    duracion = request.form.get("duracion")
    nparticipante = request.form.get("nparticipante")


    bd.registrar_evento(deporte_seleccionado,sede_seleccionada,area_seleccionada,cod_persona, fecha, hora, duracion, nparticipante)
    
    bd.cerrar_bd()
    return render_template('evento_registrado.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], registro_recibo = bd.get_registro_recibo())


@app.route('/prestamo_inicio')
def prestamo_inicio():
    bd = Conexion()
    bd.conectar()
    lista_sedes = bd.lista_sedes()
    bd.cerrar_bd()
    return render_template('prestamo_inicio.html', lista_sedes = lista_sedes, sede_boolean = False, equipo_boolean = False)


@app.route('/prestamo_sede', methods=['POST'])
def prestamo_sede():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    lista_equipos = bd.lista_equipos(sede_seleccionada)
    #Como se guardó el id de la sede, se trae toda la sede para imprimirla en el html
    info_sede = bd.get_sede(sede_seleccionada)
    bd.cerrar_bd()
    return render_template('prestamo_inicio.html', sede = info_sede,  sede_boolean = True, equipo_boolean = False, lista_equipos = lista_equipos)

#No lista nada porque ya se saben los tipos de préstamo
@app.route('/prestamo_equipo', methods=['POST'])
def prestamo_equipo():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    equipo_seleccionado = request.form.get("equipo")
    #Como se guardó el id de la sede, se trae toda la sede para imprimirla en el html
    info_sede = bd.get_sede(sede_seleccionada)
    info_equipo = bd.get_equipo(sede_seleccionada, equipo_seleccionado)
    bd.cerrar_bd()
    return render_template('prestamo_inicio.html', sede = info_sede, equipo = info_equipo,  sede_boolean = True, equipo_boolean = True)

@app.route('/registra_prestamo', methods=['POST'])
def registra_prestamo():
    bd = Conexion()
    bd.conectar()
    sede_seleccionada = request.form.get("sede")
    equipo_seleccionado = request.form.get("equipo")
    tipo_prestamo = request.form.get("tipo_prestamo")
    #Como se guardó el id de la sede, se trae toda la sede para imprimirla en el html
    registro_equipo = bd.get_equipo(sede_seleccionada,equipo_seleccionado)
    id_equipo = registro_equipo[0]
    consec_inve = registro_equipo[3]

    #Actualiza el estado del inventario a prestado
    bd.actualiza_estado_prestamo_inventario(sede_seleccionada,equipo_seleccionado,consec_inve)
    
    bd.registrar_prestamo(tipo_prestamo,session['persona_sesion'][0],sede_seleccionada, consec_inve,id_equipo)
    bd.cerrar_bd()


    return render_template('prestamo_registrado.html', nombre = session['persona_sesion'][2], apellido = session['persona_sesion'][3], prestamo_recibo = bd.get_prestamo_recibo())


@app.route('/logout')
def logout():
    if 'persona_sesion' in session:
        session.pop('persona_sesion')#Elimina las cookies de la sesión
    return redirect(url_for('Index'))#Busca la url de la función ingreso, no del html


if __name__ == '__main__':
    app.run(port = 3000 ,debug = True)

