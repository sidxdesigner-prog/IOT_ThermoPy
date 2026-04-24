Este projeto simula um ambiente monitorado por sensores de temperatura e controlado por atuadores (Ar-condicionado e Aquecedor), processando a variação climática em tempo real.

O sistema é dividido em três blocos fundamentais que interagem sequencialmente:

1. main() - O Orquestrador
É o coração do programa. Responsável por gerenciar o fluxo de execução e a interface com o usuário.

Gerenciamento de Dados: Organiza variáveis globais e locais, além de estruturar o dicionário base para o JSON.
Loop Principal: Controla a passagem dos dias (ex: 5 dias) e o cronômetro interno (30s por dia).
Controle de Tempo: Utiliza time.sleep(5) para ditar o ritmo das leituras.
Persistência (JSON): Realiza a abertura e fechamento do arquivo, além de calcular estatísticas (Maior e Menor temperatura registrada) para o relatório final.
Exibição: Renderiza a "GUI" no terminal com o status atual de cada ciclo.

3. clima() - O Estrategista
Módulo responsável pela imprevisibilidade da natureza no simulador.

Definição de Tendência: Sorteia o comportamento térmico do dia (Quente ou Frio) logo após o valor inicial.
Ponto de Partida: Define o valor inicial (ou herda do dia anterior) para estabilizar a curva de variação.
Retorno: Entrega a "direção" do clima para que o motor de processamento saiba o que calcular.

3. tempo() - O Motor de Processamento  
Onde a "física" do ambiente acontece.

Cálculo Térmico: Soma ou subtrai graus com base na tendência definida pelo módulo clima().
Lógica de Atuadores: Decide o estado (LIGADO/DESLIGADO) do Ar-condicionado e do Aquecedor.
Balanço de Forças: Executa a compensação (Potência do aparelho vs. Tendência natural).
Registro de Ações: Retorna o timestamp e a ação executada para serem salvos no JSON.

🛠️ Fluxo de Funcionamento (Pipeline)
O usuário define a quantidade de dias.
main() cria a estrutura do dicionário e abre o arquivo JSON.
clima() sorteia a tendência do dia.
O loop while inicia:
tempo() calcula a nova temperatura.
tempo() ativa/desativa aparelhos.
main() exibe no console e salva no JSON.
time.sleep(5) aguarda o próximo ciclo.
Ao final, o JSON é fechado e o relatório de Max/Min é exibido.
