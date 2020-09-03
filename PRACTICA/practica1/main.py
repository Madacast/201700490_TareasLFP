import json
import webbrowser

lista=[]
maximoEdad=0
maximoPromedio=0
minimoEdad=0
minimoPromedio=0
sumaEdad=0
sumaPromedio=0

class persona:
    def __init__(self,nombre,edad,activo,promedio):
        self.nombre=nombre
        self.edad=edad
        self.activo=activo
        self.promedio=promedio

def cargaDatos(archivo):
    global sumaEdad
    global sumaPromedio
    global maximoEdad
    global maximoPromedio
    global minimoEdad
    global minimoPromedio

    archivo+='.json'
    file = open(archivo)
    count = file.read()
    biblioteca= json.loads(count)
    for corre in biblioteca:
#recorre lista json
        for corre2 in corre:
#obtiene etiquetas de datos
    #obtiene nombre
            if  str(corre2)=='nombre':
                nombre = corre['nombre']
    #obtiene Edad
            if  str(corre2)=='edad':
                edad=corre['edad']
    #Suma edad a variable global sumaEdad
                sumaEdad+=edad
                if maximoEdad<edad:
                    maximoEdad=edad
                if minimoEdad>edad or len(lista)==0:
                    minimoEdad=edad
    #obtiene Activo
            if str(corre2)=='activo':
                activo=corre['activo']
    #obtiene promedio
            if str(corre2)=='promedio':
                promedio=corre['promedio']
                sumaPromedio+=promedio
                if maximoPromedio<promedio:
                    maximoPromedio=promedio
                if minimoPromedio>promedio or len(lista)==0:
                    minimoPromedio=promedio
        newPersona= persona(nombre,edad,activo,promedio)
        lista.append(newPersona)
    file.close()
    print(archivo + ' se cargo con exito.')

def maximo(tipo):
    global maximoEdad
    global maximoPromedio
    if  tipo=='edad':
        return maximoEdad
    elif tipo=='promedio':
        return maximoPromedio
    else:
        print('No existe algun campo '+tipo+', verifique su entrada')

def minimo(tipo):
    global minimoEdad
    global minimoPromedio
    if tipo=='edad':
        return minimoEdad
    elif tipo=='promedio':
        return minimoPromedio
    else:
        print('No existe algun campo '+tipo+', verifique su entrada')

def suma(tipo):
    global sumaEdad
    global sumaPromedio
    if  tipo=='edad':
        return sumaEdad
    elif tipo=='promedio':
        return sumaPromedio
    else:
        print('No existe algun campo '+tipo+', verifique su entrada')

def generaHTML(numero):
    i=0
    codigo='''<!doctype html>
<html lang="es">	 	 
<HEAD>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">	 
<link rel="stylesheet" href="css/bootstrap.min.css">
<TITLE> Practica 1 </TITLE>
</HEAD>	 
<BODY>
<h1>Reporte</h1>	 
<table class="table table-hover">
<tr>
<td>Nombre</td>
<td>Edad</td>
<td>Activo</td>
<td>Promedio</td>
</tr>
<tbody>
    '''
    for recorre in lista:
        codigo += '<tr>\n'
        codigo += '<td>'
        codigo += recorre.nombre
        codigo += '</td>\n'
        codigo += '<td>'
        codigo += str(recorre.edad)
        codigo += '</td>\n'
        codigo += '<td>'
        codigo += str(recorre.activo)
        codigo += '</td>\n'
        codigo += '<td>'
        codigo += str(recorre.promedio)
        codigo += '</td>\n'
        codigo += '</tr>\n'
        i += 1
        if i==numero:
            break
    codigo+='''<tbody>
</table>
</BODY>	 
</HTML>	'''
    return codigo

