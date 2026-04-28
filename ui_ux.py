import time
from main.main import main
dev_1 = "Alexandre"
dev_2 = "Pedro"
gerente = "SID_Devops"
repeat= 25
temporizador = 0.05


print("-" * 65)
print("Seja bem vindo ao simulador de alteração de temperatuas com IOT")
print("-" * 65, "\n")
looping = int(input("de quantos dias deseja gerar o relátorio? "))

for num in range(looping):
    
    action_airconditioner, action_heater, max_temp, min_temp = main(num)
    print(f"\n iniciando o {num + 1}º dia ")

    print("\n loading ", end="")
    for ponto in range (repeat):
        time.sleep(temporizador)
        print(".", end="", flush=True)
    print("")

    print("\n verificando tendencia ", end="")
    for ponto in range (repeat - 14):
        time.sleep(temporizador)
        print(".", end="", flush=True)
    print("")

    print("\n gerando relatório ", end="")
    for ponto in range (repeat - 10):
        time.sleep(temporizador)
        print(".", end="", flush=True)
    print("")
    
    print("\n salvando arquivo ", end="")
    for ponto in range (repeat - 9):
        time.sleep(temporizador)
        print(".", end="", flush=True)
    print("")


    print(f"\nRelátorio do {num+1}º dia")
    print(f"\na temperatura Máxima foi {max_temp}º graus Celsius:")
    time.sleep(0.2)
    print(f"\na temperatura Mínima foi {min_temp}º graus Celsius:")
    time.sleep(0.2)

    if action_airconditioner != 0:
        print(f"\no arcondicionado foi ativado {action_airconditioner} vez(es)")
    else:
        print(f"\nnão houve acionamentos do arcondicionado hoje")
    time.sleep(0.2)

    if action_heater != 0:
        print(f"\no aquecedor foi ativado {action_heater} vez(es)")
    else:
        print(f"\nnão houve acionamentos do aquecedor hoje")

    input("\npressione qualquer tecla para continuar.....\n")

print("-" * 65)
print("Obrigado por participar da versão beta desde projeto")
print(f"Sistema desenvolvido por {dev_1}, {dev_2} e {gerente}")
print("-" * 65, "\n")