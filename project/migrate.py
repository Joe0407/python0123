import sqlite3

conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE USUARIOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25),
            PASSWORD VARCHAR(255) NOT NULL,
            EMAIL VARCHAR(255) NOT NULL,
            FULLNAME VARCHAR(25) NOT NULL,
            SCORE INT,
            TIPOUSUARIO VARCHAR(25)
        ); """
cursor_obj.execute(table)

## tabla productos
cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
table = """ CREATE TABLE PRODUCTOS (
            ID_PRODUCTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMEPRODUCT VARCHAR(255) NOT NULL,
            NRO_SERIE VARCHAR(250) NOT NULL,
            CATEGORIA VARCHAR(25) NOT NULL,
            STCOKACTUAL INT,
            PRICE VARCHAR(20) NOT NULL,
            CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)

## tabla venta
cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

table=""" CREATE TABLE VENTA (
            ORDERID  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT, 
            PRICETOTAL VARCHAR(25) NOT NULL,
            FOREIGN KEY(PRODUCTID) REFERENCES PRODUCTOS(ID_PRODUCTO)
        ); """

cursor_obj.execute(table)

##tabla detalle_venta
cursor_obj.execute("DROP TABLE IF EXISTS DETALLE_VENTA")

table=""" CREATE TABLE DETALLE_VENTA (
            ID_DETALLE_VENTA INTEGER PRIMARY KEY,
            VENTAID INTEGER ,
            PRODUCTID INTEGER,
            CANTIDAD_PRODUCTO INTEGER,
            FOREIGN KEY(VENTAID) REFERENCES VENTA(ORDERID),
            FOREIGN KEY(PRODUCTID) REFERENCES PRODUCTOS(ID_PRODUCTO)
        ); """
cursor_obj.execute(table)

## TABLA TIPO_CAMBIO

cursor_obj.execute(' DROP TABLE IF EXISTS TIPO_CAMBIO')


table = """
        CREATE TABLE TIPO_CAMBIO (
            ID_CAMBIO_DOLAR INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPRA VARCHAR(10),
            VENTA VARCHAR(10),
            FECHA TIMESTAMP DATE
        ); """

cursor_obj.execute(table)

conn.commit()
