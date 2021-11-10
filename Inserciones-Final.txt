
INSERT INTO Deporte VALUES(00001, 'Futbol', 11);
INSERT INTO Deporte VALUES(00002, 'Futbol Sala', 5);
INSERT INTO Deporte VALUES(00003, 'Beisbol', 9);
INSERT INTO Deporte VALUES(00004, 'Badminton', 1);
INSERT INTO Deporte VALUES(00005, 'Badminton en Parejas', 2);
INSERT INTO Deporte VALUES(00006, 'Balonmano', 7);
INSERT INTO Deporte VALUES(00007, 'Baloncesto', 5);
INSERT INTO Deporte VALUES(00008, 'Esgrima', 1);
INSERT INTO Deporte VALUES(00009, 'Rugby', 15);
INSERT INTO Deporte VALUES(00010, 'Judo', 1);
INSERT INTO Deporte VALUES(00011, 'Hockey', 6);
INSERT INTO Deporte VALUES(00012, 'Raquetbol', 1);
INSERT INTO Deporte VALUES(00013, 'Raquetbol doble', 2);
INSERT INTO Deporte VALUES(00014, 'Waterpolo', 6);
INSERT INTO Deporte VALUES(00015, 'Boxeo', 1);
INSERT INTO Deporte VALUES(00016, 'Voleibol', 6);
INSERT INTO Deporte VALUES(00017, 'Ultimate', 7);
INSERT INTO Deporte VALUES(00018, 'Tennis', 1);
INSERT INTO Deporte VALUES(00019, 'Ajedrez', 1);
INSERT INTO Deporte VALUES(00020, 'Ciclo-cross', 1);


INSERT INTO TipoPersona VALUES(1, 'Administrador')
INSERT INTO TipoPersona VALUES(2, 'Comisario')


INSERT INTO Persona VALUES(0001, 001, 'Angelica', 'Perez', 'anrez1', 'aperez@correo.com', 'angel');
INSERT INTO Persona VALUES(0002, 001, 'Nicolas', 'Bermudez', 'nidez1', 'nbermudez@correo.com', 'carro');
INSERT INTO Persona VALUES(0003, 001, 'Daniel', 'Ortiz', 'datiz1', 'dortiz@correo.com', 'casa3');
INSERT INTO Persona VALUES(0004, 002, 'Carlos', 'Lopez', 'capez1', 'clopez@correo.com', 'tortu');
INSERT INTO Persona VALUES(0005, 002, 'Maria', 'Lopez', 'mapez1', 'mlopez@correo.com', 'carlo');
INSERT INTO Persona VALUES(0006, 002, 'Juan', 'Carbalo', 'jualo1', 'jcarbalo@correo.com', 'jachf');
INSERT INTO Persona VALUES(0007, 002, 'David', 'Rodriguez', 'dauez1', 'drodriguez@correo.com', 'nwncu');
INSERT INTO Persona VALUES(0008, 002, 'Sara', 'Salamanca', 'sanca1', 'ssalamanca@correo.com', 'pajar');
INSERT INTO Persona VALUES(0009, 002, 'Akcel', 'Ribon', 'akbon1', 'aribon@correo.com', 'perro');
INSERT INTO Persona VALUES(0010, 002, 'Sebastian', 'Ortiz', 'setiz1', 'sortiz@correo.com', 'celul');


