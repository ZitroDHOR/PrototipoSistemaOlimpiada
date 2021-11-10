/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     3/10/2021 7:08:03 p. m.                      */
/*==============================================================*/


alter table AREA
   drop constraint FK_AREA_SEDEAREA_SEDE;

alter table COMIDEPOR
   drop constraint FK_COMIDEPO_COMIDEPOR_PERSONA;

alter table COMIDEPOR
   drop constraint FK_COMIDEPO_COMIDEPOR_DEPORTE;

alter table COMISARIODEPORTES
   drop constraint FK_COMISARI_COMISARIO_PERSONA;

alter table COMISARIODEPORTES
   drop constraint FK_COMISARI_COMISARIO_DEPORTE2;

alter table COMISARIOEVENTO
   drop constraint FK_COMISARI_COMISARIO_PERSONA_;

alter table COMISARIOEVENTO
   drop constraint FK_COMISARI_EVENTO_EVENTO;

alter table COMISARIOEVENTO
   drop constraint FK_COMISARI_TAREA_TAREA;

alter table EQUIPODEPORTE
   drop constraint FK_EQUIPODE_EQUIPODEP_DEPORTE;

alter table EQUIPODEPORTE
   drop constraint FK_EQUIPODE_EQUIPODEP_EQUIPO;

alter table EVENTO
   drop constraint FK_EVENTO_ADMINISTR_PERSONA;

alter table EVENTO
   drop constraint FK_EVENTO_AREAEVENT_AREA;

alter table EVENTO
   drop constraint FK_EVENTO_DEPORTEEV_DEPORTE;

alter table EVENTO
   drop constraint FK_EVENTO_SEDEEVENT_SEDE;

alter table INVENTARIO
   drop constraint FK_INVENTAR_EQUIPOINV_EQUIPO;

alter table INVENTARIO
   drop constraint FK_INVENTAR_ESTADOINV_ESTADO;

alter table INVENTARIO
   drop constraint FK_INVENTAR_SEDEINVEN_SEDE;

alter table PERSONA
   drop constraint FK_PERSONA_TIPO_TIPOPERS;

alter table POLIDEPORTIVO
   drop constraint FK_POLIDEPO_AREAPOLI_AREA;

alter table POLIDEPORTIVO
   drop constraint FK_POLIDEPO_POLIDEPOR_DEPORTE;

alter table PRESTADO
   drop constraint FK_PRESTADO_ADMINISTR_PERSONA;

alter table PRESTADO
   drop constraint FK_PRESTADO_ESTADOPRE_ESTADO;

alter table PRESTADO
   drop constraint FK_PRESTADO_INVENPRES_INVENTAR;

alter table UNICO
   drop constraint FK_UNICO_DEPORTEUN_DEPORTE;

alter table UNICO
   drop constraint FK_UNICO_SEDEUNICO_SEDE;

drop index SEDEAREA_FK;

drop table AREA cascade constraints;

drop index COMIDEPOR2_FK;

drop index COMIDEPOR_FK;

drop table COMIDEPOR cascade constraints;

drop index COMISARIODEPORTES2_FK;

drop index COMISARIODEPORTES_FK;

drop table COMISARIODEPORTES cascade constraints;

drop index TAREA_FK;

drop index COMISARIO_FK;

drop index EVENTO_FK;

drop table COMISARIOEVENTO cascade constraints;

drop table DEPORTE cascade constraints;

drop table DEPORTE2 cascade constraints;

drop table EQUIPO cascade constraints;

drop index EQUIPODEPORTE2_FK;

drop index EQUIPODEPORTE_FK;

drop table EQUIPODEPORTE cascade constraints;

drop table ESTADO cascade constraints;

drop index DEPORTEEVENTO_FK;

drop index ADMINISTRADOR_FK;

drop index AREAEVENTO_FK;

drop index SEDEEVENTO_FK;

drop table EVENTO cascade constraints;

drop index ESTADOINVENTARIO_FK;

drop index EQUIPOINVENTARIO_FK;

drop index SEDEINVENTARIO_FK;

drop table INVENTARIO cascade constraints;

drop index TIPO_FK;

drop table PERSONA cascade constraints;

drop index AREAPOLI_FK;

drop index POLIDEPORTE_FK;

drop table POLIDEPORTIVO cascade constraints;

drop index ADMINISTRAPRESTA_FK;

drop index INVENPRESTAMO_FK;

drop index ESTADOPRESTAMO_FK;

drop table PRESTADO cascade constraints;

drop table SEDE cascade constraints;

