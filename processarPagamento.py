import json

def lambda_handler(event, context):
    pedido_id = event.get('pedido_id')
    
    # Lógica fictícia de pagamento
    status_pagamento = "Pagamento aprovado"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "pedido_id": pedido_id,
            "status_pagamento": status_pagamento
        })
    }
