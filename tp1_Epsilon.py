import random

# Grupo Épsilon Ɛ
# Integrantes:
#   Agustín Ezequiel Firmapaz     105172
#   Érik Emmanuel Anrique         103911
#   Tomas Troglio                 104378
#   Santiago Gomez                103430


#Constantes
#Inicio
#Cadenas de validacion
minusculas = "qwertyuiopasdfghjklzxcvbnm"
mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeros    = "1234567890"
simbolos   = ".:-_@#$&/()?*"
telefonica = "1234567890+() -"
alfanum    = minusculas + mayusculas + numeros
#Fin Cadenas de validacion

#Inicio
#Mensajes 
ingreso_predeterminado  = "Ingrese un dato: "
ingrese_latitud         = "Ingrese la latitud en la que se encuentra: "
ingrese_longitud        = "Ingrese la longitud en la que se encuentra: "
ingrese_contrasenia     = "Ingrese una clave de acceso: "
ingrese_restaurant      = "Ingrese el nombre del restaurant: "
ingrese_usuario         = "Ingrese su nombre de usuario: "
ingrese_telefono        = "Ingrese su numero de telefono: "
ingrese_direccion       = "Ingrese su direccion: "
ingrese_plato           = "Ingrese el nombre del plato: "
ingrese_precio          = "Ingrese el precio correspondiente: "
ingrese_radio           = "Ingrese el radio de entrega: "
ingrese_entero          = "Ingrese un numero entero: "
#Requisitos
requisitos_primer_plato = "Debera ingresar un primer plato para su restaurante."
requisitos_contrasenia  = "Debera tener al menos 8 caracteres, al menos una minuscula, una mayuscula, un numero y un simbolo."
requisitos_restaurante  = "El nombre debera contener entre 5 y 25 caracteres."
requisitos_plato        = requisitos_restaurante
requisitos_usuario      = "Debera contener entre 3 y 12 caracteres exclusivamente alfanumericos."
requisito_existencia_restaurante  = "Se requiere la existencia de al menos un restaurante."
requisito_existencia_rappitendero = "Se requiere la existencia de al menos un rappitendero."
requisito_existencia_cliente      = "Se requiere la existencia de al menos un cliente."
#Reingreso
reingrese_contrasenia   = "Ingrese nuevamente su clave de acceso: "
reingrese_datos         = "Por favor, ingrese los datos nuevamente."
reingrese_flotante      = "Se debe ingresar un numero real."
#Fin Mensajes

#Inicio
#Errores
error_dato_incorrecto        = "El dato ingresado no pudo ser procesado."
error_contrasenia_invalida   = "La contraseña ingresada no cumple con los requisitos."
error_contrasenia_incorrecta = "Las claves de acceso ingresadas no coinciden"
error_longitud               = "Se requiere cumplir con la longitud indicada en el intervalo:"
error_vacio                  = "No se ha ingresado información."
error_caracter_invalido      = "Usted ha ingresado un caracter invalido."
error_info_duplicada         = "No se puede ingresar este nombre porque ya existe."
error_tipo_entero            = "Se ingreso un dato que no puede ser procesado como numero entero."
#Fin Errores

#Inicializacion de listas de entidades

l_rappitenderos = []
l_restaurantes = []
l_clientes = []
l_pedido = []

#Fin de inicializacion de listas de entidades

##################################################################################################################################################
########################################################## FUNCIONES #########################################################################
##################################################################################################################################################

##################################################################################################################################################
########################################################## FUNCION 1 #####################################################################################
##################################################################################################################################################