drop table TAREA cascade constraints;

drop table TIPOPERSONA cascade constraints;

drop index DEPORTEUNICO_FK;

drop index SEDEUNICO_FK;

drop table UNICO cascade constraints;

/*==============================================================*/
/* Table: AREA                                                  */
/*==============================================================*/
create table AREA 
(
   IDCOMPLEJO           CHAR(5)              not null,
   IDAREA               CHAR(3)              not null,
   NOMAREA              VARCHAR2(10)         not null,
   UBICACION            VARCHAR2(30)         not null,
   constraint PK_AREA primary key (IDCOMPLEJO, IDAREA)
);

/*==============================================================*/
/* Index: SEDEAREA_FK                                           */
/*==============================================================*/
create index SEDEAREA_FK on AREA (
   IDCOMPLEJO ASC
);

/*==============================================================*/
/* Table: COMIDEPOR                                             */
/*==============================================================*/
create table COMIDEPOR 
(
   CODPERSONA           VARCHAR2(4)          not null,
   IDDEPORTE            CHAR(5)              not null,
   constraint PK_COMIDEPOR primary key (CODPERSONA, IDDEPORTE)
);

/*==============================================================*/
/* Index: COMIDEPOR_FK                                          */
/*==============================================================*/
create index COMIDEPOR_FK on COMIDEPOR (
   CODPERSONA ASC
);

/*==============================================================*/
/* Index: COMIDEPOR2_FK                                         */
/*==============================================================*/
create index COMIDEPOR2_FK on COMIDEPOR (
   IDDEPORTE ASC
);

/*==============================================================*/
/* Table: COMISARIODEPORTES                                     */
/*==============================================================*/
create table COMISARIODEPORTES 
(
   CODPERSONA           VARCHAR2(4)          not null,
   IDDEPORTE2           CHAR(5)              not null,
   constraint PK_COMISARIODEPORTES primary key (CODPERSONA, IDDEPORTE2)
);

/*==============================================================*/
/* Index: COMISARIODEPORTES_FK                                  */
/*==============================================================*/
create index COMISARIODEPORTES_FK on COMISARIODEPORTES (
   CODPERSONA ASC
);

/*==============================================================*/
/* Index: COMISARIODEPORTES2_FK                                 */
/*==============================================================*/
create index COMISARIODEPORTES2_FK on COMISARIODEPORTES (
   IDDEPORTE2 ASC
);

/*==============================================================*/
/* Table: COMISARIOEVENTO                                       */
/*==============================================================*/
create table COMISARIOEVENTO 
(
   CONSECCOMISARIO      NUMBER(3)            not null,
   CONSEC               NUMBER(5,0)          not null,
   CODPERSONA           VARCHAR2(4)          not null,
   IDTAREA              VARCHAR2(3)          not null,
   FECHA                DATE,
   constraint PK_COMISARIOEVENTO primary key (CONSECCOMISARIO)
);

/*==============================================================*/
/* Index: EVENTO_FK                                             */
/*==============================================================*/
create index EVENTO_FK on COMISARIOEVENTO (
   CONSEC ASC
);

/*==============================================================*/
/* Index: COMISARIO_FK                                          */
/*==============================================================*/
create index COMISARIO_FK on COMISARIOEVENTO (
   CODPERSONA ASC
);

/*==============================================================*/
/* Index: TAREA_FK                                              */
/*==============================================================*/
create index TAREA_FK on COMISARIOEVENTO (
   IDTAREA ASC
);

/*==============================================================*/
/* Table: DEPORTE                                               */
/*==============================================================*/
create table DEPORTE 
(
   IDDEPORTE            CHAR(5)              not null,
   NOMDEPORTE           VARCHAR2(30)         not null,
   NMAXINTEGRANTES      NUMBER(2,0)          not null,
   constraint PK_DEPORTE primary key (IDDEPORTE)
);

/*==============================================================*/
/* Table: DEPORTE2                                              */
/*==============================================================*/
create table DEPORTE2 
(
   IDDEPORTE2           CHAR(5)              not null,
   NOMDEPORTE           VARCHAR2(30)         not null,
   NMAXINTEGRANTES      NUMBER(2,0)          not null,
   constraint PK_DEPORTE2 primary key (IDDEPORTE2)
);

/*==============================================================*/
/* Table: EQUIPO                                                */
/*==============================================================*/
create table EQUIPO 
(
   IDEQUIPO             VARCHAR2(3)          not null,
   NOMEQUIPO            VARCHAR2(30)         not null,
   NPARTES              NUMBER(4,0)          not null,
   constraint PK_EQUIPO primary key (IDEQUIPO)
);

