import webbrowser
class persona:
    def __init__(self,nombre,edad,activo,saldo):
        self.nombre=nombre
        self.edad=edad
        self.activo=activo
        self.saldo=saldo

lista=[]

persona1=persona('Eddy','33',True,1450)
lista.append(persona1)
persona2=persona('Raul','22',False,140)
lista.append(persona2)
persona3=persona('Diego','14',True,104)
lista.append(persona3)
persona4=persona('Roberto','47',True,14050)
lista.append(persona4)
persona5=persona('Tomas','89',True,145000)
lista.append(persona5)
persona6=persona('Maria','12',False,100)
lista.append(persona6)
persona7=persona('Gloria','07',True,145)
lista.append(persona7)
persona8=persona('Karen','9',False,178)
lista.append(persona8)
persona9=persona('Susan','14',True,10)
lista.append(persona9)
persona10=persona('Emily','45',False,145440)
lista.append(persona10)

def generaHTML():
    codigo='''<HTML>	 	 
<HEAD>	 
<TITLE> Tarea 4 </TITLE>
</HEAD>	 
<BODY>	 
<table border="1">
<tr>
<td>Nombre</td>
<td>Edad</td>
<td>Activo</td>
<td>Saldo</td>
</tr>
'''
    for recorre in lista:
        codigo+='<tr>\n'
        codigo+='<td>'
        codigo+=recorre.nombre
        codigo+='</td>\n'
        codigo += '<td>'
        codigo+=recorre.edad
        codigo += '</td>\n'
        codigo += '<td>'
        codigo+=str(recorre.activo)
        codigo += '</td>\n'
        codigo += '<td>'
        codigo+=str(recorre.saldo)
        codigo += '</td>\n'
        codigo+='</tr>\n'
    codigo+='''</table>
</BODY>	 
</HTML>	
    '''
    return codigo


file=open("tarea4.html","w")
file.write(generaHTML())
file.close()

webbrowser.open('tarea4.html')