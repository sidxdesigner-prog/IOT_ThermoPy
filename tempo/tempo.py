import random, time, json

# FUNÇÃO 2: CONTAGEM DE ATIVAÇÕES

def contar_ativacoes(dia, acoes):

    contador_ar = 0
    contador_aquecedor = 0

    lista = acoes[dia]

    for item in lista:

        texto = item["acao"]

        if texto == "ar ligado":
            contador_ar += 1

        if texto == "aquecedor ligado":
            contador_aquecedor += 1

    return contador_ar, contador_aquecedor



# FUNÇÃO 3: PROCESSAMENTO DE TEMPO

def processamento_tempo(dia, tendencia, potencia, temperatura, quantidade_de_leituras):

    referencia = 5
    graus = 1

    aparelhos = {
        "ar": False,
        "aquecedor": False
    }

    historico = []

    # Carregar JSON
    try:
        with open('tempo/acoes.json', 'r', encoding="utf-8") as arquivo:
            acoes = json.load(arquivo)
    except:
        acoes = {}

    if dia not in acoes:
        acoes[dia] = []

    # Simulação
    for _ in range(quantidade_de_leituras):

        variacao = 0
        acao_realizada = None

        # Controle dos aparelhos
        if temperatura >= 30:
            if aparelhos["ar"] == False:
                aparelhos["ar"] = True
                aparelhos["aquecedor"] = False
                acao_realizada = "ar ligado"

            variacao = potencia * referencia

        elif temperatura <= 18:
            if aparelhos["aquecedor"] == False:
                aparelhos["aquecedor"] = True
                aparelhos["ar"] = False
                acao_realizada = "aquecedor ligado"

            variacao = potencia * referencia

        else:
            aparelhos["ar"] = False
            aparelhos["aquecedor"] = False

        # Tendência climática
        if tendencia == "frio":
            temperatura -= (graus - variacao)

        else:
            temperatura += (graus - variacao)

        horario = time.time()

        historico.append({
            "timestamp": horario,
            "temperatura": round(temperatura, 2)
        })

        # Registrar ação
        if acao_realizada:
            acoes[dia].append({
                "timestamp": horario,
                "acao": acao_realizada
            })

        time.sleep(1)

    # Salvar JSON
    with open('tempo/acoes.json', 'w', encoding="utf-8") as arquivo:
        json.dump(acoes, arquivo,ensure_ascii= False , indent=4)

    total_ar, total_aquecedor = contar_ativacoes(dia, acoes)

    return total_ar, total_aquecedor, historico