/*==============================================================*/
/* Table: EQUIPODEPORTE                                         */
/*==============================================================*/
create table EQUIPODEPORTE 
(
   IDDEPORTE            CHAR(5)              not null,
   IDEQUIPO             VARCHAR2(3)          not null,
   constraint PK_EQUIPODEPORTE primary key (IDDEPORTE, IDEQUIPO)
);

/*==============================================================*/
/* Index: EQUIPODEPORTE_FK                                      */
/*==============================================================*/
create index EQUIPODEPORTE_FK on EQUIPODEPORTE (
   IDDEPORTE ASC
);

/*==============================================================*/
/* Index: EQUIPODEPORTE2_FK                                     */
/*==============================================================*/
create index EQUIPODEPORTE2_FK on EQUIPODEPORTE (
   IDEQUIPO ASC
);

/*==============================================================*/
/* Table: ESTADO                                                */
/*==============================================================*/
create table ESTADO 
(
   IDESTADO             VARCHAR2(2)          not null,
   DESCESTADO           VARCHAR2(30)         not null,
   constraint PK_ESTADO primary key (IDESTADO)
);

/*==============================================================*/
/* Table: EVENTO                                                */
/*==============================================================*/
create table EVENTO 
(
   CONSEC               NUMBER(5,0)          not null,
   IDDEPORTE            CHAR(5)              not null,
   CODPERSONA           VARCHAR2(4)          not null,
   IDCOMPLEJO           CHAR(5)              not null,
   ARE_IDCOMPLEJO       CHAR(5),
   IDAREA               CHAR(3),
   FECHAHORA            DATE                 not null,
   DURACION             DATE                 not null,
   NPARTICIPANTE        NUMBER(3)            not null,
   constraint PK_EVENTO primary key (CONSEC)
);

/*==============================================================*/
/* Index: SEDEEVENTO_FK                                         */
/*==============================================================*/
create index SEDEEVENTO_FK on EVENTO (
   IDCOMPLEJO ASC
);

/*==============================================================*/
/* Index: AREAEVENTO_FK                                         */
/*==============================================================*/
create index AREAEVENTO_FK on EVENTO (
   ARE_IDCOMPLEJO ASC,
   IDAREA ASC
);

/*==============================================================*/
/* Index: ADMINISTRADOR_FK                                      */
/*==============================================================*/
create index ADMINISTRADOR_FK on EVENTO (
   CODPERSONA ASC
);

/*==============================================================*/
/* Index: DEPORTEEVENTO_FK                                      */
/*==============================================================*/
create index DEPORTEEVENTO_FK on EVENTO (
   IDDEPORTE ASC
);

/*==============================================================*/
/* Table: INVENTARIO                                            */
/*==============================================================*/
create table INVENTARIO 
(
   IDCOMPLEJO           CHAR(5)              not null,
   IDEQUIPO             VARCHAR2(3)          not null,
   CONSECINVE           NUMBER(4,0)          not null,
   IDESTADO             VARCHAR2(2)          not null,
   NPIEZAS              NUMBER(3,0)          not null,
   constraint PK_INVENTARIO primary key (IDCOMPLEJO, IDEQUIPO, CONSECINVE)
);

/*==============================================================*/
/* Index: SEDEINVENTARIO_FK                                     */
/*==============================================================*/
create index SEDEINVENTARIO_FK on INVENTARIO (
   IDCOMPLEJO ASC
);

/*==============================================================*/
/* Index: EQUIPOINVENTARIO_FK                                   */
/*==============================================================*/
create index EQUIPOINVENTARIO_FK on INVENTARIO (
   IDEQUIPO ASC
);

/*==============================================================*/
/* Index: ESTADOINVENTARIO_FK                                   */
/*==============================================================*/
create index ESTADOINVENTARIO_FK on INVENTARIO (
   IDESTADO ASC
);

/*==============================================================*/
/* Table: PERSONA                                               */
/*==============================================================*/
create table PERSONA 
(
   CODPERSONA           VARCHAR2(4)          not null,
   IDTIPOPERSONA        VARCHAR2(3)          not null,
   NOMPERSONA           VARCHAR2(30)         not null,
   APEPERSONA           VARCHAR2(30)         not null,
   USERPER              VARCHAR2(6)          not null,
   CORREOPER            VARCHAR2(50)         not null,
   PASSWORD             VARCHAR2(5)          not null,
   constraint PK_PERSONA primary key (CODPERSONA)
);

