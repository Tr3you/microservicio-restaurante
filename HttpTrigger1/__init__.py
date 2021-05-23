import logging
from database_connection import add_new_restaurant
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        id_restaurante = req_body['id_restaurante']
        nombre_restaurante = req_body['nombre_restaurante']
        especialidad = req_body['especialidad']
        color =req_body['color']
        logo = req_body['logo']
        chef = req_body['chef']
        status_code = add_new_restaurant(id_restaurante, nombre_restaurante, especialidad, color, logo, chef)
        if(status_code == 200):
            response = {"r": "Usuario añadido con exito", "status_code": 200}
            response = json.dumps(response)
            return func.HttpResponse(response, status_code=200)
        else:
            return func.HttpResponse('ERROR FATAL', status_code=500)
    except Exception as e:
        return func.HttpResponse(f'ERROR:{e}', status_code=500)
