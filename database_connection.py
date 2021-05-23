import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_new_restaurant(id_restaurante, nombre_restaurante, especialidad, color, logo, chef):
    try: 
        db.collection('restaurantes').document(str(id_restaurante)).set({
            'id_restaurante': id_restaurante, 
            'nombre_restaurante':nombre_restaurante,
            'especialidad': especialidad, 
            'color': color, 
            'logo': logo,
            'chef':chef
        })
        return 200
    except:
        return 500


def update_restaurant(id_restaurante, nombre_restaurante, especialidad, color, logo, chef):
    try: 
        db.collection('restaurantes').document(str(id_restaurante)).update({
            'id_restaurante': id_restaurante, 
            'nombre_restaurante':nombre_restaurante,
            'especialidad': especialidad, 
            'color': color, 
            'logo': logo,
            'chef':chef
        })
        return 200
    except:
        return 500


def get_restaurant(id_restaurante):
    try:
        result = db.collection('restaurantes').document(str(id_restaurante)).get()
        if result.exists:
            return 200, result.to_dict()
    except:
        return 500, {}