import sys
import os
from util.iso8583 import ISO8583
import argparse
# !/usr/local/bin/python

encabhtml = '<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<style>\n.table-bordered' \
            ' th,.table-bordered  td{\n\nborder:1px solid #ddd !important;\n}\n.hex{\n\npadding-left:0px;\n' \
            'margin:0px;\nfloat:left;\nposition:absolute;\nwidth:710px;\n}\n' \
            '.cuadro{outline: 1px  dotted #181783;outline-offset: 0.5px}'\
            '.linea{\nfont-size:15px;\npadding' \
            '-left:0px;\nmargin:0px;\nwidth:710px;\nfloat:left;\n}\n.campos{\nclear:both;\n display:block;\n ' \
            'font-size:15px;\nmargin-top:10px;\nwidth:100%;\nfloat:left;\n}\n.lineah{\nmargin-left:710px;\n' \
            'font-size:15px;\npadding-left:0px;\nmargin:0px;\nwidth:450px;\nfloat:left;\n}\n.bin{\nmargin-left' \
            ':710px;\npadding:0px;\nfloat:left;\nposition:relative;\nwidth:450px;\n}\n.mensaje{\nmargin:0px;\n' \
            'width:100%;\nfloat:left;\n}\n.data{\nfloat:left;\n }\n.yellow{\nbackground-color:#468CD2;\n ' \
            '!important;\ncolor:white;\nbox-shadow: 2px 1px 1px #333333;\n' \
            '}\n.white{\nbackground-color:white;\n}\n.color1{\ntext-decoration:underline;\n}\n.' \
            'color2{\n}\n.separador{\nwidth:945px;\n}</style>\n<script language="Javascript" type' \
            '="text/Javascript"> function resalta (id){\nvar hex = "hex"+id;\n var bin = "bin' \
            '"+id;\n var num = "num"+id;\n var tex = "tex"+id;\n var lor = "lor"+id;\n var idc = ' \
            '"idc"+id;\n cambia(hex, "white", "yellow");\n cambia(bin, "white", "yellow");\n ' \
            'cambia(num, "white", "yellow");\n cambia(tex, "white", "yellow");\n cambia(lor, ' \
            '"white", "yellow");\n cambia(idc, "white", "yellow");\n cambia(hex+"a", "white", ' \
            '"yellow");\n cambia(bin+"a", "white", "yellow");\n  };\n function normal (id){\nvar ' \
            'hex = "hex"+id;\n var bin = "bin"+id;\n var num = "num"+id;\n var tex = "tex"+id;\n' \
            ' var lor = "lor"+id;\n var idc = "idc"+id;\n cambia(hex, "yellow", "white");\n ' \
            'cambia(bin, "yellow", "white");\n cambia(num, "yellow", "white");\n cambia(tex, ' \
            '"yellow", "white");\n cambia(lor, "yellow", "white");\n  cambia(idc, "yellow", ' \
            '"white");\n  cambia(hex+"a", "yellow", "white");\n cambia(bin+"a", "yellow", ' \
            '"white");\n };\n function cambia (id, clase1, clase2){\nif ( document.' \
            'getElementById(id).classList.contains(clase1) ){\ndocument.getElementById(id)' \
            '.classList.remove(clase1);\n}\nelse{\ndocument.getElementById(id).classList.' \
            'add(clase2);\n };\n };\n</script>\n</head>\n<body>\n<font face="Courier New" size="9">' \
            '<div class="base">\n<div class="mensaje">\n<div class="hex">\n<div class = "linea">'




meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
         'Diciembre']

color1 = 'LightYellow'

color2 = 'white'

values = {3: {'List': {'items': 3,
                       'largo': 2,
                       1: {'00': 'Electronic Purchase',
                           '01': 'Cash Advance',
                           '17': 'Carga chip',
                           '30': 'Balance',
                           },
                       3: {'00': 'No program aplies',
                           '02': 'Automatic currency exchange',
                           '19': 'Merchant discount program',
                           },
                       },
              },
          4: 'Monto',
          5: 'Monto',
          6: 'Monto',
          7: 'DateTime',
          8: 'Monto',
          14: 'Date',
          18: {'9999': 'Electronic Purchase', '6010': 'Cash Advance'},
          22: {'List': {'items': 12,
                        'largo': 1,
                        1: {'1': 'PAN Entry Mode Capacity',
                            '2': 'Track II Read',
                            '5': 'Chip card'
                            },
                        2: {'1': 'PIN'},
                        5: {'1': 'Card holder present'},
                        7: {'2': ' Track II Read', '5': 'Chip card'},
                        8: {'5': ' Signature', '1': 'PIN'},
                        },
               },
          25: {'02': 'ATM', '00': 'POS'},
          32: {'992000': 'Adquiriente de las trans. POS'},
          #49: {'999': 'CUC', '192': 'CUP', '840': 'USD'},
          70: {'001': 'sign on', '002': 'sign off /accepted', '003': 'sign on accepted', '004': 'sign on denied'}

          }