def info_hardcodeada():
    restaurantes_hardcodeados = [
    {"Nombre": "McDonald's", "Direccion": "Independencia 1700", "Telefono": "11-2445-1234", "Posicion":(22.0,10.0), "Radio de entrega": 2.5 , "Platos": [{"Nombre": "Cuarto de Libra" , "Precio": 195.0}, {"Nombre": "McNuggets", "Precio": 215.0 }, {"Nombre": "Big Mac", "Precio": 200.0}, {"Nombre": "Ensalada Caesar", "Precio": 270.0}], "Total de ventas": 0.0},
    {"Nombre": "Parripollo Lo de Cesar" , "Direccion": "Coronel Montenegro 1250" , "Telefono": "11-7491-2670", "Posicion":(5.0,19.0), "Radio de entrega": 1.0, "Platos": [{"Nombre": "Pollo al Spiedo", "Precio": 290.0}, {"Nombre": "Pata", "Precio": 35.0}, {"Nombre": "Pechuga", "Precio": 110.0}, {"Nombre": "Porcion de Fritas", "Precio": 70.0}, {"Nombre": "Coca Cola", "Precio": 85.0}], "Total de ventas": 0.0},
    {"Nombre": "Lo de Carlitos" , "Direccion": "Posta de Pardo 700" , "Telefono": "11-6495-8744", "Posicion":(-15.0,-9.0), "Radio de entrega": 2.0, "Platos": [{"Nombre": "Panqueque ddl", "Precio": 170.0}, {"Nombre": "Hamburguesa completa", "Precio": 210.0}, {"Nombre": "Papas Fritas", "Precio": 120.0}, {"Nombre": "Fanta", "Precio": 75.0}, {"Nombre": "Heineken", "Precio": 130.0}], "Total de ventas": 0.0},
    {"Nombre": "Cerveceria Antares" , "Direccion": "Quirno Acosta 324", "Telefono": "11-1645-5987", "Posicion":(7.0,-4.2), "Radio de entrega": 1.0, "Platos": [{"Nombre": "Honey", "Precio": 165.0}, {"Nombre": "Ipa", "Precio": 165.0}, {"Nombre": "Porter", "Precio": 165.0}, {"Nombre": "Papas Rusticas", "Precio": 195.0}, {"Nombre": "Rabas", "Precio": 350.0}, {"Nombre": "Choricitos al vino", "Precio": 420.0}], "Total de ventas": 0.0},
    {"Nombre": "Green eat", "Direccion": "Alpinos", "Telefono": "11-6135-3544", "Posicion":(-20.0,13.0), "Radio de entrega": 2.0, "Platos": [{"Nombre": "Tofu", "Precio": 95.0}, {"Nombre": "Sopa", "Precio": 140.0}, {"Nombre": "Ensalada", "Precio": 130.0}, {"Nombre": "Hummus", "Precio": 400.0}, {"Nombre": "Leche de soya", "Precio": 120.0}, {"Nombre": "Leche de almendras", "Precio": 160.0}], "Total de ventas": 0.0},
    {"Nombre": "El Bar de Moe", "Direccion": "Av. Siempre Viva 742", "Telefono": "11-6673-5524", "Posicion":(15.0,-15.0), "Radio de entrega": 2.0, "Platos": [{"Nombre": "Duff", "Precio": 110.0}, {"Nombre": "Quilmes", "Precio": 105.0}, {"Nombre": "Llamarada Moe", "Precio": 120.0}, {"Nombre": "Destornillador", "Precio": 135.0}, {"Nombre": "El Fernet de Moe", "Precio": 150.0}], "Total de ventas": 0.0}]

    rappitenderos_hardcodeados = [
    {"Nombre": "Agustin Firmapaz", "Propina acumulada": 0.0, "Posicion actual": [0.0,0.0], "Pedido actual": {"Platos":[], "Destino": None}},
    {"Nombre": "Tomas Troglio", "Propina acumulada": 0.0, "Posicion actual": [0.0,0.0], "Pedido actual": {"Platos":[], "Destino": None}},
    {"Nombre": "Erik Anrique", "Propina acumulada": 0.0, "Posicion actual": [0.0,0.0], "Pedido actual": {"Platos":[], "Destino": None}},
    {"Nombre": "Santiago Gomez", "Propina acumulada": 0.0, "Posicion actual": [0.0,0.0], "Pedido actual": {"Platos":[], "Destino": None}},
    {"Nombre": "Ezequiel Busquin", "Propina acumulada": 0.0, "Posicion actual": [0.0,0.0], "Pedido actual": {"Platos":[], "Destino": None}}]

    clientes_hardcodeados = [
    {"Nombre": "Juancito123", "Contrasenia": "JuanK-po99", "Telefono": "11-7986-4012", "Direccion": "Alcorta 587", "Posicion": (-5.0,-5.8), "Rappicreditos": 0.0},
    {"Nombre": "Martita96", "Contrasenia": "Hipotenusa_34", "Telefono": "11-4615-7010", "Direccion": "9 de Julio 1795", "Posicion": (8.0,-17.0), "Rappicreditos": 0.0},
    {"Nombre": "Mirko42", "Contrasenia": "YngMirk_420", "Telefono": "11-6352-4871", "Direccion": "Av. Corrientes 735", "Posicion": (0.0,6.3), "Rappicreditos": 0.0},
    {"Nombre": "NatalyPortman", "Contrasenia": "pechugasLaru-6", "Telefono": "11-3569-2305", "Direccion": "Almirante Brown 215", "Posicion": (4.9,20.0), "Rappicreditos": 0.0},
    {"Nombre": "FedeRico74", "Contrasenia": "C-ontrasenia01", "Telefono": "11-5862-4799", "Direccion": "Av. Libertador 1369", "Posicion": (-2.0,5.0), "Rappicreditos": 0.0}]

    return restaurantes_hardcodeados, rappitenderos_hardcodeados, clientes_hardcodeados

