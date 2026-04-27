import time, json, random

referencia = 5
graus = 1

def time_of_change(potencia, temp, estado):
    resultado = ""

    if 'arconditioner' in estado:
        if temp >= 30 and estado["arconditioner"] != True:
            estado["arconditioner"] = True
            resultado = "arcondicionado Ligado"
        elif temp >= 30 and estado["arconditioner"] == True:
            temp = temp - (potencia * referencia)
        elif temp <= 27 and estado["arconditioner"] == True:
            estado["arconditioner"] = False
            resultado = "arcondicionado Desligado"
    if 'heater' in estado:
        if temp <= 18 and estado["heater"] != True:
            estado["heater"] = True
            resultado = "aquecedor Ligado"
        elif temp <= 18 and estado["heater"] == True:
            temp = temp + (potencia * referencia)
        elif temp >= 27 and estado["heater"] == True:
            estado["heater"] = False
            resultado = "aquecedor Desligado"
    return temp, resultado, estado

def tempo(dia, tendencia, potencia, temp, reads):
    
    estado = {"arconditioner"  : False, "heater" : False}
    lista = []
    action = {}
    action["Ações"]= []
    

    if dia != "dia_1":
        with open('tempo/acoes.json', 'r+', encoding="utf-8") as action_file:
            action = json.load(action_file)

    action["Ações"].append(dia)

    for k in range(reads):  

        temp, resultado, estado = time_of_change(potencia, temp, estado)

        if tendencia == "frio":
            temp = temp - (graus * referencia)

        else:
            temp = temp + (graus + referencia)

        clock = time.time()
        lista.append({"timestamp" : clock, "temperatura" : temp})

        if resultado != "":
            clock = time.time()
            action["Ações"].append({"timestamp": clock, "ação" : resultado})

    with open('tempo/acoes.json', 'w+', encoding="utf-8") as action_file:
        json.dump(action, action_file, ensure_ascii= False, indent=2)

    estado = {"arconditioner"  : False, "heater" : False}
    
    return lista