/*==============================================================*/
/* Index: TIPO_FK                                               */
/*==============================================================*/
create index TIPO_FK on PERSONA (
   IDTIPOPERSONA ASC
);

/*==============================================================*/
/* Table: POLIDEPORTIVO                                         */
/*==============================================================*/
create table POLIDEPORTIVO 
(
   IDPOLI               VARCHAR2(4)          not null,
   IDCOMPLEJO           CHAR(5)              not null,
   IDAREA               CHAR(3)              not null,
   IDDEPORTE            CHAR(5)              not null,
   constraint PK_POLIDEPORTIVO primary key (IDPOLI)
);

/*==============================================================*/
/* Index: POLIDEPORTE_FK                                        */
/*==============================================================*/
create index POLIDEPORTE_FK on POLIDEPORTIVO (
   IDDEPORTE ASC
);

/*==============================================================*/
/* Index: AREAPOLI_FK                                           */
/*==============================================================*/
create index AREAPOLI_FK on POLIDEPORTIVO (
   IDCOMPLEJO ASC,
   IDAREA ASC
);

/*==============================================================*/
/* Table: PRESTADO                                              */
/*==============================================================*/
create table PRESTADO 
(
   CONSECPRESTA         NUMBER(3,0)          not null,
   IDESTADO             VARCHAR2(2)          not null,
   CODPERSONA           VARCHAR2(4)          not null,
   IDCOMPLEJO           CHAR(5)              not null,
   IDEQUIPO             VARCHAR2(3)          not null,
   CONSECINVE           NUMBER(4,0)          not null,
   FECHAPREST           DATE,
   constraint PK_PRESTADO primary key (CONSECPRESTA)
);

/*==============================================================*/
/* Index: ESTADOPRESTAMO_FK                                     */
/*==============================================================*/
create index ESTADOPRESTAMO_FK on PRESTADO (
   IDESTADO ASC
);

/*==============================================================*/
/* Index: INVENPRESTAMO_FK                                      */
/*==============================================================*/
create index INVENPRESTAMO_FK on PRESTADO (
   IDCOMPLEJO ASC,
   IDEQUIPO ASC,
   CONSECINVE ASC
);

/*==============================================================*/
/* Index: ADMINISTRAPRESTA_FK                                   */
/*==============================================================*/
create index ADMINISTRAPRESTA_FK on PRESTADO (
   CODPERSONA ASC
);

/*==============================================================*/
/* Table: SEDE                                                  */
/*==============================================================*/
create table SEDE 
(
   IDCOMPLEJO           CHAR(5)              not null,
   NOMCOMPLEJO          VARCHAR2(30)         not null,
   PRESUPUESTO          NUMBER(7,2)          not null,
   DIRECCION            VARCHAR2(30)         not null,
   constraint PK_SEDE primary key (IDCOMPLEJO)
);

/*==============================================================*/
/* Table: TAREA                                                 */
/*==============================================================*/
create table TAREA 
(
   IDTAREA              VARCHAR2(3)          not null,
   DESCTAREA            VARCHAR2(20)         not null,
   constraint PK_TAREA primary key (IDTAREA)
);

/*==============================================================*/
/* Table: TIPOPERSONA                                           */
/*==============================================================*/
create table TIPOPERSONA 
(
   IDTIPOPERSONA        VARCHAR2(3)          not null,
   DESCTIPOPERSO        VARCHAR2(30)         not null,
   constraint PK_TIPOPERSONA primary key (IDTIPOPERSONA)
);

/*==============================================================*/
/* Table: UNICO                                                 */
/*==============================================================*/
create table UNICO 
(
   IDUNICO              VARCHAR2(4)          not null,
   IDCOMPLEJO           CHAR(5)              not null,
   IDDEPORTE            CHAR(5)              not null,
   AREAUNICO            NUMBER(4,2),
   constraint PK_UNICO primary key (IDUNICO)
);

/*==============================================================*/
/* Index: SEDEUNICO_FK                                          */
/*==============================================================*/
create index SEDEUNICO_FK on UNICO (
   IDCOMPLEJO ASC
);

/*==============================================================*/
/* Index: DEPORTEUNICO_FK                                       */
/*==============================================================*/
create index DEPORTEUNICO_FK on UNICO (
   IDDEPORTE ASC
);

alter table AREA
   add constraint FK_AREA_SEDEAREA_SEDE foreign key (IDCOMPLEJO)
      references SEDE (IDCOMPLEJO);

