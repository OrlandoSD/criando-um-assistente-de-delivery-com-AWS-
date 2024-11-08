import json

def lambda_handler(event, context):
    pedido_id = event.get('pedido_id')
    
    # Lógica fictícia para despachar pedido
    status_envio = "Pedido despachado"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "pedido_id": pedido_id,
            "status_envio": status_envio
        })
    }
