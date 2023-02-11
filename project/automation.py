import pandas as pd
import os
import db
import requests #importando libreria requests
import datetime as d # importando libreria fecha

## FUNCION PARA INSERTAR LA DATA

def insertData():
    
    url='https://api.apis.net.pe/v1/tipo-cambio-sunat'
    r = requests.get(url)
    datos = r.json()
    compra = datos['compra']
    venta = datos['venta']
    fecha=datos['fecha']
    data=(compra,venta,fecha)
    # query y conection a bd
    query = "INSERT INTO TIPO_CAMBIO VALUES (NULL,?,?,?)"
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    cursor.execute(query,data).fetchall()
    conn.con.commit()
    print("data insertada")

##FUNCION PARA LEER LA DATA

def LeerData():
    query = "SELECT * FROM TIPO_CAMBIO"
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    tipo_cambio=cursor.execute(query).fetchall()
       
 ##dataframe
    columnas=["ID_CAMBIO","COMPRA","VENTA","FECHA"]
    df= pd.DataFrame(tipo_cambio,columns=columnas)
    print(df)
    
def ActualizarData():
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
        
    ID= int(input("ingrese el ID a actualizar: "))
    if(ID>0):
        compra = input("Ingrese el valor de compra del dolar: ")
        venta = input("Ingrese el valor de venta del dolar: ")
        
        query= "UPDATE TIPO_CAMBIO SET COMPRA =?, VENTA=? WHERE ID_CAMBIO_DOLAR=?"
        cursor.execute(query,[compra,venta,ID])
        conn.con.commit()
        print ("Data Actualizada")

message="""
    1)Insertar data:
    2)Leer los datos ingresados
    3)Actualizar data del dolar
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))

if(a==1):
    insertData()
    LeerData()
    
elif(a==2):
    LeerData()
elif(a==3):
    ActualizarData()