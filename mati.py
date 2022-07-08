import mysql.connector
conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="mati")
cursor=conexion.cursor()
cursor.execute("CREATE TABLE categoria (id INTEGER PRIMARY KEY,descripcion VARCHAR(255) NOT NULL) ")
# cursor.execute("select * from cargos")
# for fila in cursor:
#     print(fila)
conexion.close()