def cargar_info_predefinida():
    l_restaurantes, l_rappitenderos, l_clientes = info_hardcodeada()
    for rappitendero in l_rappitenderos:
        rappitendero["Posicion actual"] = l_restaurantes[random.randrange(len(l_restaurantes))]["Posicion"]
    return l_restaurantes, l_rappitenderos, l_clientes

##################################################################################################################################################
########################################################## FUNCION 2 #####################################################################################
##################################################################################################################################################

#Funciones bases
def texto_long_max_min(max = 256, min = 0, mensaje_de_ingreso = ingreso_predeterminado):
    verificado = False
    while not verificado:
        texto = input(mensaje_de_ingreso)
        if min<=len(texto)<=max :
            verificado = True
        else:
            print(error_longitud, min, ",", max)
    return texto

#Funciones de validacion
def verificar_caracteres (caracteres_validos, texto):
    verificado = False
    caracter_invalido_encontrado = False
    for caracter in texto:
        if caracter not in caracteres_validos:
            caracter_invalido_encontrado = True
    if caracter_invalido_encontrado == False:
            verificado = True
    return verificado

def verificar_cadena_no_vacia(texto):
    verificado = False
    if texto != "":
        verificado = True
    return verificado

def validar_tipo_flotante(dato_ingresado):
    try:
        dato_ingresado = float(dato_ingresado)
        verificado = True
    except ValueError:
        verificado = False
    return verificado, dato_ingresado

def validar_flotante_positivo(numero):
    verificado = False
    es_flotante, numero = validar_tipo_flotante(numero)
    if es_flotante:
        if numero > 0:
            verificado = True
    return verificado, numero

def validar_tipo_entero(numero):
    es_entero = False
    while not es_entero:
        try:
            numero_entero = int(numero)
            es_entero = True
        except ValueError:
            print(error_tipo_entero)
            numero = input(ingrese_entero)
    return numero_entero

def verificar_contrasenia (contrasenia):
    verificado = False
    tiene_minus = tiene_mayus = tiene_num = tiene_sim = False
    for caracter in contrasenia:
        if caracter in minusculas:
            tiene_minus = True
        elif caracter in mayusculas:
            tiene_mayus = True
        elif caracter in numeros:
            tiene_num = True
        elif caracter in simbolos:
            tiene_sim = True
    if tiene_minus and tiene_mayus and tiene_num and tiene_sim:
        verificado = True
    return verificado

def verificar_existencia_de_datos_necesarios():
    existen_los_datos = False
    if l_restaurantes == []:
        print(requisito_existencia_restaurante)
    if l_rappitenderos == []:
        print(requisito_existencia_rappitendero)
    if l_clientes == []:
        print(requisito_existencia_cliente)
    if l_restaurantes != [] and l_rappitenderos != [] and l_clientes != []:
        existen_los_datos = True
    return existen_los_datos

#Funciones de carga
def cargar_real_positivo(mensaje_de_ingreso):
    numero_real = input(mensaje_de_ingreso)
    es_positivo, numero_real = validar_flotante_positivo(numero_real)
    while not es_positivo:
        print(error_dato_incorrecto)
        numero_real = input(mensaje_de_ingreso)
        es_positivo, numero_real = validar_flotante_positivo(numero_real)
    return numero_real