INSERT INTO Sede VALUES('se001', 'Cayetano Cañisales', 55555.00, 'Calle 48 sur # 34b 67');
INSERT INTO Sede VALUES('se002', 'Leon 13', 77777.00, 'Calle 57 # 40b 7');
INSERT INTO Sede VALUES('se003', 'Polideportivo Salitre', 15479.00,'Calle 5 # 80b 4');
INSERT INTO Sede VALUES('se004', 'Polideportivo Molinos', 45781.00, 'Calle 7 # 8 79');
INSERT INTO Sede VALUES('se005', 'Complejo Acuatico Salitre', 15751.00,'Calle 7 # 8 90');
INSERT INTO Sede VALUES('se006', 'Polideportivo Tapitas', 24793.00,'Calle 72 # 79 12');
INSERT INTO Sede VALUES('se007', 'Complejo Deportivo Chapinero', 23156.00,'Calle 10 # 80 40');
INSERT INTO Sede VALUES('se008', 'CAN', 10120.00,'Calle 8 sur # 34c 90');
INSERT INTO Sede VALUES('se009', 'Life Dep', 48464, 'Calle 50 sur # 98 85');
INSERT INTO Sede VALUES('se010', 'Arena de Lucha primeros puños', 56754.00,'Calle 4 sur # 3e 85');
INSERT INTO Sede VALUES('se011', 'Maderamen Cazuca', 19181.00,'Calle 84 # 43b 67');
INSERT INTO Sede VALUES('se012', 'Cancha de Tennis Nacional', 46838.00,'Carrera 48 # 34b 67');
INSERT INTO Sede VALUES('se013', 'Pista de Hockey Albañiles', 48782.00,'Calle 2 # 30 7');
INSERT INTO Sede VALUES('se014', 'Pista de BMX', 12976.00,'Carrera 90 sur # 34b 67');
INSERT INTO Sede VALUES('se015', 'Techo', 46872.00,'Calle 30 sur # 30 67');



INSERT INTO Equipo VALUES(001, 'Balon Grande', 4);
INSERT INTO Equipo VALUES(002, 'Balon pequeño', 4);
INSERT INTO Equipo VALUES(003, 'Pelota de Beisbol', 20);
INSERT INTO Equipo VALUES(004, 'Bate de Madera', 4);
INSERT INTO Equipo VALUES(005, 'Volante', 15);
INSERT INTO Equipo VALUES(006, 'Raqueta de Malla', 8);
INSERT INTO Equipo VALUES(007, 'Baston Hockey', 30);
INSERT INTO Equipo VALUES(008, 'Disco Hockey', 30);
INSERT INTO Equipo VALUES(009, 'Porteria Hockey', 8);
INSERT INTO Equipo VALUES(010, 'Balon Rugby', 15);
INSERT INTO Equipo VALUES(011, 'Malla Tennis', 8);
INSERT INTO Equipo VALUES(012, 'Malla Voleibol', 2);
INSERT INTO Equipo VALUES(013, 'Balon Baloncesto', 6);
INSERT INTO Equipo VALUES(014, 'Mesa Ajedrez', 4);
INSERT INTO Equipo VALUES(015, 'Par Guantes Boxeo', 7);
INSERT INTO Equipo VALUES(016, 'Frisbi', 4);
INSERT INTO Equipo VALUES(017, 'Espada Esgrima', 6);
INSERT INTO Equipo VALUES(018, 'Alfombra Judo', 2);
INSERT INTO Equipo VALUES(019, 'Raqueta Raquetbol', 4);
INSERT INTO Equipo VALUES(020, 'Balon Waterpolo', 4);

INSERT INTO EquipoDeporte VALUES(001, 00001);
INSERT INTO EquipoDeporte VALUES(002, 00002);
INSERT INTO EquipoDeporte VALUES(003, 00003);
INSERT INTO EquipoDeporte VALUES(004, 00003);
INSERT INTO EquipoDeporte VALUES(005, 00004);
INSERT INTO EquipoDeporte VALUES(006, 00004);
INSERT INTO EquipoDeporte VALUES(007, 00011);
INSERT INTO EquipoDeporte VALUES(008, 00011);
INSERT INTO EquipoDeporte VALUES(009, 00011);
INSERT INTO EquipoDeporte VALUES(010, 00009);
INSERT INTO EquipoDeporte VALUES(011, 00018);
INSERT INTO EquipoDeporte VALUES(012, 00016);
INSERT INTO EquipoDeporte VALUES(013, 00007);
INSERT INTO EquipoDeporte VALUES(014, 00019);
INSERT INTO EquipoDeporte VALUES(015, 00015);
INSERT INTO EquipoDeporte VALUES(016, 00017);
INSERT INTO EquipoDeporte VALUES(017, 00008);
INSERT INTO EquipoDeporte VALUES(018, 00010);
INSERT INTO EquipoDeporte VALUES(019, 00012);
INSERT INTO EquipoDeporte VALUES(020, 00014);



