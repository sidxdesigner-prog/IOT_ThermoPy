import time, json, random

shuffle = [+ 5,- 7,+ 6,- 7,- 5,+ 8,+ 5,+ 4,]
dia_temp = ""

def clima(dia, temp, list_temp):
    lista = []
    global dia_temp

    if dia == "dia_1":
        clock = time.time()
        lista.append({"timestamp": clock, "temperatura": temp})
        temp = random.choice(list_temp)
        time.sleep(0.2)
        clock = time.time()
        lista.append({"timestamp": clock, "temperatura": temp})
    else:  
        with open('IOT/Python/Atividade_em_grupo_01/sensor.json', 'r+', encoding="utf-8") as dados:
            conteudo = json.load(dados)         
        clock = time.time()
        lista.append({"timestamp": clock, "temperatura": conteudo[dia_temp][-1]["temperatura"]})
        time.sleep(0.2)
        clock = time.time()
        lista.append({"timestamp": clock, "temperatura": conteudo[dia_temp][-1]["temperatura"] + random.choice(shuffle)})
        
    dia_temp = dia   
            
    if lista[0]["temperatura"] > lista[1]["temperatura"]:
        lista.append({"tendencia": "frio"})
    else:
       lista.append({"tendencia": "quente"})

    return lista