def cargar_direccion():
    direccion = input(ingrese_direccion)
    direccion_valida = verificar_cadena_no_vacia(direccion)
    while not direccion_valida:
        print(error_vacio)
        direccion = input(ingrese_direccion)
        direccion_valida = verificar_cadena_no_vacia(direccion)
    return direccion

def cargar_telefono():
    telefono = input(ingrese_telefono)
    telefono_valido = verificar_caracteres(telefonica, telefono)
    while not telefono_valido:
        print(error_caracter_invalido)
        telefono = input(ingrese_telefono)
        telefono_valido = verificar_caracteres(telefonica, telefono)
    return telefono

def cargar_coordenada(mensaje_de_ingreso_de_coordenada):
    coordenada = input(mensaje_de_ingreso_de_coordenada)
    coordenada_valida, coordenada = validar_tipo_flotante(coordenada)
    while not coordenada_valida:
        print(error_dato_incorrecto)
        coordenada = input(mensaje_de_ingreso_de_coordenada)
        coordenada_valida, coordenada = validar_tipo_flotante(coordenada)
    return coordenada

def cargar_posicion():
    latitud  = cargar_coordenada(ingrese_latitud)
    longitud = cargar_coordenada(ingrese_longitud)
    posicion = (latitud, longitud)
    return posicion

def cargar_primer_instancia_de_contrasenia():
    contrasenia = texto_long_max_min(min=8, mensaje_de_ingreso=ingrese_contrasenia)
    contrasenia_valida = verificar_contrasenia(contrasenia)
    while not contrasenia_valida:
        print(error_contrasenia_invalida)
        contrasenia = texto_long_max_min(min=8, mensaje_de_ingreso=ingrese_contrasenia)
        contrasenia_valida = verificar_contrasenia(contrasenia)
    return contrasenia

def cargar_contrasenia():
    print(requisitos_contrasenia)
    primer_instancia  = cargar_primer_instancia_de_contrasenia()
    segunda_instancia = input(reingrese_contrasenia)
    while primer_instancia != segunda_instancia:
        print(error_contrasenia_incorrecta)
        segunda_instancia = input(reingrese_contrasenia)
    return primer_instancia

def obtener_pos_restaurant():
    try:
        indice = random.randint(0,len(l_restaurantes))
        posicion_aleatoria = l_restaurantes[indice]["Posicion"]
    except IndexError:
        posicion_aleatoria = (random.uniform(-5,5),random.uniform(-5,5))
    return posicion_aleatoria

#Carga de datos ya existentes
def verificar_existencia(entidad_ingresada, lista_de_entidades):
    entidad_univoca = False
    duplicado = False
    for entidad in lista_de_entidades:
        if entidad["Nombre"] == entidad_ingresada:
            duplicado = True
    if not duplicado:
        entidad_univoca = True
    return entidad_univoca

def cargar_nombre_de_usuario():
    print(requisitos_usuario)
    usuario = texto_long_max_min(12, 3, ingrese_usuario)
    usuario_valido = verificar_caracteres(alfanum, usuario)
    usuario_unico  = verificar_existencia(usuario, l_clientes)
    while not usuario_valido or not usuario_unico:
        if not usuario_unico:
            print(error_info_duplicada)
        else:
            print(error_caracter_invalido)
        usuario = texto_long_max_min(12, 3, ingrese_usuario)
        usuario_valido = verificar_caracteres(alfanum, usuario)
        usuario_unico  = verificar_existencia(usuario, l_clientes)
    return usuario

def cargar_nombre_de_rappitendero():
    rappitendero = texto_long_max_min(mensaje_de_ingreso=ingrese_usuario)
    rappitendero_unico = verificar_existencia(rappitendero, l_rappitenderos)
    while not rappitendero_unico:
        print(error_info_duplicada)
        rappitendero = texto_long_max_min(mensaje_de_ingreso=ingrese_usuario)
        rappitendero_unico = verificar_existencia(rappitendero, l_rappitenderos)
    return rappitendero