INSERT INTO Estado VALUES(01, 'libre');
INSERT INTO Estado VALUES(02, 'dañado');
INSERT INTO Estado VALUES(03, 'perdido');
INSERT INTO Estado VALUES(04, 'prestado');
INSERT INTO Estado VALUES(05, 'prestamo evento');
INSERT INTO Estado VALUES(06, 'prestamo practica');


INSERT INTO Tarea VALUES(001, 'Juez');
INSERT INTO Tarea VALUES(002, 'Observador');



INSERT INTO Inventario VALUES('se001', 001, 1, 1, 4);
INSERT INTO Inventario VALUES('se001', 002, 1, 3, 4);
INSERT INTO Inventario VALUES('se003', 003, 1, 3, 20);
INSERT INTO Inventario VALUES('se003', 004, 1, 5, 4);
INSERT INTO Inventario VALUES('se003', 005, 1, 6, 15);
INSERT INTO Inventario VALUES('se003', 006, 1, 6, 8);
INSERT INTO Inventario VALUES('se004', 007, 1, 3, 30);
INSERT INTO Inventario VALUES('se004', 008, 1, 2, 30);
INSERT INTO Inventario VALUES('se004', 009, 1, 2, 8);
INSERT INTO Inventario VALUES('se004', 010, 1, 2, 15);
INSERT INTO Inventario VALUES('se004', 011, 1, 3, 8);
INSERT INTO Inventario VALUES('se005', 020, 1, 4, 4);
INSERT INTO Inventario VALUES('se005', 001, 1, 5, 4);
INSERT INTO Inventario VALUES('se005', 002, 1, 1, 4);
INSERT INTO Inventario VALUES('se006', 014, 1, 1, 4);
INSERT INTO Inventario VALUES('se006', 015, 1, 1, 7);
INSERT INTO Inventario VALUES('se007', 016, 1, 3, 4);
INSERT INTO Inventario VALUES('se007', 017, 1, 2, 6);
INSERT INTO Inventario VALUES('se008', 012, 1, 4, 2);
INSERT INTO Inventario VALUES('se008', 013, 1, 5, 6);
INSERT INTO Inventario VALUES('se008', 018, 1, 3, 2);
INSERT INTO Inventario VALUES('se008', 019, 1, 3, 4);
INSERT INTO Inventario VALUES('se009', 003, 1, 2, 20);
INSERT INTO Inventario VALUES('se009', 004, 1, 1, 4);
INSERT INTO Inventario VALUES('se009', 010, 1, 1, 15);
INSERT INTO Inventario VALUES('se010', 005, 1, 4, 15);
INSERT INTO Inventario VALUES('se010', 006, 1, 1, 8);
INSERT INTO Inventario VALUES('se010', 007, 1, 3, 30);
INSERT INTO Inventario VALUES('se010', 008, 1, 2, 30);
INSERT INTO Inventario VALUES('se010', 009, 1, 1, 8);
INSERT INTO Inventario VALUES('se012', 011, 1, 1, 8);
INSERT INTO Inventario VALUES('se011', 001, 1, 4, 4);
INSERT INTO Inventario VALUES('se013', 007, 1, 3, 20);
INSERT INTO Inventario VALUES('se013', 008, 1, 3, 50);
INSERT INTO Inventario VALUES('se013', 009, 1, 5, 4);
INSERT INTO Inventario VALUES('se015', 001, 1, 6, 20);
#Añadí más porque tocaba que todas las sedes tubieran por lo menos una cosa libre en el inventario
INSERT INTO Inventario VALUES('se001', 004, 1, 1, 4);
INSERT INTO Inventario VALUES('se001', 010, 1, 1, 4);
INSERT INTO Inventario VALUES('se003', 017, 1, 1, 20);
INSERT INTO Inventario VALUES('se003', 018, 1, 1, 4);
INSERT INTO Inventario VALUES('se003', 019, 1, 1, 15);
INSERT INTO Inventario VALUES('se003', 020, 1, 1, 8);
INSERT INTO Inventario VALUES('se004', 013, 1, 1, 30);
INSERT INTO Inventario VALUES('se004', 009, 1, 1, 30);
INSERT INTO Inventario VALUES('se004', 010, 1, 1, 8);
INSERT INTO Inventario VALUES('se004', 012, 1, 1, 15);
INSERT INTO Inventario VALUES('se004', 012, 1, 1, 8);
INSERT INTO Inventario VALUES('se005', 008, 1, 1, 4);
INSERT INTO Inventario VALUES('se005', 007, 1, 1, 4);
INSERT INTO Inventario VALUES('se005', 003, 1, 1, 4);
INSERT INTO Inventario VALUES('se006', 008, 1, 1, 4);
INSERT INTO Inventario VALUES('se006', 006, 1, 1, 7);
INSERT INTO Inventario VALUES('se007', 005, 1, 1, 4);
INSERT INTO Inventario VALUES('se007', 007, 1, 1, 6);
INSERT INTO Inventario VALUES('se008', 009, 1, 1, 2);
INSERT INTO Inventario VALUES('se008', 014, 1, 1, 6);
INSERT INTO Inventario VALUES('se008', 019, 1, 1, 2);
INSERT INTO Inventario VALUES('se008', 015, 1, 1, 4);
INSERT INTO Inventario VALUES('se009', 004, 1, 1, 20);
INSERT INTO Inventario VALUES('se009', 003, 1, 1, 4);
INSERT INTO Inventario VALUES('se009', 011, 1, 1, 15);
INSERT INTO Inventario VALUES('se010', 008, 1, 1, 15);
INSERT INTO Inventario VALUES('se010', 007, 1, 1, 8);
INSERT INTO Inventario VALUES('se010', 009, 1, 1, 30);
INSERT INTO Inventario VALUES('se010', 010, 1, 1, 30);
INSERT INTO Inventario VALUES('se010', 002, 1, 1, 8);
INSERT INTO Inventario VALUES('se012', 013, 1, 1, 8);
INSERT INTO Inventario VALUES('se011', 012, 1, 1, 4);
INSERT INTO Inventario VALUES('se013', 004, 1, 1, 20);
INSERT INTO Inventario VALUES('se013', 005, 1, 1, 50);
INSERT INTO Inventario VALUES('se013', 006, 1, 1, 4);
INSERT INTO Inventario VALUES('se015', 007, 1, 1, 20);


