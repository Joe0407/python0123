import models.product as md

def controllerProducto():
    producto=md.ModelProducto()
    data=producto.getProducto()
    return data

def InsertProducto(data):
    producto=md.ModelProducto()
    producto.InsertProducto(data)
 