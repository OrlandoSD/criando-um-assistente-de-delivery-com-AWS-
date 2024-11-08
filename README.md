Exemplo de Workflow de Entrega com AWS Step Functions e Lambda
Este projeto é um exemplo de fluxo de delivery com funções AWS Lambda e AWS Step Functions.

Estrutura do Projeto
lambdas/receber_pedido.py: Função Lambda que simula o recebimento de um pedido.
lambdas/processar_pagamento.py: Função Lambda que simula o processamento de pagamento.
lambdas/despachar_pedido.py: Função Lambda que simula o despacho do pedido.
statemachine/statemachine_definition.json: Definição do fluxo da Step Function em JSON.
Como Usar
Clone o repositório e, quando desejar implantar, use o console da AWS para:

Criar funções Lambda com os códigos fornecidos.
Criar uma Step Function usando a definição em statemachine_definition.json.
