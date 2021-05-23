# Microservicio Restaurante

Microservicio desarrollado en python y desplegado en Azure Functions para la aplicacion web RestBit. Este microservicio se encarga de administrar la creacion, la actualizacion y la recuperacion de la informacion de los restaurante dentro de la plataforma.

#### URL: 'https://microservicio-restaurante.azurewebsites.net/api

# Funciones

#### method = POST | endpoint: /httptrigger1'

Json request body:

{  

    "id_restaurante": int,  
    "nombre_restaurante": string,  
    "especialidad": string,  
    "chef": string,  
    "color": string,  
    "logo": string  
  
}

#### method = PUT | endpoint: /httptrigger2'

Json request body:

{  

    "id_restaurante": int,  
    "nombre_restaurante": string,  
    "especialidad": string,  
    "chef_principal": string,  
    "color": string,  
    "logo": string  
  
}

#### method = GET | endpoint: /httptrigger2'

Json request body:

{  

    "id_restaurante": int
    
}


