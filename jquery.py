#Se importa las librerias Flask y render template
from cgitb import text
from dataclasses import dataclass
from email import message
from email.mime import application
from logging import root
from tkinter import messagebox
from turtle import position
from urllib import response
from wsgiref.util import request_uri
from flask import Flask, redirect, render_template, request, url_for, Response, jsonify
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
'''
El primer argumento es el nombre del módulo o paquete de la aplicación. __name__ es un atajo 
conveniente para esto que es apropiado para la mayoría de los casos. Esto es necesario para 
que Flask sepa dónde buscar recursos como plantillas y archivos estáticos.
'''
app = Flask(__name__) 

#Gestion de coneccion a base de datos mongodb
MONGOHOST = "localhost"
MONGOPORT = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGOHOST + ":" + MONGOPORT + "/"

MONGO_BASEDATOS = "JuegoAhorcado"
MONGO_COLLECTION1 = "Ciclo"
MONGO_COLLECTION2 = "Permisos"
MONGO_COLLECTION3 = "Roles"
MONGO_COLLECTION4 = "Usuarios"
MONGO_COLLECTION5 = "Materias"
MONGO_COLLECTION6 = "Evaluaciones"
MONGO_COLLECTION7 = "Cursos"
MONGO_COLLECTION8 = "Obtenido"
MONGO_COLLECTION9 = "Valoraciones"
MONGO_COLLECTION10 = "Puntuaciones"

cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_BASEDATOS]
coleccion1 = baseDatos[MONGO_COLLECTION1]
coleccion2 = baseDatos[MONGO_COLLECTION2]
coleccion3 = baseDatos[MONGO_COLLECTION3]
coleccion4 = baseDatos[MONGO_COLLECTION4]
coleccion5 = baseDatos[MONGO_COLLECTION5]
coleccion6 = baseDatos[MONGO_COLLECTION6]
coleccion7 = baseDatos[MONGO_COLLECTION7]
coleccion8 = baseDatos[MONGO_COLLECTION8]
coleccion9 = baseDatos[MONGO_COLLECTION9]
coleccion10 = baseDatos[MONGO_COLLECTION10]


print(baseDatos.list_collection_names())


'''
    Decorador para decirle a Flask qué URL debe activar nuestra función.
'''
ciclo = baseDatos[MONGO_COLLECTION1]
permisos = baseDatos[MONGO_COLLECTION2]
roles = baseDatos[MONGO_COLLECTION3]
usuarios = baseDatos[MONGO_COLLECTION4]
materias = baseDatos[MONGO_COLLECTION5]
evaluaciones = baseDatos[MONGO_COLLECTION6]
cursos = baseDatos[MONGO_COLLECTION7]
obtenido = baseDatos[MONGO_COLLECTION8]
valoraciones = baseDatos[MONGO_COLLECTION9]
puntuaciones = baseDatos[MONGO_COLLECTION10]

#decorador para la pagina de inicio
@app.route('/')
#Se crea la función para determinada acción -> Game página principal
def loginGame():
    usuarioResivido = usuarios.find({"rol":"Estudiante", "estado":"Activo"})
    return render_template('loginGame.html', usuarios = usuarioResivido)

#Decorador para la pagina de administrador
@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

#Decorador para la pagina de evaluaciones
@app.route('/evaluacionGame')
def evaluacionGame():
    marteriaE = obtenido.find()
    usuarioE = obtenido.find()
    cursoE = obtenido.find()
    selectoN = obtenido.find()
    usuarioX = obtenido.find()
    return render_template('evaluacionGame.html', usuario = usuarioE, nombre = selectoN, materia = marteriaE, curso = cursoE, usuarioy = usuarioX)

#Decorador para la pagina del juego
@app.route('/game')
def game():
    marteriaE = obtenido.distinct("materia")
    usuarioE = obtenido.distinct("usuario")
    cursoE = obtenido.distinct("curso")
    selectoN = obtenido.find()
    return render_template('game.html', usuario = usuarioE, nombre = selectoN, materia = marteriaE, curso = cursoE)

#Registros
@app.route('/registroUsuario')
def registroUsuario():
    usuarioResivido = usuarios.find()
    rolF = roles.distinct("rol")
    materiaF = materias.distinct("nombre")
    cursoF = cursos.find()
    return render_template('formularios/registroUsuario.html', usuarios = usuarioResivido, rol = rolF, materia = materiaF, curso = cursoF)

@app.route('/registroAcademico')
def registroAcademico():
    cursoresivido = cursos.find()
    materiaResivido = materias.find()
    cicloResivido = ciclo.find()
    cicloCurso = ciclo.find({"estado":"Activo"})
    usuariosNombres = usuarios.find({"rol":"Docente"})
    usuariosTutor = usuarios.find({"rol":"Docente"})
    return render_template('formularios/registroAcademico.html', ciclos = cicloResivido, nombresD = usuariosNombres, cicloC = cicloCurso, materia = materiaResivido, cursoM = cursoresivido, tutorU = usuariosTutor)

