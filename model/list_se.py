from model.kid import Kid
from model.node import Node


class ListSE:
    def __init__(self):
        # crear constructor para la lista
        self.head = None
        # verificar si la lista esta vacia
        self.size = 0
        # talla de la lista

    def add(self, kid: Kid): # llamar clase kid de tipo kid
        if self.head == None:
            self.head = Node(kid)
        else:
            temp = self.head # crear temporal
            while temp.next != None: # temporal toma su siguiente y añadir a la lista
                temp = temp.next
            # Estoy parado en el último dato
            temp.next = Node(kid)
        self.size+=1

    def add_to_start(self, kid:Kid):
        if self.head == None: # verificar si las lista esta vacia
            self.head = Node(kid) # el dato se meta en el costal
        else:
            newNode = Node(kid) # que el niño se meta en un nuevo costal
            newNode.next = self.head # añadadir al inico
            self.head = newNode
        self.size += 1 # talla de la lista

    def invert(self):
        if self.head != None:
            temp = self.head # crear temporal
            listCp = ListSE()
            while temp != None:
                listCp.add(temp.data) # crear lista copia
                temp = temp.next # tempral tome el ultmo dato y lo lleve a la lista copia
            self.head = listCp.head

    def add_by_position(self, position: int, kid: Kid):
        if position == 1: #verificar la posicion
            self.add_to_start(kid) #si la posicion es 1 añadir al inicio
        else:
            postemp = 1
            temp = self.head
            while postemp < (position - 1):
                temp = temp.next
                postemp = postemp + 1

            newNode = Node(kid)
            newNode.next = temp.next
            temp.next = newNode
            self.size += 1

    def mix_by_gender(self):
        if self.size > 1:
            contM = 1
            contF = 2
            temp = self.head
            listCp = ListSE()
            while temp != None:
                if temp.data.gender == 'M':
                    if contM > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contM, temp.data)
                    contM += 2
                else:
                    if contF > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contF, temp.data)
                    contF += 2
                temp = temp.next
            self.head = listCp.head






