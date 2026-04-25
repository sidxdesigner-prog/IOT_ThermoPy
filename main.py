import time, json, random, randomClima
import time

temperatura_iniciais = [18, 19, 20, 34, 35, 36]
timestamp = 0
temperatura = 28
tendencia = 1
potencia = 2.3
max_Temperatura = -100
min_Temperatura = 100
ativados_Ventilador = 0
ativados_Aquecedor = 0
clima = ["dia_quente", "dia_frio"]
dev_1 = "Pedro"
dev_2 = "Alexandre"
gerente = "SID_Devops"


def main(loop):
    reads = 5
    data = {}
    for i in range(loop):
        air_conditioner = False
        heater = False
        key = f"dia_{i + 1}"
        print(f"iniciando o {i + 1}º dia ")
        if key not in data:
            data[key] = []
        for k in range(reads):
            timestamp = time.time()
            if key == "day_1" and (data[key]["temperatura"] == none or data[key]["temperatura"] == null ):
                value = randomClima(timestamp, temperatura, temperatura_iniciais)
            else:


print("-" * 40)
print("Seja bem vindo ao simulador de alteração de temperatuas com IOT")
print(f"Sistema desenvolvido por {dev_1}, {dev_2} e {gerente}")
print("-" * 40, "\n")
looping = int(input("de quantos dias deseja gerar o relátorio? "))
main(looping)


