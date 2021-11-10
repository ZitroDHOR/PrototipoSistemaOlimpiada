import cx_Oracle
from datetime import datetime
from datetime import timedelta

class Conexion: 
    

    def __init__(self):
        #Configura variables de la conexión a la bd
        self.host="localhost"
        self.user="sistema_pdb"
        self.password="clave_pdb"
        self.tnsname="BDORACLE"

    def conectar(self):
        #Crea conexión
        try:
            self.conexion=cx_Oracle.connect(self.user,self.password,self.host+"/"+self.tnsname)
        except Exception as error:
                print("No se pudo conectar a la base de datos, error: "+ error)
        else:
                print("Conexión establecida uwu")
    
    def enviar_datos(self, nombre, apellido, correo, fecha_nacimiento):
        cursor = self.conexion.cursor()
        
        #Obtiene los de la posición 0 y 2
        sub_nombre = nombre[:2].lower()
        #Obtiene los últimos tres valores de la cadena
        sub_apellido = apellido[-3:].lower()
        cliente_id = sub_nombre + sub_apellido 
        #Formateando fecha
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        fecha_nacimiento = f"{fecha_nacimiento.day}-{fecha_nacimiento.month}-{fecha_nacimiento.year}"
        
        #Añadiendo número incremental, si no hay se deja el 
        #Se saca número mayor gracias al orden
        cursor.execute("SELECT NUMERO_ID FROM CLIENTE WHERE CLIENTE_ID=:cliente_id ORDER BY NUMERO_ID DESC",{'cliente_id':cliente_id})

        array_reciente = cursor.fetchone()
        if array_reciente != None:
            #uso de .zfill para que se llenen los campos de la izquierda con los 0 que se necesiten, ejm: 001, 002... 010
            numero_id = str(int(array_reciente[0]) + 1).zfill(3)
        else:
            numero_id = '001'
        

        #Envía la sentencia
        sentencia_sql = "INSERT INTO CLIENTE (CLIENTE_ID, NOMBRE, APELLIDO, CORREO, FECHA_NACIMIENTO, NUMERO_ID) VALUES (:cliente_id, :nombre, :apellido, :correo, :fecha_nacimiento, :numero_id)"
        datos = {'cliente_id':cliente_id, 'nombre': nombre, 'apellido': apellido, 'correo': correo, 'fecha_nacimiento':fecha_nacimiento, 'numero_id':numero_id}
        cursor.execute(sentencia_sql, datos)
        
        #Sube commit y cierra cursor
        self.conexion.commit()
        
        #Se guarda el id como variable global para que se pueda llamar desde app y enviarlo al controlador del correo
        self.id_completo = cliente_id + "-" + numero_id
        cursor.close()
    
    #Función que inserta la contraseña ya cuando la persona accedió al link
    def insertar_password(self, password, id_completo):
        cursor = self.conexion.cursor()
        #Se separan las variables para hacer la revisión separada en la base de datos
        cliente_id = id_completo.split('-')[0]
        numero_id = id_completo.split('-')[1]
        sentencia_sql = "UPDATE CLIENTE SET CONTRASENA =:password WHERE CLIENTE_ID=:cliente_id AND NUMERO_ID=:numero_id"
        datos = {'password':password, 'cliente_id':cliente_id, 'numero_id':numero_id}
        cursor.execute(sentencia_sql, datos)
        self.conexion.commit()
        cursor.close()

    #Variable para enviarse por correo
    def get_id_completo(self):
        return self.id_completo

    def cerrar_bd(self):
        #Cierra conexión con base de datos
        self.conexion.close()
    
    def verifica_usuario_password(self, userper_formulario,password_formulario):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM PERSONA WHERE IDTIPOPERSONA= 1 AND USERPER=:userper_formulario AND PASSWORD=:password_formulario",{'userper_formulario':userper_formulario, 'password_formulario': password_formulario})
        registro = cursor.fetchone()
        cursor.close()
        if not(registro is None):
            self.persona = registro    
            
            return True
        else:
            return False
        
    
    def get_persona(self):
        return self.persona

    def lista_sedes(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM SEDE")
        registro = cursor.fetchall()
        cursor.close()
        return registro
    
    def lista_areas(self, id_complejo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM AREA WHERE IDCOMPLEJO =:id_complejo",{'id_complejo':id_complejo})
        registro = cursor.fetchall()
        cursor.close()
        return registro

    #Para saber qué deportes se pueden jugar en una sede, se va a polideportivo o único según corresponda
    #Primero busca en el polideportivo con el complejo y el área, si no se encuentra ahí, va a la tabla único que no requiere del área
    def lista_deportes(self, id_complejo, id_area):
        cursor = self.conexion.cursor()
        #Hace un where para sacar los deportes que se encuentran en el polideportivo
        cursor.execute("SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE D, POLIDEPORTIVO P WHERE P.IDCOMPLEJO =:id_complejo AND P.IDAREA =:id_area AND D.IDDEPORTE = P.IDDEPORTE",{'id_complejo':id_complejo, 'id_area':id_area})
        registro = cursor.fetchall()
 
        
        #No sirve el is None porque al hacer fetchall, se crea la tupla igual, aunque esté vacía
        if len(registro) == 0:
            #Hace un where para sacar los deportes que se encuentran en unico
            cursor.execute("SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE = U.IDDEPORTE",{'id_complejo':id_complejo})
            registro = cursor.fetchall()
        
        cursor.close()
        return registro
    
    #Hace un where entre los id de la sede, el inventario y el equipo para sacar el nombre de los equipos que están en la sede
    #IDESTADO es 1 porque solo se busca los que tengan estado libre
    def lista_equipos(self, id_complejo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT E.IDEQUIPO, E.NOMEQUIPO, E.NPARTES, I.IDESTADO FROM EQUIPO E, INVENTARIO I, SEDE S WHERE I.IDESTADO=1 AND S.IDCOMPLEJO=:id_complejo AND S.IDCOMPLEJO = I.IDCOMPLEJO AND I.IDEQUIPO = E.IDEQUIPO",{'id_complejo':id_complejo})
        registro = cursor.fetchall()
        cursor.close()
        return registro
    
    def get_sede(self, id_complejo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM SEDE WHERE IDCOMPLEJO =:id_complejo",{'id_complejo':id_complejo})
        registro = cursor.fetchone() #Solo trae a uno
        cursor.close()
        return registro
    
    def get_area(self, id_complejo, id_area):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM AREA WHERE IDCOMPLEJO =:id_complejo AND IDAREA =:id_area",{'id_complejo':id_complejo, 'id_area':id_area})
        registro = cursor.fetchone() #Solo trae a uno
        cursor.close()
        return registro
    
    def get_deporte(self, id_deporte):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM DEPORTE WHERE IDDEPORTE =:id_deporte",{'id_deporte':id_deporte})
        registro = cursor.fetchone() #Solo trae a uno
        cursor.close()
        return registro


    def get_equipo(self, id_complejo, id_equipo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT E.IDEQUIPO, E.NOMEQUIPO, I.IDESTADO, I.CONSECINVE FROM EQUIPO E, INVENTARIO I, SEDE S WHERE S.IDCOMPLEJO =: id_complejo AND S.IDCOMPLEJO = I.IDCOMPLEJO AND I.IDEQUIPO = E.IDEQUIPO AND E.IDEQUIPO =: id_equipo",{'id_complejo':id_complejo,'id_equipo':id_equipo})
        registro = cursor.fetchone() #Solo trae a uno
        cursor.close()
        return registro
    
    def get_estado(self, id_estado):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTADO WHERE IDESTADO =:id_estado",{'id_estado':id_estado})
        registro = cursor.fetchone() #Solo trae a uno
        cursor.close()
        return registro

    def registrar_evento(self, id_deporte, id_complejo, id_area, cod_persona, fecha, hora, duracion, nparticipante):
        
        #Se formatea correctamente la fecha y hora
        print(fecha)
        print(hora)
        print(duracion)

        fecha_hora = f"{fecha} {hora}"
        print(fecha_hora)
        
        #Seteando la duración, se mostrará la hora de salida del evento, entonces se suman los minutos que ingresó el usuario
        hora_salida = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M') +timedelta(minutes=int(duracion))
        hora_salida = f"{hora_salida.year}-{hora_salida.month}-{hora_salida.day} {hora_salida.hour}:{hora_salida.minute}"
        print(hora_salida)
    

        
        cursor = self.conexion.cursor()
        print(id_deporte)
        print(id_complejo)
        print(id_area)
        print(cod_persona)
        #En are_idcomplejo se mete el mismo id complejo
        cursor.execute("INSERT INTO EVENTO (IDDEPORTE, IDCOMPLEJO, ARE_IDCOMPLEJO, IDAREA, CODPERSONA, FECHAHORA, DURACION, NPARTICIPANTE) VALUES (:id_deporte, :id_complejo, :id_complejo, :id_area, :cod_persona, to_date(:fecha_hora, 'yyyy-mm-dd HH24:MI'), to_date(:hora_salida, 'yyyy-mm-dd HH24:MI'), :nparticipante)"
        ,{'id_deporte':id_deporte, 'id_complejo':id_complejo, 'id_area':id_area, 'cod_persona':cod_persona, 'fecha_hora':fecha_hora, 'hora_salida':hora_salida, 'nparticipante':nparticipante})
        self.conexion.commit()

        cursor.execute("SELECT CONSEC FROM EVENTO WHERE IDDEPORTE=:id_deporte AND IDCOMPLEJO=:id_complejo AND CODPERSONA=:cod_persona AND FECHAHORA = to_date(:fecha_hora, 'yyyy-mm-dd:HH24:MI')", {'id_deporte':id_deporte,'id_complejo':id_complejo, 'cod_persona':cod_persona,'fecha_hora':fecha_hora})
        consecutivo = cursor.fetchone()[0]
        cursor.close()

        #No se devuelve el nombre de la persona porque ya está en la coockie de la sesión
        registro_recibo = [consecutivo, self.get_sede(id_complejo)[1], self.get_area(id_complejo, id_area)[2], fecha_hora, hora_salida, nparticipante]
        self.registro_recibo = registro_recibo

    def get_registro_recibo(self):
        return self.registro_recibo

    
    def registrar_prestamo(self, tipo_prestamo, cod_persona, id_complejo, consec_inve, id_equipo):
        
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO PRESTADO VALUES(NULL, :id_estado, :cod_persona, :id_complejo, :id_equipo, :consec_inve, sysdate)"
        ,{'id_estado':tipo_prestamo, 'cod_persona': cod_persona, 'id_complejo':id_complejo, 'id_equipo': id_equipo, 'consec_inve':consec_inve})
        self.conexion.commit()

        cursor.execute("SELECT CONSECPRESTA, FECHAPREST FROM PRESTADO WHERE IDESTADO=:id_estado AND CODPERSONA =: cod_persona AND IDCOMPLEJO =: id_complejo", {'id_estado':tipo_prestamo, 'cod_persona':cod_persona,'id_complejo':id_complejo})
        #Se trae el consecutivo y la fecha que quedó registrada por la base de datos
        registro = cursor.fetchone()
        consecutivo = registro[0]
        fecha_prest = registro[1]
        #Trae el nombre del estado a partir del id traido desde el formulario
        nom_prestamo = self.get_estado(tipo_prestamo)[1]
        #No se devuelve el nombre de la persona porque ya está en la coockie de la sesión
        prestamo_recibo = [consecutivo,nom_prestamo, self.get_sede(id_complejo)[1],self.get_equipo(id_complejo,id_equipo)[1],consec_inve, fecha_prest]
        self.prestamo_recibo = prestamo_recibo
        cursor.close()
    
    def get_prestamo_recibo(self):
        return self.prestamo_recibo
    
    #Realiza un update para cambiar el idestado del inventario que se está pidiendo prestado
    def actualiza_estado_prestamo_inventario(self, id_complejo, id_equipo, consec_inve):
        cursor = self.conexion.cursor()
        #IDESTADO = 4 PARA QUE QUEDE PRESTADO
        cursor.execute("UPDATE INVENTARIO SET IDESTADO = 4 WHERE IDCOMPLEJO =: id_complejo AND IDEQUIPO =: id_equipo AND CONSECINVE =: consec_inve"
        ,{'id_complejo':id_complejo, 'id_equipo': id_equipo, 'consec_inve':consec_inve})
        self.conexion.commit()
        cursor.close()
    
    

        
