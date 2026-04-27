import time, json, random
from clima.clima import clima
from tempo.tempo import tempo

temperatura_iniciais = [18, 19, 20, 34, 35, 36]
temperatura = 28
potencia = 2.3
timestamp = time.time()
fluxo = 25
temporizador = 0.05
dev_1 = "Alexandre"
dev_2 = "Pedro"
gerente = "SID_Devops"


def main(loop):
    global potencia, temperatura_iniciais, temperatura
    reads = 3
    data = {}
    for i in range(loop):
        
        key = f"dia_{i + 1}"
        print(f"\n iniciando o {i + 1}º dia ")
        
        print("\n loading ", end="")
        for j in range (fluxo):
            time.sleep(temporizador)
            print(".", end="", flush="True")
            
        if key not in data:
            data[key] = []
            
        print("")
        print("\n verificando tendencia ", end="")
        for j in range (fluxo - 14):
            time.sleep(temporizador)
            print(".", end="", flush="True")  

        dias= clima(key, temperatura, temperatura_iniciais)
        tendencia = dias[-1]["tendencia"]
        dias.pop()
        temperatura = dias[-1]["temperatura"]
        
        for a in range(len(dias)):
            data[key].append(dias[a])
            
        print("")
        print("\n gerando relatório ", end="")
        for j in range (fluxo - 10):
            time.sleep(temporizador)
            print(".", end="", flush="True")
                
        for k in range(reads):
            leituras = tempo(key, tendencia, potencia, temperatura, reads)

        for a in range(len(leituras)):
            data[key].append(leituras[a])

        print("")
        print("\n salvando arquivo ", end="")
        for j in range (fluxo - 9):
            time.sleep(temporizador)
            print(".", end="", flush="True")
            
        with open('sensor.json', 'w+', encoding="utf-8") as temp_file:
            json.dump(data, temp_file, ensure_ascii=False, indent=2)
            
    
        



print("-" * 65)
print("Seja bem vindo ao simulador de alteração de temperatuas com IOT")
print(f"    Sistema desenvolvido por {dev_1}, {dev_2} e {gerente}")
print("-" * 65, "\n")
looping = int(input("de quantos dias deseja gerar o relátorio? "))
main(looping)

