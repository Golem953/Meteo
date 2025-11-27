from src.Domain.entity.ANodeLinkedList import ANodeLinkedList 
from src.Domain.ports.IDataStructure import IDataStructure

class LinkedList(IDataStructure):
    def __init__(self, first_node:ANodeLinkedList):
        self.first_node = first_node

    # Ajout d'un maillon en fin de liste
    def add_node(self, first_node:ANodeLinkedList):
        

        # print("Adding node to linked list: "+ self.get_last().get_value())
        # print("New node to add: "+ first_node.get_value())
        self.get_last().set_next(first_node)

    


    def search(self, value):
        actual_node = self.first_node

        while actual_node != None:

            if actual_node.get_value() == value:
                return True

            actual_node = actual_node.get_next()

        return False
    
    # Renvoie le dernier élément de la liste (Celui avec get_next() = None)
    def get_last(self):
        actual_node = self.first_node

        # print("Getting last node..."+ actual_node.get_value())
        while actual_node.get_next() != None:
            actual_node = actual_node.get_next()

        # print("Last node found: " + actual_node.get_value())
        return actual_node

    def afficher_liste(self):
        maillon_actuel = self.first_node

        while maillon_actuel.next_node != None:
            # print(maillon_actuel.get_value())
            maillon_actuel = maillon_actuel.get_next()

        print(maillon_actuel.get_value() + "-> Next"+ str(maillon_actuel.get_next())+ "||")

    def __str__(self):
        actual_node = self.first_node

        return_string = ""

        while actual_node.get_next() != None:   
        
            return_string += str(actual_node.get_value()) + " -> "
            actual_node = actual_node.get_next()

       

        return return_string