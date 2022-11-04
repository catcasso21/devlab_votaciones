from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos las mesas")
        unaMesa={
            "_id":"a1",
            "cantidad_inscritos":"123"
        }
        return [unaMesa]

    def create(self,infoMesa):
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self,id):
        print("Mostrando una mesa con id ",id)
        laMesa = {
            "_id": id,
            "cantidad_inscritos":"123"
        }
        return laMesa

    def update(self, id, infoMesa):
        print("Actualizando mesas con id ",id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self,id):
        print("Eliminando mesa con id ",id)
        return {"deleted_count":1}