@app.route('/registroPermisos')
def registroPermisos():
    listPermisos = permisos.distinct("nombre")
    materiaResivido = materias.find()
    cicloResivido = ciclo.find()
    cicloMateria = ciclo.find({"estado":"Activo"})
    usuariosNombres = usuarios.find({"rol":"Docente"})
    return render_template('formularios/registroPermisos.html', ciclos = cicloResivido, nombresD = usuariosNombres, cicloM = cicloMateria, materia = materiaResivido, permisosL = listPermisos)


#Listas
@app.route('/registrosUsuarios')
def registrosUsuarios():
    usuarioEstudiante = usuarios.find({"rol":"Estudiante", "estado":"Activo"})
    usuarioAdministradores = usuarios.find({"rol":"Administrador", "estado":"Activo"})
    usuarioDocentes = usuarios.find({"rol":"Docente", "estado":"Activo"})
    return render_template('listas/registrosUsuarios.html', estudiantes = usuarioEstudiante, administradores = usuarioAdministradores, docentes = usuarioDocentes)

@app.route('/asignacionesAcademicas')
def asignacionesAcademicas():
    ciclos = ciclo.find()
    materia = materias.find()
    curso = cursos.find()
    return render_template('listas/asignacionesAcademicas.html',ciclosT = ciclos, materiasT = materia, cursosT = curso)

@app.route('/asignacionesPermisos')
def asignacionesPermisos():
    permiso = permisos.find()
    rol = roles.find()
    return render_template('listas/asignacionesPermisos.html',permisoL = permiso, rolL = rol)

#Editables
@app.route('/gestionUsuarios')
def gestionUsuarios():
    rolesL = roles.distinct("rol")
    materiaL = materias.distinct("nombre")
    usuarioEstudiante = usuarios.find({"rol":"Estudiante"})
    usuarioAdministradores = usuarios.find({"rol":"Administrador"})
    usuarioDocentes = usuarios.find({"rol":"Docente"})
    cursoF = materias.distinct("curso")
    return render_template('gestiones/gestionUsuarios.html', estudiantes = usuarioEstudiante, administradores = usuarioAdministradores, docentes = usuarioDocentes, materia = materiaL, roles = rolesL, curso = cursoF)

@app.route('/gestionAcademica')
def gestionAcademica():
    materiaResivido = materias.find()
    cicloResivido = ciclo.find()
    cursoResivido = cursos.find()
    ciclosCodigo = ciclo.distinct("codigo")
    cicloMateria = ciclo.find({"estado":"Activo"})
    usuariosNombres = usuarios.find({"rol":"Docente"})
    return render_template('gestiones/gestionAcademica.html', ciclos = cicloResivido, nombresD = usuariosNombres, cicloM = cicloMateria, materia = materiaResivido, curso = cursoResivido, codigo = ciclosCodigo)

@app.route('/gestionPermisos')
def gestionPermisos():
    permiso = permisos.find()
    rol = roles.find()
    permisosx = permisos.distinct("nombre")
    return render_template('gestiones/gestionPermisos.html',permisosE = permiso, rolesE = rol, permisoL = permisosx)

#Errores de datos
@app.route('/errorUsuario')
def errorUsuario():
    return render_template('errores/errorUsuario.html')

@app.route('/errorCorreo')
def errorCorreo():
    return render_template('errores/errorCorreo.html')

@app.route('/errorCedula')
def errorCedula():
    return render_template('errores/errorCedula.html')

@app.route('/errorUsuarioDuplicado')
def errorUsuarioDuplicado():
    return render_template('errores/errorUsuarioDuplicado.html')

@app.route('/errorCicloActivo')
def errorCicloActivo():
    return render_template('errores/errorCicloActivo.html')

@app.route('/errorCodigoExiste')
def errorCodigoExiste():
    return render_template('errores/errorCodigoExiste.html')

@app.route('/errorCursoAsignado')
def errorCursoAsignado():
    return render_template('errores/errorCursoAsignado.html')

@app.route('/errorDocenteExiste')
def errorDocenteExiste():
    return render_template('errores/errorDocenteExiste.html')

@app.route('/errorNRCExiste')
def errorNRCExiste():
    return render_template('errores/errorNRCExiste.html')

@app.route('/errorPermisoExiste')
def errorPermisoExiste():
    return render_template('errores/errorPermisoExiste.html')

@app.route('/errorRolExiste')
def errorRolExiste():
    return render_template('errores/errorRolExiste.html')

#Correcto de datos
@app.route('/correctoCiclo')
def correctoCiclo():
    return render_template('correcto/correctoCiclo.html')

@app.route('/correctoCurso')
def correctoCurso():
    return render_template('correcto/correctoCurso.html')

@app.route('/correctoMateria')
def correctoMateria():
    return render_template('correcto/correctoMateria.html')

@app.route('/correctoPermiso')
def correctoPermiso():
    return render_template('correcto/correctoPermiso.html')

@app.route('/correctoRol')
def correctoRol():
    return render_template('correcto/correctoRol.html')

