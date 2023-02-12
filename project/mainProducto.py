import controller as ctr

message="""
    1)Ingresar data del producto y listar Producto
    2)Actualizar Usuario
    3)Eliminar Usuario
    """  
print(message) 

global option
option=input('ingrese una opcion: ')

##Ingresar Producto

def IngresarProducto():
    Nombre_producto=input('Ingrese el nombre del producto: ')
    Nro_Serie=input('Ingrese el numero de serie del producto: ')
    Categoria=input('Ingrese la categoria: ')
    Stck_Actual=int(input('Ingrese el stock: '))
    price=input('Ingrese el precio unitario: ')
    data=(Nombre_producto,Nro_Serie,Categoria,Stck_Actual,price)
    
    try:
        ctr.InsertProducto(data)
    except Exception as e:
        print('error al ingresar la data del producto')
        print(e)

def listarProducto():
    data=ctr.controllerProducto()
    for row in data:
        print(row)



if __name__=='__main__':
    if option=='1':
        IngresarProducto()
        listarProducto()