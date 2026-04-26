import time, json, random

referencia = 5
graus = 1
arconditioner = False
heater = False


def isFrezze(potencia, temp):
    
    global heater
    
    if heater == False:
        temp = temp - (graus * referencia)
        if temp <= 18:
            heater = True
            return temp,"aquecedor ligado"
        else:
            return temp,"null"
    else:
        temp = (temp - (graus * referencia)) + (potencia * referencia)
        if temp >= 21:
            heater = False
            return temp,"aquecedor desligado"
        else:
            return temp, "null"

    
def isHot(potencia, temp):
    
    global arconditioner
    
    if arconditioner == False:
        if temp >= 30:
            arconditioner = True
            temp = (temp + (graus * referencia)) - (potencia * referencia)
            return temp,"arcondionado ligado"
        else:
            temp = temp + (graus * referencia)
            return temp,"null"
    else:
        if temp <= 27:
            arconditioner = False
            temp = (temp + (graus * referencia))
            return temp,"arcondionado desligado"
        else:
            temp = (temp + (graus * referencia)) - (potencia * referencia)
            return temp,"null"

     
def tempo(dia, tendencia, potencia, temp, reads):
    
    global arconditioner, heater
    
    lista = []
    action = {}
    action["Ações"] = [dia]
    
    if dia == "dia_1":
        
        for k in range(reads):  
            
            time.sleep(0.1)
            
            if tendencia == "frio":
                
                temp, resultado =  isFrezze(potencia, temp)

                clock = time.time()
                lista.append({"timestamp": clock, "temperatura": temp})
                
                if resultado != "null":
                    leitura_nome = f"leitura_{k+3}"
                    action["Ações"].append({leitura_nome:{"timestamp": clock, "Ação" : resultado}})
                    
            else:
                temp, resultado =  isHot(potencia, temp)
                
                clock = time.time()
                lista.append({"timestamp": clock, "temperatura": temp})
                
                if resultado != "null":
                    leitura_nome = f"leitura_{k+3}"
                    action["Ações"].append({leitura_nome:{"timestamp": clock, "Ação" : resultado}})
                    
        with open('IOT/Python/Atividade_em_grupo_01/tempo/acoes.json', 'w+', encoding="utf-8") as action_file:
            json.dump(action, action_file, ensure_ascii= False, indent=2)
    else:
        with open('IOT/Python/Atividade_em_grupo_01/tempo/acoes.json', 'r+', encoding="utf-8") as dados:
            conteudo = json.load(dados)

        conteudo["Ações"].append(dia)
        
        for k in range(reads):  
            
            if tendencia == "frio":
                
                temp, resultado =  isFrezze(potencia, temp)
                
                clock = time.time()
                lista.append({"timestamp": clock, "temperatura": temp})
                
                if resultado != "null":
                    leitura_nome = f"leitura_{k+3}"
                    conteudo["Ações"].append({leitura_nome:{"timestamp": clock, "Ação" : resultado}})
                    
            else:
                temp, resultado =  isHot(potencia, temp)
                
                clock = time.time()
                lista.append({"timestamp": clock, "temperatura": temp})
                
                if resultado != "null":
                    leitura_nome = f"leitura_{k+3}"
                    conteudo["Ações"].append({leitura_nome:{"timestamp": clock, "Ação" : resultado}})
                    
        with open('IOT/Python/Atividade_em_grupo_01/tempo/acoes.json', 'w+', encoding="utf-8") as action_file:
            json.dump(conteudo, action_file, ensure_ascii= False, indent=2)
                          
    arconditioner = False
    heater = False
        
    return lista      