alter table COMIDEPOR
   add constraint FK_COMIDEPO_COMIDEPOR_PERSONA foreign key (CODPERSONA)
      references PERSONA (CODPERSONA);

alter table COMIDEPOR
   add constraint FK_COMIDEPO_COMIDEPOR_DEPORTE foreign key (IDDEPORTE)
      references DEPORTE (IDDEPORTE);

alter table COMISARIODEPORTES
   add constraint FK_COMISARI_COMISARIO_PERSONA foreign key (CODPERSONA)
      references PERSONA (CODPERSONA);

alter table COMISARIODEPORTES
   add constraint FK_COMISARI_COMISARIO_DEPORTE2 foreign key (IDDEPORTE2)
      references DEPORTE2 (IDDEPORTE2);

alter table COMISARIOEVENTO
   add constraint FK_COMISARI_COMISARIO_PERSONA_ foreign key (CODPERSONA)
      references PERSONA (CODPERSONA);

alter table COMISARIOEVENTO
   add constraint FK_COMISARI_EVENTO_EVENTO foreign key (CONSEC)
      references EVENTO (CONSEC);

alter table COMISARIOEVENTO
   add constraint FK_COMISARI_TAREA_TAREA foreign key (IDTAREA)
      references TAREA (IDTAREA);

alter table EQUIPODEPORTE
   add constraint FK_EQUIPODE_EQUIPODEP_DEPORTE foreign key (IDDEPORTE)
      references DEPORTE (IDDEPORTE);

alter table EQUIPODEPORTE
   add constraint FK_EQUIPODE_EQUIPODEP_EQUIPO foreign key (IDEQUIPO)
      references EQUIPO (IDEQUIPO);

alter table EVENTO
   add constraint FK_EVENTO_ADMINISTR_PERSONA foreign key (CODPERSONA)
      references PERSONA (CODPERSONA);

alter table EVENTO
   add constraint FK_EVENTO_AREAEVENT_AREA foreign key (ARE_IDCOMPLEJO, IDAREA)
      references AREA (IDCOMPLEJO, IDAREA);

alter table EVENTO
   add constraint FK_EVENTO_DEPORTEEV_DEPORTE foreign key (IDDEPORTE)
      references DEPORTE (IDDEPORTE);

alter table EVENTO
   add constraint FK_EVENTO_SEDEEVENT_SEDE foreign key (IDCOMPLEJO)
      references SEDE (IDCOMPLEJO);

alter table INVENTARIO
   add constraint FK_INVENTAR_EQUIPOINV_EQUIPO foreign key (IDEQUIPO)
      references EQUIPO (IDEQUIPO);

alter table INVENTARIO
   add constraint FK_INVENTAR_ESTADOINV_ESTADO foreign key (IDESTADO)
      references ESTADO (IDESTADO);

alter table INVENTARIO
   add constraint FK_INVENTAR_SEDEINVEN_SEDE foreign key (IDCOMPLEJO)
      references SEDE (IDCOMPLEJO);

alter table PERSONA
   add constraint FK_PERSONA_TIPO_TIPOPERS foreign key (IDTIPOPERSONA)
      references TIPOPERSONA (IDTIPOPERSONA);

alter table POLIDEPORTIVO
   add constraint FK_POLIDEPO_AREAPOLI_AREA foreign key (IDCOMPLEJO, IDAREA)
      references AREA (IDCOMPLEJO, IDAREA);

alter table POLIDEPORTIVO
   add constraint FK_POLIDEPO_POLIDEPOR_DEPORTE foreign key (IDDEPORTE)
      references DEPORTE (IDDEPORTE);

alter table PRESTADO
   add constraint FK_PRESTADO_ADMINISTR_PERSONA foreign key (CODPERSONA)
      references PERSONA (CODPERSONA);

alter table PRESTADO
   add constraint FK_PRESTADO_ESTADOPRE_ESTADO foreign key (IDESTADO)
      references ESTADO (IDESTADO);

alter table PRESTADO
   add constraint FK_PRESTADO_INVENPRES_INVENTAR foreign key (IDCOMPLEJO, IDEQUIPO, CONSECINVE)
      references INVENTARIO (IDCOMPLEJO, IDEQUIPO, CONSECINVE);

alter table UNICO
   add constraint FK_UNICO_DEPORTEUN_DEPORTE foreign key (IDDEPORTE)
      references DEPORTE (IDDEPORTE);

alter table UNICO
   add constraint FK_UNICO_SEDEUNICO_SEDE foreign key (IDCOMPLEJO)
      references SEDE (IDCOMPLEJO);

