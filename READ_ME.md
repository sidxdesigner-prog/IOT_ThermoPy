1. Preparação (O que o programa precisa saber antes de começar)

Definir Limites: Criar constantes para as temperaturas de controle (30, 27, 18, 21).


Estado Inicial: Criar variáveis para saber se o ventilator e o aqueduct estão desligados no início.


Estatísticas: Criar variáveis para guardar a Temp_Máxima, Temp_Mínima e os contadores de acionamento.
INÍCIO
    CARREGAR dados do arquivo "sensor.json"
    
    PARA CADA leitura EM dados:
        1. IDENTIFICAR Temperatura e Timestamp atuais [cite: 7, 8]
        
        2. LÓGICA DO VENTILADOR (Histerese):
           SE Temperatura >= 30 E Ventilador está DESLIGADO:
               LIGAR Ventilador, SALVAR ação e AUMENTAR contador [cite: 14, 22, 26]
           SENÃO SE Temperatura <= 27 E Ventilador está LIGADO:
               DESLIGAR Ventilador e SALVAR ação [cite: 15, 22]
               
        3. LÓGICA DO AQUECEDOR (Histerese):
           SE Temperatura <= 18 E Aquecedor está DESLIGADO:
               LIGAR Aquecedor, SALVAR ação e AUMENTAR contador [cite: 16, 22, 27]
           SENÃO SE Temperatura >= 21 E Aquecedor está LIGADO:
               DESLIGAR Aquecedor e SALVAR ação [cite: 17, 22]
               
        4. ATUALIZAR ESTATÍSTICAS (Máxima e Mínima)
        
    FIM DO LOOP
    
    SALVAR lista de ações no arquivo "acoes.json" [cite: 22, 47]
    EXIBIR resumo final na tela [cite: 23]
FIM