def cargar_nombre_plato_o_restaurante(mensaje_de_ingreso_de_nombre, lista_platos_o_restaurantes):
    print(requisitos_plato)
    nombre = texto_long_max_min(25,5,mensaje_de_ingreso_de_nombre)
    nombre_unico = verificar_existencia(nombre, lista_platos_o_restaurantes)
    while not nombre_unico:
        print(error_info_duplicada)
        nombre = texto_long_max_min(25,5,mensaje_de_ingreso_de_nombre)
        nombre_unico = verificar_existencia(nombre, lista_platos_o_restaurantes)
    return nombre

#Plato
def cargar_plato():
    if l_restaurantes != []:
        cod_elec_rst = eleccion_restaurante(l_restaurantes)
        l_platos = l_restaurantes[cod_elec_rst-1]["Platos"]
        plato           = {}
        plato["Nombre"] = cargar_nombre_plato_o_restaurante(ingrese_plato, l_platos)
        plato["Precio"] = cargar_real_positivo(ingrese_precio)
        l_restaurantes[cod_elec_rst-1]["Platos"].append(plato)
        print("¡Listo! Se han añadido los nuevos platos")
        print("Volviendo al menu...")
    else:
        print(requisito_existencia_restaurante)
        

def carga_del_primer_plato():
    print(requisitos_primer_plato)
    plato           = {}
    plato["Nombre"] = texto_long_max_min(25,5,ingrese_plato)
    plato["Precio"] = cargar_real_positivo(ingrese_precio)
    return [plato]

#Restaurant

def cargar_restaurante():
    restaurante                    = {}
    restaurante["Nombre"]          = cargar_nombre_plato_o_restaurante(ingrese_restaurant, l_restaurantes)
    restaurante["Direccion"]       = cargar_direccion()
    restaurante["Telefono"]        = cargar_telefono()
    restaurante["Posicion"]        = cargar_posicion()
    restaurante["Radio"]           = cargar_real_positivo(ingrese_radio)
    restaurante["Platos"]          = carga_del_primer_plato()
    restaurante["Total de ventas"] = 0.0
    l_restaurantes.append(restaurante)
    print("¡Listo! Su restaurante a sido cargado.")
    print("Volvieno al menu...")

#Cliente
def cargar_cliente():
    cliente                = {}
    cliente["Nombre"]      = cargar_nombre_de_usuario()
    cliente["Contrasenia"] = cargar_contrasenia()
    cliente["Telefono"]    = cargar_telefono()
    cliente["Direccion"]   = cargar_direccion()
    cliente["Posicion"]    = cargar_posicion()
    cliente["Rappicreditos"]    = 0.0
    l_clientes.append(cliente)
    print("¡Listo! Los datos han sido cargados con exito")
    print("Volviendo al menu...")

#Rappitendero
def cargar_rappitendero():
    rappitendero = {}
    rappitendero["Nombre"]          = cargar_nombre_de_rappitendero()
    rappitendero["Propina acumulada"]         = 0.0
    rappitendero["Posicion actual"] = obtener_pos_restaurant()
    rappitendero["Pedido actual"]   = None
    l_rappitenderos.append(rappitendero)
    print("¡Listo! Los datos han sido cargados con exito")
    print("Volviendo al menu...")

###########################################################################################################################################
############################################################## FUNCION 3 ##################################################################
###########################################################################################################################################

def pedido_manual(l_restaurantes, l_rappitenderos, l_clientes):
    cod_cli = verif_cliente(l_clientes)
    print("Restaurantes disponibles: ")
    cod_elec_rst = eleccion_restaurante(l_restaurantes)
    l_platos = l_restaurantes[cod_elec_rst]["Platos"]
    l_pedido, costo_total = eleccion_plato(l_platos)
    l_pedido["Destino"] = l_clientes[cod_cli]["Posicion"]
    print("¡Listo! Su orden esta siendo emitida")
    cod_rapten = random.randrange(len(l_rappitenderos))
    print("Su rappitendero es: ", l_rappitenderos[cod_rapten]["Nombre"])
    l_rappitenderos[cod_rapten]["Pedido actual"] = l_pedido
    distancia = calc_tiempo_entrega(l_restaurantes, l_rappitenderos, l_clientes, cod_rapten, cod_elec_rst, cod_cli)
    print("Tiempo estimado de entrega: ", distancia/15, "hora/s")
    print("El rapitendero ha llegado a su destino")
    terminar_pedido(l_restaurantes, l_rappitenderos, l_clientes, cod_elec_rst, cod_rapten, cod_cli, costo_total)
    print("¡Muchas gracias por su compra!")
    print("Cerrando sesion...")
    

