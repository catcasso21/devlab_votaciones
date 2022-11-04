from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los Candidatos")
        unCandidato = {
            "_id": "a1",
            "cedula": "123",
            "nombre": "Juan",
            "pardido":"Conservador"
        }
        return [unCandidato]

    def create(self, infoCandidato):
        print("Crear un infoCandidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self,id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "partido":"Conservador"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Eliminando Candidato con id ", id)
        return {"deleted_count": 1}