from sqlite3 import Cursor
import mysql.connector
import os
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")
conexion=mysql.connector.connect(host="localhost",      ##url de la base de datos
                                  user="root",          #usuario de la base de datos   
                                  passwd="",            # contraseña de la base de datos
                                  database="prueba")    #!importante tienes que tener una base de datos que se llame prueba
cursor=conexion.cursor()

##roles para login

cursor.execute("create table if not exists roles (id int not null auto_increment primary key,descripcion varchar(255) not null); ")
cursor.execute ("insert ignore into roles values (1,'administrador')")
cursor.execute ("insert ignore into roles values (2,'bodeguero')")
conexion.commit()

##login 
cursor.execute("create table if not exists usuario (id int not null auto_increment primary key,id_rol int not null,nombre_usuario varchar(255) not null,clave varchar(255) not null)")
cursor.execute("insert ignore into usuario values (1,1,'admin','admin')")
conexion.commit()
 
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

#insert de la tabla producto
cursor.execute("insert ignore into producto values (1,1,'papelucho','libro infantil','editorial 1','marcela pas')")
cursor.execute("insert ignore into producto values (2,2,'natura','revista principalmente enfocada a mujeres ','editorial 1','desconocido')")
cursor.execute("insert ignore into producto values (3,3,'enciclopedia de la ciencia animal','enciclopedia de ejemplo de animales','editorial 2','multiples autores')")
conexion.commit()


##creacion de la tabla bodega
cursor.execute("create table if not exists bodega (id int not null auto_increment primary key,nombre varchar(255) not null,direccion varchar(255))")
cursor.execute("insert ignore into bodega values (1,'bodega 1','tongoy')")
cursor.execute("insert ignore into bodega values (2,'bodega santiago ','calle morande')")

conexion.commit()

cursor.execute("create table if not exists editorial (id int not null auto_increment primary key,nombre varchar(255) not null)")
cursor.execute("insert ignore into editorial values(1,'editorial sexto piso')")
cursor.execute("insert ignore into editorial values(2,'Editorial Errata Naturae')")
conexion.commit()


#relaciones
cursor.execute("alter table producto add constraint foreign key (id_categoria) references categoria (id)")
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

login=False
while not login: # <-------------- funcion de login 
    clear()
    print ("ingrese nombre de usuario")
    usuario =input()
    clear()
    print("ingrese contraseña")
    passwd=input()
    consulta ="select count(*) from usuario where nombre_usuario=%s and clave=%s"
    datos=(usuario,passwd)
    try:
        cursor.execute(consulta, datos)
        resultado=cursor.fetchone()
        if resultado[0]!=0:
            login=True
        else:
            clear()
            input("Usuario no encontrado precione enter para reintentar \n")

    except:
        print ("error en la consulta. reintentando...")

salir = False
opcion = 0
 
while not salir:
    clear()
    print ("1.Menu producto")
    print ("2.Menu bodega ")
    print ("3.Menu editorial")
    print ("4.Menu autores")
    print ("5. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1: # <----------------- menu producto
        atras=False
        clear()
        while not atras:
            print ("1. listar productos")
            print ("2. añadir producto")
            print ("3. eliminar producto")
            print ("5. atras")
            opcionp=pedirNumeroEntero()
            if opcionp ==1: # <----------- listar producto
                cursor.execute("select * from producto")
                print("la lista de los productos:  " )
                for fila in cursor:
                    print("ID = ", fila[0])
                    print("Nombre = ", fila[2])
                    print("Descripcion  = ", fila[3])
                    print("Editorial  = ", fila[4])
                    print("Autor  = ", fila[5], "\n")
                    print ("el numero de producto es de :", cursor.rowcount)



            elif opcionp ==2: # <--------- ingresar producto
                sql = (
                    "insert into producto(id_categoria,nombre,descripcion,editorial,autores)"
                    "VALUES (%s, %s, %s, %s, %s)")
                cursor.execute("select * from categoria ")
                print ("categorias existentes")
                for fila in cursor:
                    print ("ID = ",fila[0], " nombre: ",fila[1])
                print("Ingrese el id de la categoria del producto")
                id_cat=int (input())
                print("ingrese el nombre del producto: \n")
                nombre_prod=input()
                print("ingrese descripcion del producto: \n")
                descripcion_prod=input()
                print ("ingrese editorial del producto: \n")
                editorial_prod=input()
                print("ingrese el o los autores del producto: \n")
                autores_prod=input()
                datos = (id_cat,nombre_prod,descripcion_prod,editorial_prod,autores_prod)
                
                try:
                    cursor.execute(sql, datos)
                    conexion.commit()
                except:
                    conexion.rollback()
                print ("datos guardatos exitosamente")
            elif opcionp ==5:
                atras=True


    elif opcion == 2: # <----------- menu bodega
        atras = False
        clear()  
        while not atras:
            print ("1. listar bodegas")
            print ("2. añadir bodega")
            print ("3. eliminar bodega")
            print ("5. atras")
            opcionb=pedirNumeroEntero()
            if opcionb == 1: # <---- en el caso de buscar bodegas 
                clear()
                cursor.execute("select * from bodega")
                for fila in cursor:
                    print("ID = ", fila[0])
                    print("Nombre = ", fila[1])
                    print("Direccion = ", fila[2])
                    print ("el numero de producto es de :", cursor.rowcount ,"\n")
                input("precione enter para continuar..")

            elif opcionb==2: # <--- en el caso de añadir bodega
                clear()
                print ("Ingrese el nombre de la bodega")
                nombre_bodega = input()
                print ("Ingrese direccion de la bodega")
                direccion_bodega = input()
                consulta="insert into bodega (nombre,direccion) values (%s,%s)"
                datos=(nombre_bodega,direccion_bodega)
                try:
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    print ("datos de bodega guardatos exitosamente")

                except:
                    print("error al ingresar los datos de bodega")
                    conexion.rollback()


            elif opcionb == 5:
                atras=True

    elif opcion == 3: #<------------ menu editorial
        atras=False
        clear()
        while not atras:
            print ("1. listar editoriales ")
            print ("2. añadir editoriales ")
            print ("3. eliminar editoriales ")
            print ("5. atras \n")
            opcione=pedirNumeroEntero()

            if opcione==1: #<-------- listar editoriales
                clear()
                cursor.execute("select * from editorial")
                for fila in cursor:
                    print ("ID =", fila[0])
                    print ("Nombre =", fila[1])
                input("precione enter para continuar..")
                clear()
            elif opcione ==2:# <------- añadir editoriales 
                clear()
                print ("ingrese nombre de editorial")
                nombre_editorial=input()
                print(nombre_editorial)
                consulta="insert into editorial values (null,%s)"    
                try:
                    cursor.execute(consulta, nombre_editorial)
                    conexion.commit()
                    print ("datos de editorial guardatos exitosamente")

                except:
                    print("error al ingresar los datos de la editorial")
                    conexion.rollback()
            elif opcione==5:
                atras=True

    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
clear()
conexion.close()


