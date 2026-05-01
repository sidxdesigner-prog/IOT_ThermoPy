import random, time, json


def executar_simulacao_climatica(indice_sensor, nome_do_dia, temperatura_inicial):
    
    # Lista com possiveis variações de temperatura
    variacoes = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
    
    print(temperatura_inicial)
    # Se não for o primeiro dia, tenta recuperar dados antigos
    if nome_do_dia != "dia_1":
        try:
            with open("./sensor.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                
                # Pega a temperatura do indice informado
                temperatura_inicial = dados[indice_sensor][-1]["temperatura"]
        
        except:
            pass
    
    print(temperatura_inicial)
    
    # Escolhe uma variacao aleatoria
    variacao_escolhida = random.choice(variacoes)

    
    registros = []
    
    # Primeira Medicao (sem mudanca)
    horario1 = time.time()
    registros.append({
        "timestamp": horario1,
        "temperatura": temperatura_inicial
    })
    
    print(temperatura_inicial)
    
    
    
    # SEGUNDA MEDIÇÃO (com mudança)
    temperatura_final = temperatura_inicial + variacao_escolhida
    
    horario2 = time.time()
    registros.append({
        "timestamp": horario2,
        "temperatura": temperatura_final
    })
    print(temperatura_inicial)
    
    temp1 = registros[0]["temperatura"]
    temp2 = registros[1]["temperatura"]
    
    if temp1 > temp2:
        tendencia = "frio"
    else:
        tendencia = "calor"

    registros.append({"tendencia" : tendencia})
    

    
    return registros