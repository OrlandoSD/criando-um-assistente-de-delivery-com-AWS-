import json

def lambda_handler(event, context):
    pedido_id = event.get('pedido_id', 'N/A')
    produto_id = event.get('produto_id', 'N/A')
    quantidade = event.get('quantidade', 0)
    
    # Lógica fictícia para receber pedido
    status = "Pedido recebido com sucesso."
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "pedido_id": pedido_id,
            "status": status
        })
    }
