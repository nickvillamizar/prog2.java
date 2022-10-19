from model.kid import Kid
from model.list_se import ListSE

class ListSEService:
    def __init__(self):
        self.list= ListSE()
        #mosquera = Kid("123456","Jeronimo Mosquera",4,"M")
        mosquera = Kid({"identification":"123456","name":"Jeronimo Mosquera","age":4,"gender":"M"})
        self.list.add(mosquera)
        murillo = Kid({"identification":"654321","name":"Jeronimo Murillo","age":5,"gender":"M"})
        self.list.add(murillo)

    def add_kid(self,data):
        #Aca irian las validaciones del dict
        if "age" in data:
            if data['age'] > 0:
                self.list.add(Kid(data))
                return "Kid adicionado exitosamente"
            else:
                return "La edad debe ser positiva"
        else:
            return "Atributo age no encontrado"
    def add_to_start(self,data):
        #Aca irian las validaciones del dict
        if "age" in data:
            if data['age'] > 0:
                self.list.head.add(Kid(data))
                return "Kid adicionado exitosamente"
            else:
                return "La edad debe ser positiva"
        else:
            return "Atributo age no encontrado"

    def add_by_position(self, kidByPositionDTO: KidByPositionDTO):
        if kidByPositionDTO.position > 0 and kidByPositionDTO.position <= (self.list.size + 1):
            self.list.add_by_position(kidByPositionDTO.position, kidByPositionDTO.kid)
            return "Adicionado exitosamente"
        else:
            return "Posición no permitida"

    def mix_by_gender(self):
        self.list.mix_by_gender()
        return "Se ha ejecutado la mezcla"