@app.route('/correctoUsuario')
def correctoUsuario():
    return render_template('correcto/correctoUsuario.html')

@app.route('/correctoAdministrador')
def correctoAdministrador():
    return render_template('correcto/correctoAdministrador.html')

@app.route('/correctoDocente')
def correctoDocente():
    return render_template('correcto/correctoDocente.html')

@app.route('/correctoDocenteAlert')
def correctoDocenteAlert():
    return render_template('correcto/correctoDocenteAlert.html')

#Otros
@app.route('/valoracion')
def valoracion():
    usuarioE = obtenido.find()
    return render_template('otros/valoracion.html', usuariox = usuarioE)

@app.route('/informeValoraciones')
def informeValoraciones():
    valoracionesL = valoraciones.find()
    return render_template('otros/informeValoraciones.html', valoracion = valoracionesL)

#DOCENTE
@app.route('/docente')
def docente():
    return render_template('DOCENTE/docente.html')

@app.route('/registroAlumno')
def registroAlumno():
    usuarioEstudiante = usuarios.find({"rol":"Estudiante", "estado":"Activo"})
    return render_template('DOCENTE/registroAlumno.html', estudiantes = usuarioEstudiante)

@app.route('/notas')
def notas():
    puntuacionesE = puntuaciones.find()
    return render_template('DOCENTE/notas.html', puntuacion = puntuacionesE)


#==============================================================================================================================
#REGISTRO USUARIOS
#==============================================================================================================================

#Ingreso datos Usuario
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarUsuario', methods =["GET", "POST"])
#Crea la funcion para el ingreso del Usuario
def registrarUsuario():

    if request.method == 'POST':
        U_nombreUser =request.form.get('U_nombreUser')          #Llama la variable del furmulario
        U_nombre =request.form.get('U_nombre')                  #Llama la variable del furmulario
        U_apellido = request.form.get('U_apellido')             #Llama la variable del furmulario
        U_cedula = request.form.get('U_cedula')                 #Llama la variable del furmulario
        U_correo = request.form.get('U_correo')                 #Llama la variable del furmulario
        U_materia =request.form.get('U_materia')                #Llama la variable del furmulario
        U_curso =request.form.get('U_curso')                    #Llama la variable del furmulario
        U_rol = request.form.get('U_rol')                       #Llama la variable del furmulario
        U_foto =request.form.get('U_foto')                      #Llama la variable del furmulario


        user = usuarios.distinct("usuario")
        identificacion = usuarios.distinct("cedula")
        correo = usuarios.distinct("correo")

        if (U_nombreUser not in user):
            if (U_correo not in correo):

                if (U_rol == "Administrador"):
                    dict = {          
                        "usuario": U_nombreUser,                                  
                        "nombre": "",                                   #Asigna variable al diccionario
                        "apellido": "",                                 #Asigna variable al diccionario
                        "cedula": "",                                   #Asigna variable al diccionario
                        "correo": U_correo,                             #Asigna variable al diccionario
                        "materia": "",
                        "curso" : "",
                        "rol": U_rol,                                    #Asigna variable al diccionario
                        "foto" : "",
                        "estado" : "Activo"
                    }
                    insertar = coleccion4.insert_one(dict)                
                    print(insertar.inserted_id)                      
                    return redirect(url_for('correctoUsuario'))         #MENSAJE (USUARIO REGISTRADO)                       
                else:
                    if (U_cedula not in identificacion):
                        if (U_rol == "Estudiante"):
                            dict = {          
                                "usuario": U_nombreUser,                                  
                                "nombre": U_nombre,                             #Asigna variable al diccionario
                                "apellido": U_apellido,                         #Asigna variable al diccionario
                                "cedula": U_cedula,                             #Asigna variable al diccionario
                                "correo": U_correo,                             #Asigna variable al diccionario
                                "materia": U_materia,
                                "curso" : U_curso,
                                "rol": U_rol,                                    #Asigna variable al diccionario
                                "foto" : U_foto,
                                "estado" : "Activo"
                                }
                            insertar = coleccion4.insert_one(dict)                       
                            print(insertar.inserted_id)                      
                            return redirect(url_for('correctoUsuario'))         #MENSAJE (USUARIO REGISTRADO)
                        else: 
                            if (U_rol == "Docente"):
                                dict = {          
                                    "usuario": U_nombreUser,                                  
                                    "nombre": U_nombre,                             #Asigna variable al diccionario
                                    "apellido": U_apellido,                         #Asigna variable al diccionario
                                    "cedula": U_cedula,                             #Asigna variable al diccionario
                                    "correo": U_correo,                             #Asigna variable al diccionario

                                    "materia": U_materia,
                                    "curso" : U_curso,
                                    "rol": U_rol,                                    #Asigna variable al diccionario
                                    "foto" : "",
                                    "estado" : "Activo"
                                    }
                                insertar = coleccion4.insert_one(dict)                          
                                print(insertar.inserted_id)                         
                                return redirect(url_for('correctoUsuario'))         #MENSAJE (USUARIO REGISTRADO)
                    else:
                        return redirect(url_for('errorCedula'))
            else:
                return redirect(url_for('errorCorreo'))
        else:
            return redirect(url_for('errorUsuarioDuplicado'))
    else:
        return notFound()

