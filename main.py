import time, json, random

temperatura_Celsius = [22, 24, 31, 33, 29, 26, 17, 11, 35, 14, 10, 25]
event_Celcius = ["dia_quente", "dia_frio"]
timestamp = time.time()
ventilador = False
aquecedor = False
ativar_Ventilador = 30
desativar_Ventilador = 27
ativar_Aquecedor = 18
desativar_Aquecedor = 21
max_Temperatura = -100
min_Temperatura = 100
ativados_Ventilador = 0
ativados_Aquecedor = 0
looping = 0
conteudo = []

def sortear():
    for i in range(5):
        timetime = timestamp + (60 * i)
        temp = random.choice(temperatura_Celsius)
        conteudo.append({"timestamp": timetime, "temperatura": temp})
    with open("sensor.json", "w+", encoding="utf-8") as temperatura_file_Out:
        json.dump(conteudo, temperatura_file_Out, ensure_ascii = False, indent = 2)

#def diaQuente():

#def diaFrio():

#def verificar_temperatura():


#with open("sensor.json", "r", encoding="utf-8") as temperatura_file:
   # conteudo = json.load(temperatura_file)
sortear()

