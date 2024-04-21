from sqlite3 import apilevel
from unittest import result
from modelo import ProductoCRUD

productoCRUD = ProductoCRUD()
opcion = -1
while opcion != 0:
  print('========= INVENTARIO DE PRODUCTOS ========')
  print('[1] Mostrar')
  print('[2] Agregar')
  print('[3] Actualizar')
  print('[4] Eliminar')
  print('[5] Buscar')
  print('[0] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    productos = productoCRUD.mostrar()
    if len(productos) == 0:
      print('No hay productos!')
    else:
      for i in productos:
        print('-'*30)
        print(f'Id: {i[0]}\nNombre: {i[1]}\nPrecio: {i[2]}\nStock: {i[3]}')

  elif opcion == 2:
    resultado = productoCRUD.agregar(
      nombre=input('Ingrese el nombre del producto: '),
      precio=float(input('Ingrese el precio: ')),
      stock=int(input('Ingrese el stock: '))
    )

    if resultado:
      print('Producto agregado!')

  elif opcion == 3:
    id = input('Ingrese el id del producto: ')
    producto = productoCRUD.existe(id)
    if producto:
      print('*** Si no desea modificar el campo solo presione enter ***')
      nombre = input(f'Ingrese el nuevo nombre({producto[1]}): ')
      precio = input(f'Igrese el nuevo precio({producto[2]}): ')
      stock = input(f'Ingrese el nuevo stock({producto[3]}): ')

      if len(nombre) == 0:
        nombre = producto[1]
      if len(precio) == 0:
        precio = producto[2]
      if len(stock) == 0:
        stock = producto[3]

      resultado = productoCRUD.actualizar(id,nombre,precio,stock)
      if resultado:
        print('Producto actualizado!')
    else:
      print('El id del producto no existe!')

  elif opcion == 4:
    id = input('Ingrese el id del producto: ')
    resultado = productoCRUD.eliminar(id)
    if resultado:
      print('Producto eliminado!')

  elif opcion == 5:
    id = input('Ingrese el id del producto: ')
    producto = productoCRUD.existe(id)
    if producto:
      print(f'Id: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nStock: {producto[3]}')
    else:
      print('El id del producto no existe!')

  elif opcion == 0:
    print('Adios!')
    
  else:
    print('Opcion incorrecta!')
