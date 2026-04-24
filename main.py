import time, json, random
from clima.clima import clima
from tempo.tempo import tempo

temperatura_iniciais = [18, 19, 20, 34, 35, 36]
temperatura = 28
tendencia = 1
potencia = 2.3
timestamp = time.time()
dev_1 = "Alexandre"
dev_2 = "Pedro"
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
        climas = clima()
        data[key].append(climas)
        records = [tempo()]
        data[key].append(records)
        print(data)



print("-" * 65)
print("Seja bem vindo ao simulador de alteração de temperatuas com IOT")
print(f"    Sistema desenvolvido por {dev_1}, {dev_2} e {gerente}")
print("-" * 65, "\n")
looping = int(input("de quantos dias deseja gerar o relátorio? "))
main(looping)

