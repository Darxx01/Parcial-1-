import sqlite3

class ProductoCRUD(object):
  """
  Clase para realizar las operaciones CRUD sobre la tabla producto
  La tabla palabra esta compuesta por id,nombre,precio,stock
  """
  def __init__(self) -> None:
    """
    Conexion autmatica a la base de datos
    """
    self.conexion = sqlite3.connect("inventario.db")
    self.cursor = self.conexion.cursor()
  
  def mostrar(self):
    try:
      self.cursor.execute('select * from producto')
      return self.cursor.fetchall()
    except Exception as error:
      print(error)
      return []

  def agregar(self, nombre, precio, stock):
    try:
      self.cursor.execute(f"insert into producto(nombre,precio,stock) values('{nombre}',{precio},{stock})")
      self.conexion.commit()
      return True
    except Exception as error:
      print(error)
      return False
  
  def actualizar(self, id, nombre,precio,stock):
    try:
      self.cursor.execute(f"update producto set nombre='{nombre}',precio={precio},stock={stock} where id={id}")
      self.conexion.commit()
      return True
    except Exception as error:
      print(error)
      return False

  def eliminar(self, id):
    try:
      if(self.existe(id)):
        self.cursor.execute(f"delete from producto where id={id}")
        self.conexion.commit()
        return True
      print('Error: El id del producto no existe!')
      return False
    except Exception as error:
      print(error)
      return False

  def existe(self, id):
    try:
      self.cursor.execute(f"select * from producto where id={id}")
      return self.cursor.fetchone()
    except:
      return None