#Metodo para eliminar (registro Usuario)
@app.route('/delete/<string:id_usuario>')
#Crea la funcion para el ingreso de eliminar
def eliminar(id_usuario):
    usuario = baseDatos[MONGO_COLLECTION4]
    usuario.delete_one({"_id" : ObjectId(id_usuario)})
    return redirect(url_for('gestionUsuarios'))

#Metodo para eliminar (registros Usuarios)
@app.route('/deleteRU/<string:id_usuario>')
#Crea la funcion para el ingreso de eliminar
def eliminarRU(id_usuario):
    usuario = baseDatos[MONGO_COLLECTION4]
    usuario.delete_one({"_id" : ObjectId(id_usuario)})
    return redirect(url_for('registrosUsuarios'))

#Metodo para modificar datos
@app.route('/edit/<string:id_usuario>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del usuario
def editar(id_usuario):
    editar = baseDatos[MONGO_COLLECTION4]
    U_id = request.form.get('U_id')                             #Llama la variable del furmulario
    U_nombreUser =request.form.get('U_nombreUser')                      #Llama la variable del furmulario
    U_nombre =request.form.get('U_nombre')                      #Llama la variable del furmulario
    U_apellido = request.form.get('U_apellido')                 #Llama la variable del furmulario
    U_cedula = request.form.get('U_cedula')                     #Llama la variable del furmulario
    U_correo = request.form.get('U_correo')                     #Llama la variable del furmulario
    U_contrasenia = request.form.get('U_contrasenia')           #Llama la variable del furmulario
    U_materia =request.form.get('U_materia')
    U_curso =request.form.get('U_curso')
    U_rol = request.form.get('U_rol')                           #Llama la variable del furmulario
    U_foto =request.form.get('U_foto')
    U_estado =request.form.get('U_estado')

    if (U_materia == None):
            U_materia = "No asignado"
    
    if (U_curso == None):
            U_curso = "No asignado"

    if (U_foto == None):
            U_foto = ""
    

    dict = { 
            "usuario": U_nombreUser,
            "nombre": U_nombre,                             #Asigna variable al diccionario
            "apellido": U_apellido,                         #Asigna variable al diccionario
            "cedula": U_cedula,                             #Asigna variable al diccionario
            "correo": U_correo,                             #Asigna variable al diccionario
            "contrasenia": U_contrasenia,                 #Asigna variable al diccionario
            "materia": U_materia,
            "curso": U_curso,
            "rol": U_rol,                                    #Asigna variable al diccionario
            "foto": U_foto, 
            "estado": U_estado
        }    

    editar.update_one({'_id' : ObjectId(id_usuario)}, {'$set' : dict})
    return redirect(url_for('gestionUsuarios'))



#==============================================================================================================================
#REGISTRO ACADEMICO

#==============================================================================================================================
#REGISTRO CICLO

#Ingreso datos ciclo
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarCiclo', methods =["GET", "POST"])
#Crea la funcion para el ingreso del Ciclo
def registrarCiclo():

    if request.method == 'POST':
        A_codigo =request.form.get('A_codigo')                      #Llama la variable del furmulario
        A_periodo = request.form.get('A_periodo')                   #Llama la variable del furmulario
        A_informacion = request.form.get('A_informacion')           #Llama la variable del furmulario
        A_estado = request.form.get('A_estado')                     #Llama la variable del furmulario

        ciclosE = ciclo.distinct("estado")
        est1 = "Activo"
        est2 = "Inactivo"
        ciclos = ciclo.distinct("codigo")

        if (A_codigo not in ciclos):
            if (A_estado == est1):
                if (est1 not in ciclosE):
                    dict = { 
                                "codigo": A_codigo,                                 #Asigna variable al diccionario
                                "periodo": A_periodo,                               #Asigna variable al diccionario
                                "informacion": A_informacion,                       #Asigna variable al diccionario
                                "estado": "Activo",                                 #Asigna variable al diccionario
                                }
                    insertarC = coleccion1.insert_one(dict)                          
                    print(insertarC.inserted_id)   
                    return redirect(url_for('correctoCiclo'))
                else:
                    if (est1 in ciclosE): 
                        return redirect(url_for('errorCicloActivo'))       #VENTANA (SOLO PUEDE EXISTIR UN CICLO ACTIVO)             
            else:
                if (A_estado == est2):
                    dict = { 
                                "codigo": A_codigo,                                 #Asigna variable al diccionario
                                "periodo": A_periodo,                               #Asigna variable al diccionario
                                "informacion": A_informacion,                       #Asigna variable al diccionario
                                "estado": A_estado,                                 #Asigna variable al diccionario
                                }
                    insertarC = coleccion1.insert_one(dict)                   
                    print(insertarC.inserted_id)   
                    return redirect(url_for('correctoCiclo'))

        else:
            return redirect(url_for('errorCodigoExiste'))                   #VENTANA (YA EXISTE EL CODIGO)
               
    else:
        return notFound()

    
#Metodo para eliminar (registro ciclo)
@app.route('/deleteRC/<string:id_ciclo>')
#Crea la funcion para el ingreso de eliminar
def eliminarRC(id_ciclo):
    ciclo = baseDatos[MONGO_COLLECTION1]
    ciclo.delete_one({"_id" : ObjectId(id_ciclo)})
    return redirect(url_for('asignacionesAcademicas'))

#Metodo para eliminar (registro ciclo)
@app.route('/deleteRCA/<string:id_ciclo>')
#Crea la funcion para el ingreso de eliminar
def eliminarRCA(id_ciclo):
    ciclo = baseDatos[MONGO_COLLECTION1]
    ciclo.delete_one({"_id" : ObjectId(id_ciclo)})
    return redirect(url_for('gestionAcademica'))

#Metodo para modificar datos
@app.route('/editCA/<string:id_ciclo>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del ciclo
def editarCA(id_ciclo):
    editarCA = baseDatos[MONGO_COLLECTION1]
    A_id = request.form.get('A_id')                             #Llama la variable del furmulario
    A_codigo =request.form.get('A_codigo')                      #Llama la variable del furmulario
    A_periodo = request.form.get('A_periodo')                   #Llama la variable del furmulario
    A_informacion = request.form.get('A_informacion')           #Llama la variable del furmulario
    A_estado = request.form.get('A_estado')                     #Llama la variable del furmulario

    if (A_estado == ""):
        dict = { 
            "codigo": A_codigo,                                 #Asigna variable al diccionario
            "periodo": A_periodo,                               #Asigna variable al diccionario
            "informacion": A_informacion                        #Asigna variable al diccionario
            }
    else: 
        dict = { 
                "codigo": A_codigo,                                 #Asigna variable al diccionario
                "periodo": A_periodo,                               #Asigna variable al diccionario
                "informacion": A_informacion,                       #Asigna variable al diccionario
                "estado": A_estado                                  #Asigna variable al diccionario
                }
            
    editarCA.update_one({'_id' : ObjectId(id_ciclo)}, {'$set' : dict})
    return redirect(url_for('gestionAcademica'))


#==============================================================================================================================
#REGISTRO CURSO

#Ingreso datos cursos
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarCurso', methods =["GET", "POST"])
def registrarCurso():

    if request.method == 'POST':
        A_nivel =request.form.get('A_nivel')                        #Llama la variable del furmulario
        A_curso = request.form.get('A_curso')                       #Llama la variable del furmulario
        A_tutor = request.form.get('A_tutor')                       #Llama la variable del furmulario
        C_cicloA = request.form.get('C_cicloA')                     #Llama la variable del furmulario
    
        curso = cursos.distinct("curso", {"ciclo":request.form.get('C_cicloA')})
        tutor = cursos.distinct("tutor")
        if (A_curso not in curso):
            if (A_tutor not in tutor):
                dict = { 
                    "nivel": A_nivel,                               #Asigna variable al diccionario
                    "curso": A_curso,                               #Asigna variable al diccionario
                    "tutor": A_tutor,                               #Asigna variable al diccionario
                    "ciclo": C_cicloA,                              #Asigna variable al diccionario
                }
                insertarC = coleccion7.insert_one(dict)                         
                print(insertarC.inserted_id)   
                return redirect(url_for('correctoCurso'))    #VENTANA (CURSO REGISTRADO)
            else:
                return redirect(url_for('errorDocenteExiste'))     #VENTANA (EL DOCENTE YA ES TUTOR DEL CURSO)
        else:
            return redirect(url_for('errorCursoAsignado'))         #VENTANA (YA EXISTE UN CURSO ASIGNADO A ESE CICLO)
    else:
        return notFound()


#Metodo para eliminar (registro curso)
@app.route('/deleteRCC/<string:id_curso>')
#Crea la funcion para el ingreso de eliminar
def eliminarRCC(id_curso):
    curso = baseDatos[MONGO_COLLECTION7]
    curso.delete_one({"_id" : ObjectId(id_curso)})
    return redirect(url_for('asignacionesAcademicas'))

#Metodo para eliminar (registro curso)
@app.route('/deleteRCCA/<string:id_curso>')
#Crea la funcion para el ingreso de eliminar
def eliminarRCCA(id_curso):
    curso = baseDatos[MONGO_COLLECTION7]
    curso.delete_one({"_id" : ObjectId(id_curso)})
    return redirect(url_for('gestionAcademica'))


#Metodo para modificar datos
@app.route('/editCCA/<string:id_curso>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del ciclo
def editarCCA(id_curso):
    editarCur = baseDatos[MONGO_COLLECTION7]
    M_id = request.form.get('A_id')                             #Llama la variable del furmulario
    A_nivel = request.form.get('A_nivel')                      #Llama la variable del furmulario
    A_curso = request.form.get('A_curso')                   #Llama la variable del furmulario
    A_tutor = request.form.get('A_tutor')           #Llama la variable del furmulario
    C_cicloA = request.form.get('C_cicloA')                     #Llama la variable del furmulario


    dict = { 
            "nivel": A_nivel,                                 #Asigna variable al diccionario
            "curso": A_curso,                               #Asigna variable al diccionario
            "tutor": A_tutor,                       #Asigna variable al diccionario
            "ciclo": C_cicloA                                  #Asigna variable al diccionario
            }
            
    editarCur.update_one({'_id' : ObjectId(id_curso)}, {'$set' : dict})
    return redirect(url_for('gestionAcademica'))

#==============================================================================================================================
#REGISTRO MATERIA

#Ingreso datos materia
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarMateria', methods =["GET", "POST"])
def registrarMateria():

    if request.method == 'POST':
        M_nrc =request.form.get('M_nrc')                            #Llama la variable del furmulario
        M_nombre = request.form.get('M_nombre')                     #Llama la variable del furmulario
        M_docente = request.form.get('M_docente')                   #Llama la variable del furmulario
        M_curso = request.form.get('M_curso')                 #Llama la variable del furmulario
        
        if (M_curso == ""):
            M_curso = "No asignado"

        nrc = materias.distinct("nrc")

        if (M_nrc not in nrc):
            dict = { 
                    "nrc": M_nrc,                                 #Asigna variable al diccionario
                    "nombre": M_nombre,                               #Asigna variable al diccionario
                    "docente": M_docente,                       #Asigna variable al diccionario
                    "curso": M_curso,                                 #Asigna variable al diccionario
                    }
            insertarM = coleccion5.insert_one(dict)                              
            print(insertarM.inserted_id)   
            return redirect(url_for('correctoMateria'))      #VENTANA (MATERIA REGISTRADA)        
        else:
            return redirect(url_for('errorNRCExiste'))      #VENTANA (EL NRC YA SE ENCUENTRA REGISTRADO)
    else:
        return notFound()




#Metodo para eliminar (registro materia)
@app.route('/deleteRM/<string:id_materia>')
#Crea la funcion para el ingreso de eliminar
def eliminarRM(id_materia):
    materia = baseDatos[MONGO_COLLECTION5]
    materia.delete_one({"_id" : ObjectId(id_materia)})
    return redirect(url_for('asignacionesAcademicas'))

#Metodo para eliminar (registro materia)
@app.route('/deleteRMA/<string:id_materia>')
#Crea la funcion para el ingreso de eliminar
def eliminarRMA(id_materia):
    materia = baseDatos[MONGO_COLLECTION5]
    materia.delete_one({"_id" : ObjectId(id_materia)})
    return redirect(url_for('gestionAcademica'))


#Metodo para modificar datos
@app.route('/editMA/<string:id_materia>', methods =["GET", "POST"])
#Crea la funcion para la modificacion de materia
def editarMA(id_materia):
    editarMAT = baseDatos[MONGO_COLLECTION5]
    M_id = request.form.get('M_id')                             #Llama la variable del furmulario
    M_nrc = request.form.get('M_nrc')                      #Llama la variable del furmulario
    M_nombre = request.form.get('M_nombre')                   #Llama la variable del furmulario
    M_docente = request.form.get('M_docente')           #Llama la variable del furmulario
    M_curso = request.form.get('M_curso')                     #Llama la variable del furmulario

    dict = { 
            "nrc": M_nrc,                                 #Asigna variable al diccionario
            "nombre": M_nombre,                               #Asigna variable al diccionario
            "docente": M_docente,                       #Asigna variable al diccionario
            "curso": M_curso                                  #Asigna variable al diccionario
            }
            
    editarMAT.update_one({'_id' : ObjectId(id_materia)}, {'$set' : dict})
    return redirect(url_for('gestionAcademica'))


#==============================================================================================================================
#Registro Permisos

#==============================================================================================================================
#REGISTRO ROL

#Ingreso datos rol
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarRol', methods =["GET", "POST"])
#Crea la funcion para el ingreso del rol
def registrarRol():

    if request.method == 'POST':
        P_rol =request.form.get('P_rol')                      #Llama la variable del furmulario
        P_permisoR = request.form.get('P_permisoR')                   #Llama la variable del furmulario
        P_descripcionR = request.form.get('P_descripcionR')           #Llama la variable del furmulario
        
        rol = roles.distinct("rol")
        if (P_rol not in rol):

            dict = { 
                    "rol": P_rol,                                 #Asigna variable al diccionario
                    "permiso": P_permisoR,                               #Asigna variable al diccionario
                    "descripcion": P_descripcionR,                       #Asigna variable al diccionario
                    }

            insertarR = coleccion3.insert_one(dict)                        
            print(insertarR.inserted_id)   
            return redirect(url_for('correctoRol'))     #VENTANA (ROL REGISTRADO)        
        else:
            return redirect(url_for('errorRolExiste'))         #VENTANA (EL ROL YA ESTA REGISTRADO)
    else:
        return notFound()


#Metodo para eliminar (registro rol)
@app.route('/deleteRR/<string:id_rol>')
#Crea la funcion para el ingreso de eliminar
def eliminarRR(id_rol):
    rol = baseDatos[MONGO_COLLECTION3]
    rol.delete_one({"_id" : ObjectId(id_rol)})
    return redirect(url_for('asignacionesPermisos'))


#Metodo para eliminar (registro rol)
@app.route('/deleteRRE/<string:id_rol>')
#Crea la funcion para el ingreso de eliminar
def eliminarRRE(id_rol):
    rol = baseDatos[MONGO_COLLECTION3]
    rol.delete_one({"_id" : ObjectId(id_rol)})
    return redirect(url_for('gestionPermisos'))


#Metodo para modificar datos
@app.route('/editRE/<string:id_rol>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del ciclo
def editarRE(id_rol):
    editarRE = baseDatos[MONGO_COLLECTION3]
    P_id = request.form.get('P_id')                             #Llama la variable del furmulario
    R_rol = request.form.get('R_rol')                      #Llama la variable del furmulario
    R_permiso = request.form.get('R_permiso')                   #Llama la variable del furmulario
    R_descripcion = request.form.get('R_descripcion')           #Llama la variable del furmulario

    dict = { 
            "rol": R_rol,                                 #Asigna variable al diccionario
            "permiso": R_permiso,                               #Asigna variable al diccionario
            "descipcion": R_descripcion                                  #Asigna variable al diccionario
            }
            
    editarRE.update_one({'_id' : ObjectId(id_rol)}, {'$set' : dict})
    return redirect(url_for('gestionPermisos'))


#==============================================================================================================================
#REGISTRO PERMISO

#Ingreso datos permiso
#Controlador de la ruta para ingresar los datos del formulario
@app.route('/registrarPermiso', methods =["GET", "POST"])
#Crea la funcion para el ingreso del permiso
def registrarPermiso():

    if request.method == 'POST':
        P_nombre =request.form.get('P_nombre')                      #Llama la variable del furmulario
        P_permiso = request.form.get('P_permiso')                   #Llama la variable del furmulario
        P_descripcion = request.form.get('P_descripcion')           #Llama la variable del furmulario
        
        permiso = permisos.distinct("nombre")
        if (P_nombre not in permiso):
            dict = { 
                    "nombre": P_nombre,                                 #Asigna variable al diccionario
                    "permiso": P_permiso,                               #Asigna variable al diccionario
                    "descripcion": P_descripcion,                       #Asigna variable al diccionario
                    }

            insertarP = coleccion2.insert_one(dict)                  
            print(insertarP.inserted_id)   
            return redirect(url_for('correctoPermiso'))    #VENTANA (PERMISO REGISTRADO)
        else:
            return redirect(url_for('errorPermisoExiste')) #VENTANA (EL NOMBRE DEL PERMISO YA EXISTE)
    else:
        return notFound()


#Metodo para eliminar (registro permiso)
@app.route('/deleteRP/<string:id_permiso>')
#Crea la funcion para el ingreso de eliminar
def eliminarRP(id_permiso):
    permiso = baseDatos[MONGO_COLLECTION2]
    permiso.delete_one({"_id" : ObjectId(id_permiso)})
    return redirect(url_for('asignacionesPermisos'))

#Metodo para eliminar (registro permiso)
@app.route('/deleteRPE/<string:id_permiso>')
#Crea la funcion para el ingreso de eliminar
def eliminarRPE(id_permiso):
    permiso = baseDatos[MONGO_COLLECTION2]
    permiso.delete_one({"_id" : ObjectId(id_permiso)})
    return redirect(url_for('gestionPermisos'))


#Metodo para modificar datos
@app.route('/editPE/<string:id_permiso>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del permiso
def editarPE(id_permiso):
    editarPE = baseDatos[MONGO_COLLECTION2]
    P_id = request.form.get('P_id')                             #Llama la variable del furmulario
    P_nombre = request.form.get('P_nombre')                      #Llama la variable del furmulario
    P_permiso = request.form.get('P_permiso')                   #Llama la variable del furmulario
    P_descripcion = request.form.get('P_descripcion')           #Llama la variable del furmulario

    dict = { 
            "nombre": P_nombre,                                 #Asigna variable al diccionario
            "permiso": P_permiso,                               #Asigna variable al diccionario
            "descipcion": P_descripcion                                  #Asigna variable al diccionario
            }
            
    editarPE.update_one({'_id' : ObjectId(id_permiso)}, {'$set' : dict})
    return redirect(url_for('gestionPermisos'))


#==============================================================================================================================
#Ingresar Obtener Usuario
#==============================================================================================================================
@app.route('/obtenerUsu', methods=["GET", "POST"])
def obtenerUsu():
    obtener = baseDatos[MONGO_COLLECTION8]

    O_id = request.form.get('O_id')
    O_usuario = request.form.get('O_usuario')
    O_nombre = request.form.get('O_nombre')
    O_apellido = request.form.get('O_apellido')
    O_cedula = request.form.get('O_cedula')
    O_correo = request.form.get('O_correo')
    O_contrasenia = request.form.get('O_contrasenia')
    O_materia = request.form.get('O_materia')
    O_curso = request.form.get('O_curso')
    O_rol = request.form.get('O_rol')
    O_foto = request.form.get('O_foto')

    dict = {
        "id":O_id,
        "usuario":O_usuario,
        "nombre":O_nombre,
        "apellido":O_apellido,
        "cedula":O_cedula,
        "correo":O_correo,
        "contrasenia":O_contrasenia,
        "materia":O_materia,
        "curso":O_curso,
        "rol":O_rol,
        "foto":O_foto,
    }

    obtener.update_one({'_id' : ObjectId("630628a2e1b5b8c4bfd40d15")}, {'$set' : dict})
    return redirect(url_for('game'))



#==============================================================================================================================
#Valoracion
#==============================================================================================================================
@app.route('/valoracionx', methods=["GET", "POST"])
def valoracionx():
    obtener = baseDatos[MONGO_COLLECTION9]

    usuario = request.form.get('userT')
    estrellas = request.form.get('estrellas')

    dict = {
        "usuario":usuario,
        "valoracion": estrellas
    }
    insertarV = obtener.insert_one(dict)                  
    print(insertarV.inserted_id)
    return redirect(url_for('evaluacionGame'))

#==============================================================================================================================
#Puntuacion
#==============================================================================================================================
@app.route('/puntuacionx', methods=["GET", "POST"])
def puntuacionx():
    obtener = baseDatos[MONGO_COLLECTION10]

    nombre = request.form.get('nombreT')
    apellido = request.form.get('apellidoT')
    cedula = request.form.get('cedulaT')
    correo = request.form.get('correoT')
    materia = request.form.get('materiaT')
    puntuacion = request.form.get('puntuacionT')

    dict = {
        "nombre" :nombre,
        "apellido" : apellido,
        "cedula" : cedula,
        "correo" : correo,
        "materia" : materia,
        "puntuacion" :  puntuacion
    }
    insertarP = obtener.insert_one(dict)                  
    print(insertarP.inserted_id)
    return redirect(url_for('evaluacionGame'))



#Metodo para modificar datos
@app.route('/editNota/<string:id_cedula>', methods =["GET", "POST"])
#Crea la funcion para la modificacion del permiso
def editNota(id_cedula):
    editarNota = baseDatos[MONGO_COLLECTION10]
            
    P_puntuacion = request.form.get('P_puntuacion')     

    dict = { 
            "puntuacion" : P_puntuacion                        
            }
            
    editarNota.update_one({'_id' : ObjectId(id_cedula)}, {'$set' : dict})
    return redirect(url_for('notas'))

#==============================================================================================================================
#Ingresar Administrador
#==============================================================================================================================
#login admin
#Controlador de la ruta para borrar los datos de la tabla
@app.route('/ingresarAdmin', methods=['POST'])
#Crea la funcion para el ingreso del login de administrador
def ingresarAdmin():

    user = usuarios.find_one({"correo": request.form["usuario_admin"], "rol":"Administrador", "estado":"Activo"})

    if user is None:
        return redirect(url_for('errorUsuario'))
    else:
        passwor = user["contrasenia"]
        passw = request.form["pass_admin"]
        if user:
            if passwor == passw:
                return redirect(url_for('correctoAdministrador'))   #VENTANA (Bienvenido)
            return redirect(url_for('errorUsuario'))
        return "xd"


#==============================================================================================================================
#Ingresar Docente
#==============================================================================================================================
#login admin
#Controlador de la ruta para borrar los datos de la tabla
@app.route('/ingresarDocente', methods=['POST'])
#Crea la funcion para el ingreso del login de administrador
def ingresarDocente():

    user = usuarios.find_one({"correo": request.form["usuario_docente"], "rol":"Docente", "estado":"Activo"})

    if user is None:
        return redirect(url_for('errorUsuario'))
    else:
        passwor = user["contrasenia"]
        passw = request.form["pass_docente"]
        if user:
            if passwor == passw:
                return redirect(url_for('correctoDocenteAlert'))   #VENTANA (Bienvenido)
            return redirect(url_for('errorUsuario'))
        return "xd"



#==============================================================================================================================
#CONTROLADOR DE ERRORES
#==============================================================================================================================

#Errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
    'message':'No encontrado' + request.url,
    'status':'404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


'''
Finalmente usamos la función run() para ejecutar el servidor local con nuestra
aplicación. El if __name__ == '__main__': se asegura de que el servidor solo se ejecute 
si el script se ejecuta directamente desde el intérprete de Python y no se usa como un 
módulo importado.
'''
if __name__ == '__main__':
    app.run(debug=True)

'''
dentro del if
hashed_password = generate_password_hash(contraseña)
'''