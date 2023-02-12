import db

class ModelUser():
    def __init__(self):
        print('model user')
        self.db=db.Conection('tienda.db')
    def getUser(self):
        cursor=self.db.getCursor()
        data=cursor.execute('select * from USUARIOS').fetchall()
        return data
    def insertUser(self,data):
        inserSentence="INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES(?,?,?,?,0,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()
        print('data insertada')
        
    ## actualizar y eliminar
    
    #ACTUALIZAR
    
    def UpdateUser(self,data):
        query="UPDATE USUARIOS SET USUARIO=?,PASSWORD=?,EMAIL=?,SCORE=?,FULLNAME=?,TIPOUSUARIO=? WHERE ID=?"
        cursor=self.db.getCursor()
        cursor.execute(query,data)
        self.db.con.commit()
        print('data actualizada')
    
    ##ELIMINAR
    
    def DeleteUser(self,data):
        query="DELETE FROM USUARIOS WHERE ID=?"
        cursor=self.db.getCursor()
        cursor.execute(query,data)
        self.db.con.commit()
        print('data eliminada')

