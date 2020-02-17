iso87 = { 1:"b;8;Bit Map Extended",
        2:"n;..19;Primary account number (PAN)",
        3:"n;6;Processing code",
        4:"n;12;Amount, transaction",
        5:"n;12;Amount, Settlement",
        6:"n;12;Amount, cardholder billing",
        7:"n;10;Transmission date  time",
        8:"n;8;Amount, Cardholder billing fee",
        9:"n;8;Conversion rate, Settlement",
        10:"n;8;Conversion rate, cardholder billing",
        11:"n;6;Systems trace audit number",
        12:"n;6;Time, Local transaction",
        13:"n;4;Date, Local transaction (MMdd)",
        14:"n;4;Date, Expiration",
        15:"n;4;Date, Settlement",
        16:"n;4;Date, conversion",
        17:"n;4;Date, capture",
        18:"n;4;Merchant type",
        19:"n;3;Acquiring institution country code",
        20:"n;3;PAN Extended, country code",
        21:"n;3;Forwarding institution. country code",
        22:"n;12;Point of service entry mode",
        23:"n;3;Application PAN number",
        24:"n;3;Function code(ISO 8583:1993)/Network International identifier (?)",
        25:"n;2;Point of service condition code",
        26:"n;2;Point of service capture code",
        27:"n;1;Authorizing identification response length",
        28:"n;8;Amount, transaction fee",
        29:"n;8;Amount. settlement fee",
        30:"n;8;Amount, transaction processing fee",
        31:"n;8;Amount, settlement processing fee",
        32:"n;6;Acquiring institution identification code",
        33:"n;6;Forwarding institution identification code",
        34:"n;..28;Primary account number, extended",
        35:"z;..37;Track 2 data",
        36:"n;..104;Track 3 data",
        37:"an;12;Retrieval reference number",
        38:"an;6;Authorization identification response",
        39:"an;2;Response code",
        40:"an;3;Service restriction code",
        41:"ans;8;Card acceptor terminal identification",
        42:"ans;15;Card acceptor identification code",
        43:"ans;40;Card acceptor name/location",
        44:"an;..25;Additional response data",
        45:"an;..76;Track 1 Data",
        46:"an;..999;Additional data - ISO",
        47:"an;..999;Additional data - National",
        48:"an;..999;Additional data - Private",
        49:"a;3;Currency code, transaction",
        50:"an;3;Currency code, settlement",
        51:"a;3;Currency code, cardholder billing",
        52:"b;8;Personal Identification number data",
        53:"n;18;Security related control information",
        54:"an;..12;Additional amounts",
        55:"ans;..999;Reserved ISO",
        56:"ans;..999;Reserved ISO",
        57:"ans;..999;Reserved National",
        58:"ans;..999;Reserved National",
        59:"ans;..999;Reserved for national use",
        60:"an;..7;Advice/reason code (private reserved)",
        61:"ans;..999;Reserved Private",
        62:"ans;..999;Reserved Private",
        63:"ans;..999;Reserved Private",
        64:"b;16;Message authentication code (MAC)",
        65:"b;16;Bit map, tertiary",
        66:"n;1;Settlement code",
        67:"n;2;Extended payment code",
        68:"n;3;Receiving institution country code",
        69:"n;3;Settlement institution county code",
        70:"n;3;Network management Information code",
        71:"n;4;Message number",
        72:"ans;..999;Data record (ISO 8583:1993)/n 4 Message number, last(?)",
        73:"n;6;Date, Action",
        74:"n;10;Credits, number",
        75:"n;10;Credits, reversal number",
        76:"n;10;Debits, number",
        77:"n;10;Debits, reversal number",
        78:"n;10;Transfer number",
        79:"n;10;Transfer, reversal number",
        80:"n;10;Inquiries number",
        81:"n;10;Authorizations, number",
        82:"n;12;Credits, processing fee amount",
        83:"n;12;Credits, transaction fee amount",
        84:"n;12;Debits, processing fee amount",
        85:"n;12;Debits, transaction fee amount",
        86:"n;15;Credits, amount",
        87:"n;15;Credits, reversal amount",
        88:"n;15;Debits, amount",
        89:"n;15;Debits, reversal amount",
        90:"n;42;Original data elements",
        91:"an;1;File update code",
        92:"n;2;File security code",
        93:"n;5;Response indicator",
        94:"an;7;Service indicator",
        95:"an;42;Replacement amounts",
        96:"an;8;Message security code",
        97:"n;16;Amount, net settlement",
        98:"ans;25;Payee",
        99:"n;..11;Settlement institution identification code",
        100:"n;..11;Receiving institution identification code",
        101:"ans;17;File name",
        102:"ans;..28;Account identification 1",
        103:"ans;..28;Account identification 2",
        104:"ans;..100;Transaction description",
        105:"ans;..999;Reserved for ISO use",
        106:"ans;..999;Reserved for ISO use",
        107:"ans;..999;Reserved for ISO use",
        108:"ans;..999;Reserved for ISO use",
        109:"ans;..999;Reserved for ISO use",
        110:"ans;..999;Reserved for ISO use",
        111:"ans;..999;Reserved for ISO use",
        112:"ans;..999;Reserved for national use",
        113:"n;..11;Authorizing agent institution id code",
        114:"ans;..999;Reserved for national use",
        115:"ans;..999;Reserved for national use",
        116:"ans;..999;Reserved for national use",
        117:"ans;..999;Reserved for national use",
        118:"ans;..999;Reserved for national use",
        119:"ans;..999;Reserved for national use",
        120:"ans;..999;Reserved for private use",
        121:"ans;..999;Reserved for private use",
        122:"ans;..999;Reserved for private use",
        123:"ans;..999;Reserved for private use",
        124:"ans;..255;Info Text",
        125:"ans;..50;Network management information",
        126:"ans;..6;Issuer trace id",
        127:"ans;..999;Reserved for private use",
        128:"b;16;Message Authentication code",
        }

