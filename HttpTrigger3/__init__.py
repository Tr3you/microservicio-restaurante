import logging
import json
from database_connection import get_restaurant

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        id_restaurante = req_body['id_restaurante']
        status_code, data = get_restaurant(id_restaurante)
        if(status_code == 200):
            response = {
                "id_restaurante": data['id_restaurante'],
                "nombre_restaurante": data['nombre_restaurante'],
                "color": data['color'],
                "logo": data['logo'],
                "chef_principal": data['chef'],
                "especialidad": data['especialidad']
            }
            response = json.dumps(response)
            return func.HttpResponse(response, status_code=200)
        else:
            return func.HttpResponse('ERROR FATAL', status_code=500)
    except Exception as e:
        return func.HttpResponse(f'ERROR:{e}', status_code=500)