def verif_cliente(l_clientes):
    verif_nom = False
    while verif_nom == False:
        nombre = input("Ingrese su nombre de usuario: ")
        cont_cli = 0
        for cliente in l_clientes:
            if nombre == cliente["Nombre"]:
                verif_nom = True
                verif_contra = cliente["Contrasenia"]
                cod_cli = cont_cli
            cont_cli += 1 
        if verif_nom == False:
            print("El nombre ingresado no existe")  
    password = input("Ingrese su contraseña: ")
    while password != verif_contra:
        password = input("Contraseña incorrecta. Ingrese contraseña: ")
    return cod_cli
    
def eleccion_restaurante(l_restaurantes):
    cont_rst = 1
    for restaurante in l_restaurantes:
        print(cont_rst,". ", restaurante["Nombre"])
        cont_rst += 1
    cod_elec_rst_pre = input("Elija el numero de restaurante deseado: ")
    cod_elec_rst_pre = validar_tipo_entero(cod_elec_rst_pre)
    cod_elec_rst = verif_opcion(cod_elec_rst_pre, 1, cont_rst)
    return cod_elec_rst-1
    
def eleccion_plato(l_platos):
    costo_total = 0
    l_pedido_pre = {}
    l_pedido = {"Platos": [], "Destino": None}
    pedir = 1
    while pedir == 1:
        print("Platos disponibles: ")
        cont_pla = 1
        for plato in l_platos:
            print(cont_pla, ". ", plato["Nombre"],": $", plato["Precio"])
            cont_pla += 1
        cod_elec_plato_pre = input("Elija numero del plato deseado: ")
        cod_elec_plato_pre = validar_tipo_entero(cod_elec_plato_pre)
        maximo_pla = cont_pla
        cod_elec_plato = verif_opcion(cod_elec_plato_pre, 1, cont_pla)-1
        cant_elec_plato_pre = input("Elija la cantidad de platos a pedir (entre 1 y 10): ")
        cant_elec_plato_pre = validar_tipo_entero(cant_elec_plato_pre)
        cant_elec_plato = verif_opcion(cant_elec_plato_pre, 1, 11)
        elec_plato = l_platos[cod_elec_plato]["Nombre"]
        costo_plato = l_platos[cod_elec_plato]["Precio"]
        if elec_plato not in l_pedido_pre:
            l_pedido_pre[elec_plato] = cant_elec_plato
        else:
            l_pedido_pre[elec_plato] += cant_elec_plato
        print("Su orden es:")
        for orden in l_pedido_pre:
            print(orden, ": ", l_pedido_pre[orden])
        costo_total += costo_plato*cant_elec_plato
        print("Total: $", costo_total)
        pedir = input("¿Desea pedir otro plato? (1 = si; 0 = no): ")
        pedir = validar_tipo_entero(pedir)
    for orden in l_pedido_pre:
        l_pedido["Platos"].append((l_pedido_pre[orden], orden))
    return l_pedido, costo_total
    
    
def calc_tiempo_entrega(l_restaurantes, l_rappitenderos, l_clientes, cod_rapten, cod_elec_rst, cod_cli):
    l_rappitenderos[cod_rapten]["Destino"] = l_restaurantes[cod_elec_rst]["Posicion"] 
    lat_rst = l_rappitenderos[cod_rapten]["Destino"][0]
    lon_rst = l_rappitenderos[cod_rapten]["Destino"][1]
    lat_dom = l_clientes[cod_cli]["Posicion"][0]
    lon_dom = l_clientes[cod_cli]["Posicion"][0]
    distancia = 100*(((lat_rst-lat_dom)**2+(lon_rst-lon_dom)**2)**(1/2))
    return distancia
    #No calcula bien la distancia no se por que
    
    
