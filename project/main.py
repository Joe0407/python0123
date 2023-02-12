import controller as ctr

message="""
    1)Insertar un usuario y listar Usuarios
    2)Actualizar Usuario
    3)Eliminar Usuario
    """  
print(message) 

global option
option=input('ingrese una opcion: ')

def registerUser():
    usuario=input('ingrese el siguiente data usuario: ')
    password=input('ingrese el siguiente data password: ')
    email=input('ingrese el siguiente data email: ')
    fullname=input('ingrese el siguiente data fullname: ')
    tipousuario=input('ingrese el siguiente data tipousuario: ')
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)
def listUser():
    data=ctr.controllerUser()
    for row in data:
        print(row)
        
        
 ##Actualizar Usuario
def ActualizarUsuario():
    ID = int(input("Ingresar codigo de usuario: ")) 
    usuario=input('ingrese el nombre de usuario: ')
    password=input('ingrese el  data password: ')
    email=input('ingrese el data email: ')
    fullname=input('ingrese el data fullname: ')
    score=int(input('ingrese el score: '))
    tipousuario=input('ingrese el  data tipousuario: ')
    data=(usuario,password,email,fullname,score,tipousuario,ID)
    try:
        ctr.UpdateUser(data)
    except Exception as e:
        print('error en el codigo')
        print(e)
    
##Eliminar Usuario

def EliminarUsuario():
    ID=int(input('Ingrese el codigo de usuario a eliminar: '))
    data=(ID,)
    try:
        ctr.DeleteUser(data)
    except Exception as e:
        print ('Error al intentar eliminar al usuario')
        print(e)
        
## https://es.stackoverflow.com/questions/363669/valueerror-parameters-are-of-unsupported-type-python      
        

if __name__=='__main__':   
  
 
    if option=='1':
        registerUser()
        listUser()
    if option=='2':
        ActualizarUsuario()
    if option=='3':
        EliminarUsuario()