INSERT INTO unico VALUES('U001', 'se011', 2, 57.02);
INSERT INTO unico VALUES('U002', 'se012', 18, 78.32);
INSERT INTO unico VALUES('U003', 'se013', 11, 23.99);
INSERT INTO unico VALUES('U004', 'se014', 20, 56.29);
INSERT INTO unico VALUES('U005', 'se015', 1, 21.08)


#Tres áreas por polideportivo
INSERT INTO AREA VALUES('se001', 'A01', 'Canchas', 'Norte');
INSERT INTO AREA VALUES('se002', 'A01', 'Canchas', 'Sur');
INSERT INTO AREA VALUES('se003', 'A01', 'Canchas', 'Norte');
INSERT INTO AREA VALUES('se004', 'A01', 'Canchas', 'Norte');
INSERT INTO AREA VALUES('se005', 'A01', 'Canchas', 'Oriente');
INSERT INTO AREA VALUES('se006', 'A01', 'Canchas', 'Norte');
INSERT INTO AREA VALUES('se007', 'A01', 'Canchas', 'Sur');
INSERT INTO AREA VALUES('se008', 'A01', 'Canchas', 'Oriente');
INSERT INTO AREA VALUES('se009', 'A01', 'Canchas', 'Sur');
INSERT INTO AREA VALUES('se010', 'A01', 'Canchas', 'Occidente');
INSERT INTO AREA VALUES('se001', 'A02', 'Piscinas', 'Norte');
INSERT INTO AREA VALUES('se002', 'A02', 'Pistas', 'Sur');
INSERT INTO AREA VALUES('se003', 'A02', 'Piscinas', 'Norte');
INSERT INTO AREA VALUES('se004', 'A02', 'Pistas', 'Norte');
INSERT INTO AREA VALUES('se005', 'A02', 'Piscinas', 'Oriente');
INSERT INTO AREA VALUES('se006', 'A02', 'Piscinas', 'Norte');
INSERT INTO AREA VALUES('se007', 'A02', 'Piscinas', 'Sur');
INSERT INTO AREA VALUES('se008', 'A02', 'Pistas', 'Oriente');
INSERT INTO AREA VALUES('se009', 'A02', 'Piscinas', 'Sur');
INSERT INTO AREA VALUES('se010', 'A02', 'Piscinas', 'Occidente');
INSERT INTO AREA VALUES('se001', 'A03', 'Gimnasio', 'Occidente');
INSERT INTO AREA VALUES('se002', 'A03', 'Piscinas', 'Centro');
INSERT INTO AREA VALUES('se003', 'A03', 'Pistas', 'Centro');
INSERT INTO AREA VALUES('se004', 'A03', 'Piscinas', 'Centro');
INSERT INTO AREA VALUES('se005', 'A03', 'Gimnasio', 'Centro');
INSERT INTO AREA VALUES('se006', 'A03', 'Pistas', 'Centro');
INSERT INTO AREA VALUES('se007', 'A03', 'Pistas', 'Centro');
INSERT INTO AREA VALUES('se008', 'A03', 'Piscinas', 'Centro');
INSERT INTO AREA VALUES('se009', 'A03', 'Gimnasio', 'Centro');
INSERT INTO AREA VALUES('se010', 'A03', 'Gimnasio', 'Centro');
#Un área por "único"
INSERT INTO AREA VALUES('se011', 'A01', 'Canchas', 'Centro');
INSERT INTO AREA VALUES('se012', 'A01', 'Canchas', 'Centro');
INSERT INTO AREA VALUES('se013', 'A01', 'Pistas', 'Centro');
INSERT INTO AREA VALUES('se014', 'A01', 'Pistas', 'Centro');
INSERT INTO AREA VALUES('se015', 'A01', 'Canchas', 'Centro');