pie = '' \
      ' ' \
      '</div>\n</div>\n</div>\n</div>\n</body></html> '


def leefichero(fname, procesar=True):
    file = open(fname, 'r')
    fch = ''
    for line in file:
        fch = fch + line
    file.close()
    if procesar:
        while fch.find('\n') >= 0:
            fch = fch.replace('\n', ' ')
        while fch.find('  ') >= 0:
            fch = fch.replace('  ', ' ')
    return fch


def test_bin(mensaje, encab):
    tmp = ''
    if (mensaje.find(' ') > 3) or (mensaje.find(' ') < 0):
        tmp = mensaje
        mensaje = []
        print " Mensaje en formato binario"

        for item in tmp:
            item = hex(ord(item)).replace('0x', '')
            if item == '0x0':
                item = '00'
            item = item.zfill(len(item))
            # item = '00'[:2 - len(item)] + item
            mensaje.append(item)

    else:
        mensaje = mensaje.split(' ')

    return mensaje


import string, random
def id_gen(size=8, chars=string.ascii_uppercase[:6] + string.digits):
    """
    Genera un cadena de texto y numeros aleatoria en hexadecimal

    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))



def protec(texto):
    cambio ={" = ": "=",', "': ',"',
            "cambia":"_3","resalta":"_2","normal":"_1","> <":"><",": ":":","; ": ";","( ": "("," (": "(",
            "{ ": "{","} ": "}"," {": "{"," }": "}","\n": "","\t": " ","  ": " "
            }
    import re


    clases = {}
    #for linea in cambio:
    #    while salida.find(linea) >= 0:

    salida = texto

    for linea in cambio:
        while salida.find(linea) >= 0:
            salida = salida.replace(linea, cambio[linea])

    return salida


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", '--entrada',  help="Ubicacion del fichero con formato iso8583 a convertir")
    parser.add_argument("-d", '--destino',  help="Carpeta donde se va a guardar la pagina generada")

    args = parser.parse_args()
    cl = '\n'
    mensaje = leefichero(args.entrada)
    datos = {}
    datos["original"] = mensaje
    original = mensaje
    iso = ISO8583(mensaje)
    tipoh, tipo = iso.tipo()
    datos["tipo"] = tipo
    datos["tipoh"] = tipoh
    datos["bitmap"] = iso.bitmap()
    datos["campos"] = iso.campos()
    datos["reserv"] = iso.reservado()
    mensaje = iso.mensaje()
    datos["mensaje"] = mensaje

    pagina = encabhtml
    pagina = pagina + '<div id = "hex1000"  onmouseover="resalta(''1000'');"  onmouseout="normal(''1000'');" ' \
                      ' class="data" title="message ' + tipo + '"><b>'
    col = 0
    for item in tipoh:
        pagina += item + '&nbsp;'
        col += 1
    pagina = pagina + '</b></div>' + cl

    pagina = pagina + '<div id = "hex1001" onmouseover="resalta(''1001'');"  onmouseout="normal(''1001'');" ' \
                      'class="data" title="bitmap ' + ''.join(str(c) + ',' for c in datos["campos"]) + '">'

    subr = True
    for item in datos["bitmap"]:
        if subr:
            pagina += '<u>' + item + '</u>&nbsp;'
        else:
            pagina += item + '&nbsp;'
        subr = not subr
        col += 1
    pagina = pagina + '</div>' + cl

    pos = 0
    columnas = 25

    campos = {}
    neg = False
    for campo in datos["campos"]:
        neg = not neg
        valor = iso.valor(campo)
        campos[campo] = valor
        valorh = valor[0]
        tcampo = len(valorh)
        pagina = pagina + '<div  onmouseover="resalta(' + str(campo) + ');"  onmouseout="normal(' + \
                 str(campo) + ')" id="hex' + str(campo) + '" class="data" title="' + valor[2] + '">'
        if neg:
            pagina = pagina + '<b>'

        while len(valorh) > 0:
            pagina += valorh[0] + '&nbsp;'
            if len(valorh) > 0:
                valorh = valorh[1:]
            else:
                valorh = ''

            if col >= columnas:
                if neg:
                    pagina = pagina + '</b>'
                pagina += '</div>'+cl+'</div>'+cl+'<div class = "linea"><div  onmouseover="resalta(' + \
                          str(campo) + ')"  onmouseout="normal(' + str(campo) + ')" id="hex' + \
                          str(campo) + 'a" class="data" title="' + valor[2] + '">'
                if neg:
                    pagina = pagina + '<b>'
                col = 0
            else:
                col += 1
        if neg:
            pagina = pagina + '</b>'
        pagina = pagina + '</div>' + cl

    # bin
    pagina = pagina + '</div>'+cl+'</div>'+cl+'<div class="bin"><div class = "lineah"><div onmouseover="resalta(''1000'')"' \
                      '  onmouseout="normal(''1000'')" id= "bin1000" class="data" title="message ' + tipo + '"><b>'
    col = 0
    for item in tipo:
        pagina += item
        col += 1
    pagina = pagina + '</b></div>' + cl
    pagina = pagina + '<div id = "bin1001" onmouseover="resalta(''1001'')"  onmouseout="normal(''1001'')" ' \
                      'class="data" title="bitmap ' + ''.join(
        str(c) + ',' for c in datos["campos"]) + '">'
    for item in '.' * 8:
        pagina += item
        col += 1
    pagina = pagina + '</div>' + cl

    pos = 0
    neg = False
    for campo in datos["campos"]:
        neg = not neg
        valor = campos[campo]
        #print valor
        valorh = valor[1].replace('\x00', '.')
        tcampo = len(valorh)
        pagina = pagina + '<div onmouseover="resalta(' + str(campo) + ')"  onmouseout="normal(' + \
                 str(campo) + ')" id="bin' + str(campo) + '" class="data" title="' + valor[2] + '">'
        if neg:
            pagina = pagina + '<b>'

        while len(valorh) > 0:
            pagina += valorh[0]
            if len(valorh) > 0:
                valorh = valorh[1:]
            else:
                valorh = ''

            if col >= columnas:
                if neg:
                    pagina = pagina + '</b>'
                pagina += '</div>'+cl+'</div>'+cl+'<div class = "lineah"><div  onmouseover="resalta(' +\
                          str(campo) + ')"  onmouseout="normal(' + str(campo) + ')"  id="bin' +\
                          str(campo) + 'a" class="data" title="' + valor[2] + '">'
                if neg:
                    pagina = pagina + '<b>'
                col = 0
            else:
                col += 1
        if neg:
            pagina = pagina + '</b>'
        pagina = pagina + '</div>' + cl

    pagina = pagina + '</div>'+cl+'</div>'+cl+'</div>'+cl+'<div class = "campos"><div class="separador"><hr></div>'
    #Tabla con los binarios
    pagina = pagina +'<table>' + cl
    pagina = pagina + '<tr>'
    pagina = pagina + '<td></td>'
    pagina = pagina + '<td ></td>'
    regla = ''.join('.' * 9 + str(x + 1) for x in range(9))
    regla = regla[:64]
    pagina = pagina + '<td>' + regla + '</td>'
    pagina = pagina + '</tr>' + cl

    pagina = pagina + '<tr>'
    pagina = pagina + '<td></td>'
    pagina = pagina + '<td ></td>'
    regla = '1234567890' * 8
    regla = regla[:64]
    pagina = pagina + '<td>' + regla + '</td>'
    pagina = pagina + '</tr>' + cl

    pagina = pagina + '<tr>'
    pagina = pagina + '<td></td>'
    pagina = pagina + '<td >Bitmap&nbsp;&nbsp;</td>'
    regla = iso.bitmapbin().replace('1', '1,').replace('0', '0,').split(',')
    campo = 1
    tmp = ""
    color = 'color1'
    cuenta = 1
    for numb in regla:
        if cuenta > 8:
            cuenta = 1
            if color == 'color1':
                color = 'color2'
            else:
                color = 'color1'

        if numb == '1':
            tmp += '<span class="'+color+'" id= "idc' + str(campo) + '" ><b>1</b></span>'
        else:
            if numb == '0':
                tmp += '<span class="'+color+'" >.</span>'
        campo += 1
        cuenta +=1

    regla = tmp
    # regla = iso.bitmapbin().replace('1', '<span id= "" ><b>1</b></span>').replace('0','.')
    pagina = pagina + '<td>' + regla + '</td>'
    pagina = pagina + '</tr>' + cl
    regla = iso.extendbin().replace('1', '1,').replace('0', '0,').split(',')
    pagina = pagina + '<tr>'
    pagina = pagina + '<td></td>'
    pagina = pagina + '<td >Extend&nbsp;&nbsp;</td>'

    campo = 65
    tmp = ""
    color = 'color1'
    cuenta = 1
    for numb in regla:
        if cuenta > 8:
            cuenta = 1
            if color == 'color1':
                color = 'color2'
            else:
                color = 'color1'
        if numb == '1':
            tmp += '<span class="'+color+'" id= "idc' + str(campo) + '" ><b>1</b></span>'
        else:
            if numb == '0':
                tmp += '<span class="'+color+'" >.</span>'
        campo += 1
        cuenta += 1

    regla = tmp
    pagina = pagina + '<td>' + regla + '</td>'

    pagina = pagina + '<td></td></tr></table>'

    #Nueva tabla
    pagina = pagina + cl+'<div class="separador"><hr></div>'
    pagina = pagina + '<table><tr><td>&nbsp;</td><td></td><td></td></tr>' + cl
    pagina = pagina + '<tr><td>&nbsp;</td><td></td><td></td></tr>' + cl
    pagina = pagina + '<tr><td>&nbsp;</td><td></td><td></td></tr>' + cl
    pagina = pagina + '<tr  onmouseover="resalta(''1000'')"  onmouseout="normal(''1000'')" id="cam1000">'
    pagina = pagina + '<td id="num1000">'  '</td>'
    pagina = pagina + '<td id="tex1000">Mensaje No.</td>'
    pagina = pagina + '<td id="lor1000">' + tipo + '</td>'
    pagina = pagina + '</tr>' + cl

    pagina = pagina + '<tr  onmouseover="resalta(''1001'')"  onmouseout="normal(''1001'')" id="cam1001">'
    pagina = pagina + '<td id="num1001">'  '</td>'
    pagina = pagina + '<td id="tex1001">Campos en bitmap</td>'
    pagina = pagina + '<td id="lor1001">' + ''.join(str(x) + ',' for x in datos["campos"]) + '</td>'
    pagina = pagina + '</tr>' + cl
    pagina = pagina + '<tr><td>&nbsp;</td><td></td><td></td></tr>' + cl

    for campo in datos["campos"]:
        neg = not neg
        valor = campos[campo]
        ayuda = ''
        if campo in values:
            a = values[campo]
            data = valor[1]
            sep = ' '
            if 'List' in a:
                a = a['List']
                largo = a['largo']
                items = a['items'] + 1
                for posicion in range(items):
                    if (posicion + 1) in a:
                        a_tmp = a[(posicion + 1)]
                        texto = data[:largo]
                        if texto in a_tmp:
                            ayuda += texto + '-' + a_tmp[texto] + ', '
                    data = data[largo:]
            else:
                if 'DateTime' in a:
                    try:
                        a = meses[int(data[:2]) - 1]
                        data = data[2:]
                        a = a + ' 20' + data[:2]
                        data = data[2:]
                        a = a + ' ' + data[:2]
                        data = data[2:]
                        a = a + ':' + data[:2]
                        data = data[2:]
                        a = a + ':' + data[:2]
                        ayuda = a
                    except:
                        ayuda = ''
                else:
                    if 'Date' in a:
                        a = meses[int(data[2:4]) - 1] + ' 20' + data[:2]
                        ayuda = a

                    else:
                        if 'Monto' in a:
                            data = data[:len(data) - 2] + '.' + data[len(data) - 2:]
                            a = ' $ ' + str(float(data))
                            decimal = a.split('.')
                            if len(decimal[1]) == 1:
                                decimal[1] = decimal[1] + '0'
                            a = decimal[0] + '.' + decimal[1]
                            ayuda = a
                        else:
                            if data in a:
                                a = a[data]
                                ayuda = a
        else:
            ayuda = ''

        pagina = pagina + '<tr  title="' + ayuda + '"  onmouseover="resalta(' + str(
            campo) + ')"  onmouseout="normal(' + str(campo) + ')" id="cam' + str(campo) + '">'
        pagina = pagina + '<td  title="' + ayuda + '" id="num' + str(campo) + '">' + str(campo) + '</td>'
        pagina = pagina + '<td  title="' + ayuda + '" id="tex' + str(campo) + '">' + valor[2] + '</td>'

        tmp = valor[1]
        if campo == 1:
            tmp = '........'
            # for i in valor[1]:
            #    if ord(i) > 0:
            #        tmp +=  str(ord(i)).rjust(2,"0")

        pagina = pagina + '<td  title="' + ayuda + '" id="lor' + str(campo) + '">' + tmp + '</td>'

        pagina = pagina + '</tr>' + cl

    pagina = pagina + '</table>\n</div>' + cl

    pagina = pagina + pie
    fentrada = args.entrada.split(os.sep)[-1:][0]
    fsalida = os.path.join( args.destino, fentrada + '_ISO-8583_' + tipo + '.html')

    pagina = protec(pagina)
    file = open(fsalida, 'w')
    file.write(pagina)
    file.close()
    #pagina = iso.respuestabin()
    #file = open(fmensaje + "r", 'w')
    #file.write(pagina)
    #file.close()
    if fsalida.find('\\') < 0:
        print '\n\n -> ', os.getcwd() + os.sep + fsalida
    else:
        print '\n\n  ->', fsalida
