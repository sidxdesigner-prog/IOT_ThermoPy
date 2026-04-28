Arquivo: clima.py
Função: executar_simulacao_climatica
Argumentos: indice_sensor, nome_do_dia, temperatura_inicial

Preparação inicial:

Crie uma lista contendo diversos valores de variação (positivos e negativos).

Recuperação de estado:

Verifique se o nome_do_dia informado é diferente de "dia_1".

Caso seja um dia avançado, abra o arquivo de registros, localize a posição indicada pelo indice_sensor e extraia o último valor de temperatura salvo para atualizar a temperatura_inicial.

Geração de mudança:

Escolha aleatoriamente um valor daquela lista de variações criada no início.

Ciclo de medição (executar 2 vezes):

Na primeira vez, mantenha a temperatura como está. Na segunda, some a variação escolhida ao valor atual.

Em cada etapa, pause a execução por um breve instante, capture o horário do sistema e guarde o par "horário e temperatura".

Análise de tendência:

Compare se o valor da primeira temperatura registrada é maior que o da segunda.

Se for maior, anote que o clima tende a "frio"; caso contrário, anote que tende a "calor".

Retorno:

Entregue uma lista contendo todos os registros de temperatura e a tendência final.