def terminar_pedido(l_restaurantes, l_rappitenderos, l_clientes, cod_elec_rst, cod_rapten, cod_cli, costo_total):
    l_rappitenderos[cod_rapten]["Destino"] = l_clientes[cod_cli]["Posicion"]
    l_clientes[cod_cli]["Rappicreditos"] += rappicreditos(costo_total)
    print("Rappicreditos obtenidos: ", rappicreditos(costo_total))
    l_rappitenderos[cod_rapten]["Propina acumulada"] += costo_total*0.1
    l_restaurantes[cod_elec_rst]["Total de ventas"] += costo_total*0.9
   
def rappicreditos(gasto_total):
    if gasto_total < 200:
        rappicreditos = gasto_total*0.1
    elif gasto_total >= 200  and gasto_total <= 500:
        rappicreditos = gasto_total*0.15
    else:
        rappicreditos = gasto_total*0.2
    return rappicreditos

##########################################################################################################################################################
######################################################## FUNCION 4 #######################################################################################
##########################################################################################################################################################

def pedido_automatico(cod_rapten, cod_elec_rst, cod_cli, costo_total):
    print("¡Listo! Su orden esta siendo emitida")
    print("Su rappitendero es: ", l_rappitenderos[cod_rapten]["Nombre"])
    print("El rapitendero ha llegado a su destino")
    terminar_pedido(l_restaurantes, l_rappitenderos, l_clientes, cod_elec_rst, cod_rapten, cod_cli, costo_total)
    print("¡Muchas gracias por su compra!")
    print("Cerrando sesion...")

def carga_simulaciones(l_restaurantes, l_rappitenderos, l_clientes):
    numero_de_simulaciones_pre = input("Ingrese la cantidad de simulaciones que desea realizar entre 1 y 100, o ingrese 0 para volver al menu: ")
    numero_de_simulaciones_pre2 = validar_tipo_entero(numero_de_simulaciones_pre)
    numero_de_simulaciones = verif_opcion(numero_de_simulaciones_pre2, 0, 101)
    if numero_de_simulaciones != 0:
        max_platos_pedido_pre = input("Ingrese la cantidad maxima de platos por pedido, entre 1 y 9: ")
        max_platos_pedido_pre2 = validar_tipo_entero(max_platos_pedido_pre)
        max_platos_pedido = verif_opcion (max_platos_pedido_pre2,1,10)
        for i in range(numero_de_simulaciones):
            ran_cod_cli = random.randrange(len(l_clientes))
            ran_cod_rst = random.randrange(len(l_restaurantes))
            rad_cod_rapten = random.randrange(len(l_rappitenderos))
            gasto_total = 0
            for i in range(max_platos_pedido):
                gasto_total += l_restaurantes[ran_cod_rst]["Platos"][random.randrange(len(l_restaurantes[ran_cod_rst]["Platos"]))]["Precio"]*random.randrange(9)
            pedido_automatico(rad_cod_rapten, ran_cod_rst, ran_cod_cli, gasto_total)

##########################################################################################################################################################
######################################################## FUNCION 5 #######################################################################################
##########################################################################################################################################################
def informe(lista, parametro):
    l_informe = []
    for elem in lista:
        l_informe += [[elem["Nombre"], elem[parametro]]]
    l_ordenada = sorted(l_informe, key = lambda x:x[1], reverse = True)
    return l_ordenada

def imprimir_informe(l_informe):
    cont = 1
    for elem in l_informe:
        print(cont, ". ", elem[0], "; ", elem[1])
        cont += 1
    print("Fin del informe")

#Inicio de submenues

def submenu_cargar_info_manual(l_restaurantes, l_rappitenderos, l_clientes):
    opcion = -1
    minimo = 0
    maximo = 5
    while opcion != 0:
        print("1. Cargar nuevo restaurante")
        print("2. Cargar nuevo plato")
        print("3. Cargar nuevo cliente")
        print("4. Cargar nuevo rappitendero")
        opcion_pre = input("Seleccione la opcion que desee realizar. 0 para salir del menu: ")
        opcion_pre2 = validar_tipo_entero(opcion_pre)
        opcion = verif_opcion(opcion_pre2, minimo, maximo)
        if opcion != 0:
            opcion += 5
            derivar_opcion_carga_manual(opcion, l_restaurantes, l_rappitenderos, l_clientes)

