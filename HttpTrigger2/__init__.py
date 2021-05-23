import logging
from database_connection import update_restaurant
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
        chef = req_body['chef_principal']
        status_code = update_restaurant(id_restaurante, nombre_restaurante, especialidad, color, logo, chef)
        if(status_code == 200):
            response = {"r": "Usuario actualizado con exito", "status_code": 200}
            response = json.dumps(response)
            return func.HttpResponse(response, status_code=200)
        else:
            print("ERROR FATAL")
            return func.HttpResponse('ERROR FATAL', status_code=500)
    except Exception as e:
        print(f"Excepcion: {e}")
        return func.HttpResponse(f'ERROR:{e}', status_code=500)