class BitMap:

    def __init__(self):
        self.ok = True

    def bitmap_campos(self, hexbitmap, incremento = 0, lista = True):

        if type(hexbitmap) is list:
            lst = hexbitmap
        else:
            lst = hexbitmap.split()

        map = ''
        for v in lst:
            if len(v) == 2:
                numbin = bin(int(v, 16)).replace('0b', '').zfill(8)
                map += numbin
        if lista:
            campos = []
            i = 1
            for num in map:
                if num == '1':
                    campos.append(i + incremento )
                i += 1
            return campos
        else:
            return map

    def campos_bitmap(self, lst):
        map = '0,' * 65
        map = map.split(',')
        for v in lst:
            if v > 0:
                map[v - 1] = '1'
        hexbitmap = ''
        for i in range(8):
            num = ''.join(map[:8])
            map = map[8:]
            num = hex(int(num, 2)).upper().replace('X', 'x')
            hx = num.replace('0x', '')
            hx = hx.rjust(2, '0')
            hexbitmap += hx + ' '
        return hexbitmap


class ISO8583:
    _estructura = {'0800': [1, 7, 11, 32, 33, 70],
                  '0810': [1, 7, 11, 32, 33, 70],
                  '0100': [2, 3, 4, 6, 7, 10, 11, 14, 18, 22, 25, 26, 32, 35, 37, 41, 42, 43, 49, 51, 52],
                  '0110': [2, 3, 4, 7, 11, 32, 37, 38, 39, 41, 42, 49],
                  '0400': [1, 2, 3, 4, 5, 7, 11, 14, 18, 22, 25, 32, 37, 38, 43, 49, 54],
                  '0410': [1, 2, 3, 4, 7, 11, 32, 37, 38, 39, 49]}



    def __init__(self, mensaje):
        self._reservado = ""
        self._reservadobin = ""
        self._camposbin = ""
        self._bmp = BitMap()
        self._diccampos = {}
        self._mapa = {}
        if type(mensaje) is list:
            self._mensaje = mensaje
        else:
            if len(mensaje[0]) == 1:
               # self._mensaj1 = ''
               # for x in mensaje:
               #     p1 = ord(x)
               #     p2 = hex(p1)
               #     p3 = p2.replace('0x', '').upper()
               #     p4 = p3.rjust(2,"0")
                #    self._mensaj1 += p4


                self._mensaje =  [hex(ord(x)).replace("0x", "").upper().rjust(2,"0") for x in mensaje]


            else:
                self._mensaje = mensaje.split()
        final = 0
        acum = 0
        self._tipo = self._mensaje[0:acum + 4]
        self._tiporesp = ''.join(str((int(x, 16) - 0x30)) for x in self._tipo).replace('00', '10')
        acum += 4
        self._bitmap = self._mensaje[acum:acum+8]
        acum += 8

        self._campos= self._bmp.bitmap_campos(self._bitmap, 0 )
        self._camposbin = self._bmp.bitmap_campos(self._bitmap, 0, False)
        if self._campos[0] == 1:
            self._reservado = self._mensaje[acum:acum + 8]
            self._reservadobin = self._bmp.bitmap_campos(self._reservado, 64, False)
            self._campos.extend(self._bmp.bitmap_campos(self._reservado, 64))


        for num in self._campos:
            campo = iso87[num].split(';')
            tamcamp = campo[1].count('.')
            valor = 0
            final = 0

            if tamcamp == 0:
                final = acum + int(campo[1])
                valor = self._mensaje[acum:final]
                original = mensaje[acum:final]
                vo = original
            else:
                tmp = self._mensaje[acum:acum + tamcamp]
                valor = tamcamp
                tamcamp = ''.join( str(int(x, 16) - 0x30) for x in self._mensaje[acum:acum + tamcamp])
                tamcamp = int(tamcamp)
                final = acum + tamcamp + valor
                original = mensaje[acum:final]
                valor = self._mensaje[acum:final]
                vo = original

            if num == 2:
                origina1 = original
                original =  original[:8]+ 'X' * 6 + original[-4:]
                tmp  = []
                tmp.extend(valor[:8])
                tmp.extend(['58','58','58','58','58','58'])
                tmp.extend(valor[-4:] )
                valor = tmp

            if num == 35:
                origina1 = original
                original =  original[:8]+ 'X' * 6 + original[8+6:]
                original = original[:-13] + 'X' * 13
                tmp  = []
                tmp.extend(valor[:8])
                tmp.extend( '58' for x in range(6))
                tmp.extend(valor[14:14+12] )
                tmp.extend('58' for x in range(13))
                #print tmp
                #print valor
                valor = tmp

            nodo ={}
            nodo['inicio'] = acum
            nodo['final'] = final
            nodo['tipo'] = campo[0]
            nodo['valor'] = valor
            nodo['vorigen'] = original
            nodo['vo'] = vo
            nodo['desc'] = campo[2]
            self._diccampos[num] = nodo
            acum = final


    def respuestabin(self):
        self._responder =''
        self._responderbin =''
        if self._tipo[2] == '30':
            self._responder, self._responderbin = self._respuesta()
        return self._responderbin

    def respuesta(self):
        if self._tipo[2] == '30':
            self._responder, self._responderbin = self._respuesta()
        return self._responder

    def _respuesta(self):

        campos = self._estructura[self._tiporesp]
        lcampos = []
        lextendido = []
        for i in campos:
            if i > 64:
                lextendido.append(i - 64)
            else:
                lcampos.append(i)
        lcampos = sorted(lcampos)
        bitmap = self._bmp.campos_bitmap(lcampos)


        mensaje = []
        mensaje.extend(''.join( x + ',' for x in self._tipo).replace('30,30,', '31,30').split(','))
        mensaje.extend(bitmap.split())
        mensajebin = ''.join( str(int(x, 16) - 0x30) for x in self._tipo).replace('00', '10')
        mensajebin += ''.join( chr(int(b, 16)) for b in bitmap.split())

        if len(lextendido) > 0:
            lextendido = sorted(lextendido)
            extendido = self._bmp.campos_bitmap(lextendido)
            mensaje.extend(extendido.split())

        if self._tiporesp in self._mapa:
            mapa = self._mapa[self._tiporesp]
        mapa = {}
        for campo in lcampos:
            if campo in mapa:
                mensaje.extend(mapa[campo])
                mensajebin += ''.join(str(int(x, 16) - 0x30) for x in mapa[campo])

            else:
                if campo in self._diccampos:
                    mensaje.extend(self._diccampos[campo]['valor'])
                    mensajebin += self._diccampos[campo]['vo']

        if len(lextendido) > 0:
            for campo in lextendido:
                campo = campo + 64
                if campo  in mapa:
                    mensaje.extend(mapa[campo])
                    mensajebin += ''.join(str(int(x, 16) - 0x30) for x in mapa[campo])

                else:
                    if campo in self._diccampos:
                        mensaje.extend(self._diccampos[campo]['valor'])
                        mensajebin += self._diccampos[campo]['vo']

        return mensaje, mensajebin

    def tipo(self):
        return self._tipo, ''.join(str((int(num,16) - 0x30)) for num in self._tipo)

    def tipo_r(self):
        return self._tiporesp


    def campos(self):
        return self._campos

    def bitmapbin(self):
        return self._camposbin

    def extendbin(self):
        return self._reservadobin

    def mensaje(self):
        return self._mensaje

    def valor(self, campo, hexadecimal=True):
        nodo  = self._diccampos[campo]

        return nodo['valor'], nodo['vorigen'], nodo['desc']

    def campo_valor(self, campo,):
        nodo = self._diccampos[campo]
        return nodo['vo']

    def campo_valorh(self, campo,):
        nodo = self._diccampos[campo]
        return nodo['valor']

    def cambiax(self, x):
        if x == '58':
            y = 'X'
        else:
           y = str(int(x,16) - 0x30)
        return y

    def bitmap(self):
        return self._bitmap

    def reservado(self):
        return self._reservado

    def regla(self,  mensaje, campo, valor):
        if not(mensaje in self._mapa):
            self._mapa[mensaje] = {}
        self._mapa[mensaje][campo] = valor

    def formato(self):
        return iso87


