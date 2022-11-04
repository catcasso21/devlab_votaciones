from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")
    def index(self):
        print("Listar todos los resultados")
        unResultado={
            "_id":"resultado1",
            "numero_mesa":"mesa 1",
            "id_partido":"partido1"
        }
        return [unResultado]

    def create(self,infoResultado):
        print("Crear un resultado")
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self,id):
        print("Mostrando un resultado con id ",id)
        elResultado = {
            "_id":id,
            "numero_mesa":"mesa 1",
            "id_partido":"partido1"
        }
        return elResultado

    def update(self, id, infoResultado):
        print("Actualizando resultado con id ",id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self,id):
        print("Eliminando resultado con id ",id)
        return {"deleted_count":1}