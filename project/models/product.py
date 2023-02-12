import db

class ModelProducto():
    def __init__(self):
        print ('model Producto')
        self.db=db.Conection('tienda.db')
        
    def getProducto(self):
        cursor=self.db.getCursor()
        data=cursor.execute('SELECT FROM PRODUCTOS').fetchall()
        return data
    ## Insertar
    
    def InsertProducto(self,data):
        query="INSERT INTO PRODUCTOS(NAMEPRODUCT,NRO_SERIE,CATEGORIA,STCOKACTUAL,PRICE) VALUES (?,?,?,?,?)"
        cursor=self.db.getCursor()
        cursor.execute(query,data)
        self.db.con.commit()
        print('data del producto ingresado')
    