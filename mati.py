import mysql.connector
conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="prueba")
cursor=conexion.cursor()

##creacion de la tabla categoria
cursor.execute("CREATE TABLE IF NOT EXISTS categoria (id INT PRIMARY KEY,descripcion VARCHAR(255) NOT NULL) ")
##insert de la tabla categoria
cursor.execute("insert ignore into categoria values (1,'libros')")
cursor.execute("insert ignore into categoria values (2,'revistas')")
cursor.execute("insert ignore into categoria values (3,'enciclopedias')")
conexion.commit()

#creacion de la tabla producto
cursor.execute("create table if not exists producto (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,id_categoria integer not null,nombre varchar(255),descripcion varchar(255),editorial varchar(255),autores varchar(255) ); ")

conexion.commit()
#relacion entre producto y categoria
cursor.execute("alter table producto add constraint foreign key (id_categoria) references categoria (id)")
conexion.commit()

#insert de la tabla producto
cursor.execute("insert ignore into producto values (1,1,'papelucho','libro infantil','editorial 1','marcela pas')")
cursor.execute("insert ignore into producto values (2,2,'natura','revista principalmente enfocada a mujeres ','editorial 1','desconocido')")
cursor.execute("insert ignore into producto values (3,3,'enciclopedia de la ciencia animal','enciclopedia de ejemplo de animales','editorial 2','multiples autores')")
conexion.commit()


def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Que desea hacer? : "))
            correcto=True

        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1.Menu producto")
    print ("2.Menu bodega ")
    print ("3.Menu editorial")
    print ("4.Menu autores")
    print ("5. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        atras=False
        while not atras:
            print ("1. listar productos")
            print ("2. añadir producto");
            print ("5. atras")
            opcionp=pedirNumeroEntero()
            if opcionp ==1:
                cursor.execute("select * from producto")
                print("la lista de los productos:  " )
                for fila in cursor:
                    print("ID = ", fila[0])
                    print("Nombre = ", fila[2])
                    print("Descripcion  = ", fila[3])
                    print("Editorial  = ", fila[4])
                    print("Autor  = ", fila[5], "\n")
                    print ("el numero de producto es de :", cursor.rowcount)
            elif opcion ==2:
                sql = (
                    "insert into producto(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
                    "VALUES (%s, %s, %s, %s, %s)")
                print ("los datos")
            elif opcionp ==5:
                atras=True
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
conexion.close()


