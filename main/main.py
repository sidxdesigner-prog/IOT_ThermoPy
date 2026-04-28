import json
from clima.clima import clima
from tempo.tempo import tempo

def max_and_min(day, data):
    min_temp = max_temp = data[day][0]["temperatura"]
    for leitura in data[day]:
        if leitura["temperatura"] >= max_temp:
            max_temp = leitura["temperatura"]
        if leitura["temperatura"] <= min_temp:
            min_temp = leitura["temperatura"]
    return max_temp, min_temp

                
def main(num):
    temperatura = 28
    potencia = 2.3
    reads = 3
    data = {}
    day = f"dia_{num + 1}"
    temp_day = f"dia_{num}"
    max_temp = 100.0
    min_temp = -100.0
    
    if day != "dia_1":
        with open('./sensor.json','r', encoding="utf-8") as main_file:
            data = json.load(main_file)
            
    if day not in data:
        data[day] = []

    dic_of_clima= clima(temp_day, day, temperatura)
    tendencia = dic_of_clima[-1]["tendencia"]
    dic_of_clima.pop()
    temperatura = dic_of_clima[-1]["temperatura"]
    
    for value in dic_of_clima:
        data[day].append(value)
        
    action_aircondtioner, action_heater, dict_of_tempo = tempo(day, tendencia, potencia, temperatura, reads)
    

    for value in dict_of_tempo:
        data[day].append(value)
        
    with open('./sensor.json', 'w', encoding="utf-8") as temp_file:
        json.dump(data, temp_file, ensure_ascii=False, indent=2)

    max_temp, min_temp = max_and_min(day, data)
    
    return action_aircondtioner, action_heater, max_temp, min_temp
