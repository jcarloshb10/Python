def clasificar_regalo(id:int)->str:
    id_str = str(id)
    if id_str == id_str[::-1]:
        if id%2==0:
            return "boy"
        else:
            return "girl"
    elif id%2==0:
        return "man"
    else:
        return "woman"