#Metimos polideportivo según los deportes que se pueden jugar en las áreas
INSERT INTO POLIDEPORTIVO VALUES('P01', 'se001', 'A01', 1);
INSERT INTO POLIDEPORTIVO VALUES('P02', 'se001', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P03', 'se002', 'A01', 6);
INSERT INTO POLIDEPORTIVO VALUES('P04', 'se002', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P05', 'se003', 'A01', 9);
INSERT INTO POLIDEPORTIVO VALUES('P06', 'se003', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P07', 'se004', 'A01', 5);
INSERT INTO POLIDEPORTIVO VALUES('P08', 'se004', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P09', 'se005', 'A01', 12);
INSERT INTO POLIDEPORTIVO VALUES('P010', 'se005', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P011', 'se006', 'A01', 18);
INSERT INTO POLIDEPORTIVO VALUES('P012', 'se006', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P013', 'se007', 'A01', 3);
INSERT INTO POLIDEPORTIVO VALUES('P014', 'se007', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P015', 'se008', 'A01', 12);
INSERT INTO POLIDEPORTIVO VALUES('P016', 'se008', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P017', 'se009', 'A01', 6);
INSERT INTO POLIDEPORTIVO VALUES('P018', 'se009', 'A02', 14);
INSERT INTO POLIDEPORTIVO VALUES('P019', 'se010', 'A01', 13);
INSERT INTO POLIDEPORTIVO VALUES('P020', 'se010', 'A02', 14);


#Metimos más polideportivos porque metí más áreas
INSERT INTO POLIDEPORTIVO VALUES('P021', 'se001', 'A03', 14);
INSERT INTO POLIDEPORTIVO VALUES('P022', 'se002', 'A03', 14);
INSERT INTO POLIDEPORTIVO VALUES('P023', 'se003', 'A03', 20);
INSERT INTO POLIDEPORTIVO VALUES('P024', 'se004', 'A03', 18);
INSERT INTO POLIDEPORTIVO VALUES('P025', 'se005', 'A03', 8);
INSERT INTO POLIDEPORTIVO VALUES('P026', 'se006', 'A03', 11);
INSERT INTO POLIDEPORTIVO VALUES('P027', 'se007', 'A03', 20);
INSERT INTO POLIDEPORTIVO VALUES('P028', 'se008', 'A03', 15);
INSERT INTO POLIDEPORTIVO VALUES('P029', 'se009', 'A03', 10);
INSERT INTO POLIDEPORTIVO VALUES('P030', 'se010', 'A03', 15);


PUNTOS 3 Y 4----------------------------------------------------------------------------------
Sentencia para llamar el login y verifica si el usuario está en la base de datos:
SELECT * FROM PERSONA WHERE IDTIPOPERSONA= 1 AND
USERPER=:userper_formulario AND PASSWORD=:password_formulario

Traer la lista de sedes para que el usuario lo seleccione:
SELECT * FROM SEDE

Traer la lista de áreas para que el usuario lo seleccione:
SELECT * FROM AREA WHERE IDCOMPLEJO =:id_complejo

Para saber qué deportes se pueden jugar en una sede, se va a polideportivo o único
según corresponda. Primero busca en el polideportivo con el complejo y el área, si
no se encuentra ahí, va a la tabla único que no requiere del área:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, POLIDEPORTIVO P WHERE P.IDCOMPLEJO =:id_complejo AND P.IDAREA
=:id_area AND D.IDDEPORTE = P.IDDEPORTE

En esta sentencia toma los deportes que se encuentran asociados a las sedes que
son “Unico”:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE =
U.IDDEPORTE

En esta sentencia toma los deportes que se encuentran asociados a las sedes que
son “Unico”:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE =
U.IDDEPORTE

En esta sentencia toma los deportes que se encuentran asociados a las sedes que
son “Unico”:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE =
U.IDDEPORTE

En esta sentencia toma los deportes que se encuentran asociados a las sedes que
son “Unico”:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE =
U.IDDEPORTE

En esta sentencia toma los deportes que se encuentran asociados a las sedes que
son “Unico”:
SELECT D.IDDEPORTE, D.NOMDEPORTE, D.NMAXINTEGRANTES FROM DEPORTE
D, UNICO U WHERE U.IDCOMPLEJO =:id_complejo AND D.IDDEPORTE =
U.IDDEPORTE

Obtiene los datos del registro de préstamo:
SELECT CONSECPRESTA, FECHAPREST FROM PRESTADO WHERE
IDESTADO=:id_estado AND CODPERSONA =: cod_persona AND IDCOMPLEJO
=: id_complejo

Actualiza el estado del Inventario:
UPDATE INVENTARIO SET IDESTADO = 4 WHERE IDCOMPLEJO =: id_complejo
AND IDEQUIPO =: id_equipo AND CONSECINVE =: consec_inve