def submenu_informes(l_restaurantes, l_rappitenderos, l_clientes):
    opcion = -1
    minimo = 0
    maximo = 4
    while opcion != 0:
        print("1. Clientes con mayor cantidad de Rappicreditos")
        print("2. Rappitenderos con mayor propina acumulada")
        print("3. Restaurantes con mas ventas")
        opcion_pre = input("Seleccione la opcion que desee realizar. 0 para salir del menu: ")
        opcion_pre2 = validar_tipo_entero(opcion_pre)
        opcion = verif_opcion(opcion_pre2, minimo, maximo)
        if opcion != 0:
            opcion += 9
            derivar_opcion_informes(opcion, l_restaurantes, l_rappitenderos, l_clientes)

#Fin de submenues

### Funciones de menu
### Funciones de derivar a menu

def derivar_opcion_carga_manual(opcion, l_restaurantes, l_rappitenderos, l_clientes):
    if opcion == 6:
        cargar_restaurante()
    elif opcion == 7:
        cargar_plato()
    elif opcion == 8:
        cargar_cliente()
    elif opcion == 9:
        cargar_rappitendero()


def derivar_opcion_informes(opcion, l_restaurantes, l_rappitenderos, l_clientes):
    if opcion == 10:
        print("Los 10 clientes con mayor cantidad de rappicreditos")
        parametro = "Rappicreditos"
        l_informe = informe(l_clientes, parametro)
        del(l_informe[10:])
        imprimir_informe(l_informe)
    elif opcion == 11:
        print("Rappitenderos con mayor propina acumulada")
        parametro = "Propina acumulada"
        l_informe = informe(l_rappitenderos, parametro)
        imprimir_informe(l_informe)
    else:
        print("Restaurantes que más ventas tuvieron.")
        parametro = "Total de ventas"
        l_informe = informe(l_restaurantes, parametro)
        imprimir_informe(l_informe)

def derivar_opcion_m_ppal(opcion, l_restaurantes, l_rappitenderos, l_clientes):
    if opcion == 2: 
        submenu_cargar_info_manual(l_restaurantes, l_rappitenderos, l_clientes)
    elif opcion == 3:
        listas_con_contenido = verificar_existencia_de_datos_necesarios()
        if listas_con_contenido == True:
            pedido_manual(l_restaurantes, l_rappitenderos, l_clientes)
    elif opcion == 4:
        listas_con_contenido = verificar_existencia_de_datos_necesarios()
        if listas_con_contenido == True:
            carga_simulaciones(l_restaurantes, l_rappitenderos, l_clientes)
    elif opcion == 5:
        submenu_informes(l_restaurantes, l_rappitenderos, l_clientes)

### Fin de derivaciones
### Funcion verificar opcion
def verif_opcion(opcion, minimo, maximo):
    while opcion < minimo or opcion >= maximo:
        opcion = input("Seleccione un numero valido: ")
        opcion = validar_tipo_entero(opcion)
    return opcion
### Fin opciones

###### BLOQUE PRINCIPAL ######

print("Bienvenido")
opcion = -1
minimo = 0
maximo = 6
cargado = False
while opcion != 0:
    print("1. Carga de datos predefinidos")
    print("2. Carga de nuevos datos")
    print("3. Pedido manual")
    print("4. Simulacion de pedidos")
    print("5. Informes")
    opcion_pre = input("Seleccione la opcion que desee realizar. 0 para salir del menu: ")
    opcion_pre2 = validar_tipo_entero(opcion_pre)
    opcion = verif_opcion(opcion_pre2, minimo, maximo)
    if opcion == 1:
        if cargado == False:
            l_restaurantes_aux, l_rappitenderos_aux, l_clientes_aux = cargar_info_predefinida()
            l_restaurantes  += l_restaurantes_aux
            l_rappitenderos += l_rappitenderos_aux
            l_clientes      += l_clientes_aux
            cargado = True
            print("Datos predefinidos cargados")
        else:
            print("Los datos predefinidos ya han sido cargados")
    elif opcion != 0:
        derivar_opcion_m_ppal(opcion, l_restaurantes, l_rappitenderos, l_clientes)
print("¡Hasta luego!")