def seleccionar(campos,comparacion):
    auxComparacion=comparacion.split('=')
    auxCampos=campos.split(',')
    if  len(auxComparacion)==2:
        campo=str(auxComparacion[0])
        dato=str(auxComparacion[1])

    #opcion donde restriccion es nombre
        if campo.lower()=='nombre':
            i = 0
            auxiliar = ''
            for recorre in dato:
                if i > 0 and i < len(dato) - 1:
                    auxiliar += recorre
                i += 1
            for recorre in lista:
                if auxiliar==recorre.nombre:
                    for recorreCampos in auxCampos:
                        if recorreCampos.lower()=='edad':
                            print(recorre.edad)
                        elif recorreCampos.lower()=='nombre':
                            print(recorre.nombre)
                        elif recorreCampos.lower()=='activo':
                            print(recorre.activo)
                        elif recorreCampos.lower()=='promedio':
                            print(recorre.promedio)
                        else:
                            print('El campo '+campo+' no se encuentara especificado, revise su entrada')
    #Opcion donde restriccion es edad
        elif campo.lower()=='edad':
            for recorre in lista:
                if dato==str(recorre.edad):
                    for recorreCampos in auxCampos:
                        if recorreCampos.lower()=='edad':
                            print(recorre.edad)
                        elif recorreCampos.lower()=='nombre':
                            print(recorre.nombre)
                        elif recorreCampos.lower()=='activo':
                            print(recorre.activo)
                        elif recorreCampos.lower()=='promedio':
                            print(recorre.promedio)
                        else:
                            print('El campo '+campo+' no se encuentara especificado, revise su entrada')
    #opcion donde restriccion es promedio
        elif campo.lower()=='promedio':
            for recorre in lista:
                if dato==str(recorre.promedio):
                    for recorreCampos in auxCampos:
                        if recorreCampos.lower()=='edad':
                            print(recorre.edad)
                        elif recorreCampos.lower()=='nombre':
                            print(recorre.nombre)
                        elif recorreCampos.lower()=='activo':
                            print(recorre.activo)
                        elif recorreCampos.lower()=='promedio':
                            print(recorre.promedio)
                        else:
                            print('El campo '+campo+' no se encuentara especificado, revise su entrada')
    #opcion donde restriccion es activo
        elif campo.lower()=='activo':
            for recorre in lista:
                if dato==str(recorre.activo):
                    for recorreCampos in auxCampos:
                        if recorreCampos.lower()=='edad':
                            print(recorre.edad)
                        elif recorreCampos.lower()=='nombre':
                            print(recorre.nombre)
                        elif recorreCampos.lower()=='activo':
                            print(recorre.activo)
                        elif recorreCampos.lower()=='promedio':
                            print(recorre.promedio)
                        else:
                            print('El campo '+campo+' no se encuentara especificado, revise su entrada')
                    print('--------------\n')
        else:
            print('El campo '+campo+' no se encuentra, revise su entrada')

    else:
        print('Error, verifique su entrada')


def instrucciones():
    global lista
    while True:
        print('Ingrese su comando:\n\tCargar\n\tSeleccionar\n\tMaximo\n\tMinimo\n\tSuma\n\tCuenta\n\tReportar\n\tSalir')
        opcion=input("Ingrese su opcion: ")

    #opcion de salida
        if opcion.lower()=='salir':
            break
        else:
            aux=opcion.split()
    #opcion de carga de datos
            try:
                if aux[0].lower()=='cargar':
                    auxDatos=aux[1].split(',')
                    for inserta in auxDatos:
                        try:
                            cargaDatos(inserta)
                        except:
                            print('No se pudo cargar el archivo "'+inserta+'". Verifique su entrada.')
                            input('Presione enter para continuar')
            except:
                print('Opcion no valida, verifique su entrada')
                input('Presione enter para continuar')
    #Opcion de maximo
            if aux[0].lower()=='maximo':
                try:
                    print('El maximo de '+aux[1]+' es: '+str(maximo(aux[1].lower())))
                except:
                    print('Opcion no valida, verifique su entrada')
                input('Presione enter para continuar')
    #opcion de minimo
            elif aux[0].lower()=='minimo':
                try:
                    print('El minimo de '+aux[1]+' es: '+str(minimo(aux[1].lower())))
                except:
                    print('Opcion no valida, verifique su entrada')
                input('Presione enter para continuar')
    #opcion de suma
            elif aux[0].lower()=='suma':
                try:
                    print('La suma de '+aux[1]+' es: '+str(suma(aux[1].lower())))
                except:
                    print('Opcion no valida, verifique su entrada')
                input('Presione enter para continuar')
    #opcion de cuenta
            elif aux[0].lower()=='cuenta':
                try:
                    print('Exiten '+str(len(lista))+' registros')
                except:
                    print('Opcion no valida, verifique su entrada')
                input('Presione enter para continuar')
    #opcion que genera reportes
            elif aux[0].lower()=='reportar':
                try:
                    if  not int(aux[1])<0:
                        file=open('reporte.html','w')
                        file.write(generaHTML(int(aux[1])))
                        file.close()
                        webbrowser.open('reporte.html')
                    else:
                        print('Debe ingresar un rango mayor a cero')
                        input('Presione enter para continuar')
                except:
                    print('Opcion no valida, verifique su entrada')
                    input('Presione enter para continuar')
    #opcion seleccionar
            elif aux[0].lower()=='seleccionar':
                if len(aux)==2:
                    if aux[1]=='*':
                        for recorre in lista:
                            print('\n'+recorre.nombre+'\n'+str(recorre.edad)+'\n'+str(recorre.activo)+'\n'+str(recorre.promedio))
                            print('------------------')
                        input('Presione enter para continuar')
                    else:
                        print('Opcion no valida, verifique su entrada')
                elif len(aux)==4 and aux[2].lower()=='donde':
                    seleccionar(aux[1],aux[3])
                else:
                    print('Operacion no valida, verifique su entrada')

instrucciones()


#seleccionar('1,2,3','a=123456')