class TipoDato:
    def __init__(self, valor):
        self.valor = valor
    # valores no separados
    def vns(self):
        return ''.join(num for num in self.valor)
    # valores separados por espacio
    def vse(self):
        return ''.join(num + ' ' for num in self.valor)
    # valores separados por coma
    def vsc(self):
        return ''.join(num + ',' for num in self.valor)
    # listado
    def lista(self):
        return self.valor


if __name__ == "__main__":
    prueba = {"bitmap": "7A 24 44 81 28 E0 90 00 ",
              "campos": [2, 3, 4, 5, 7, 11, 14, 18, 22, 25, 32, 35, 37, 41, 42, 43, 49, 52]
             }

    bmp = BitMap()
    bitmap = bmp.campos_bitmap(prueba["campos"])
    assert bitmap == prueba["bitmap"]
    campos = bmp.bitmap_campos(prueba["bitmap"])
    assert prueba["campos"] == campos

    mensaje ="30 38 30 30 82 20 00 01 80 00 00 00 04 00 00 00 00 00 00 00 30 34 32 38 31 34 32 38 34 36 31 34 32 38 33 33 39 39 32 30 30 30 39 32 30 30 30 30 30 30 31"
    iso = ISO8583()
    iso.mensaje(mensaje)
    tipoh, tipo = iso.tipo()

