def userEntity(item) -> dict:
    return{
            "id":str(item["_id"]),
            "nombre" :item["nombre"],
            "apellido" :item["apellido"],
            "documento" :item["documento"],
            "avatar" :item["avatar"],  
            "email" :item["email"],
            "direccion" : item["direccion"],
            "password" :item["password"] 
    } 


def usersEntity(entity) ->list:
    return [userEntity(item) for item in entity] 
