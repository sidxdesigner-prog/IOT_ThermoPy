
1. Função de Suporte: Contagem de Ativações
O que ela recebe: O identificador do dia e o dicionário completo de ações.

Lógica de análise:

Inicie dois contadores zerados: um para o ar-condicionado e outro para o aquecedor.

Acesse a lista de registros referente ao dia específico dentro do dicionário de ações.

Percorra cada item dessa lista e verifique o texto da ação realizada.

Verifique se o texto indica que o ar-condicionado foi ligado; se sim, incremente o contador correspondente.

Verifique se o texto indica que o aquecedor foi ligado; se sim, incremente o outro contador.

O que ela entrega: O valor total de ativações do ar-condicionado e o valor total de ativações do aquecedor.

2. Função Principal: Processamento de Tempo
O que ela recebe: dia, tendencia, potencia, temperatura e quantidade_de_leituras.

Preparação de Terreno:

Defina valores padrão para o tempo de referência e a taxa de mudança de graus.

Crie uma estrutura para armazenar o estado atual dos aparelhos (ambos começando como "falso" ou desligado).

Prepare uma lista vazia para salvar o histórico de temperaturas que será gerado.

Carregamento de Dados:

Se o dia não for o "dia_1", tente abrir o arquivo JSON que guarda as ações.

Certifique-se de que o dia atual possua uma lista própria dentro desse arquivo para receber novos registros.

Ciclo de Simulação (Repetir pela quantidade de leituras solicitada):

Verificação de Dispositivos: Avalie a temperatura atual para decidir se os aparelhos devem ser ligados ou desligados e calcule o quanto eles vão afetar o clima (variação).

Influência do Clima: * Se a tendência for "frio", subtraia da temperatura o valor da mudança natural menos a resistência gerada pelo aparelho ligado.

Se a tendência for "calor", some à temperatura o valor da mudança natural menos a resistência gerada pelo aparelho ligado.

Registro de Eventos: * Capture o horário atual do sistema e adicione o par "horário e temperatura" à sua lista de histórico.

Se houve uma mudança de estado (ligar/desligar), registre o horário e qual foi a ação no dicionário de ações.

Persistência e Finalização:

Salve o dicionário de ações atualizado de volta no arquivo JSON.

Chame a Função de Suporte (citada acima) passando o dia e o dicionário para obter os totais de uso.

O que ela entrega (Retorno triplo): 
1.  O número total de vezes que o ar-condicionado ligou.
2.  O número total de vezes que o aquecedor ligou.
3.  A lista completa com todos os registros de temperatura e horários.