from src.Domain.entity.ANodeLinkedList import ANodeLinkedList 
from Infrastructure.interface.IDataStructure import IDataStructure

class LinkedList(IDataStructure):
    def __init__(self, first_node:ANodeLinkedList):
        self.first_node = first_node

    # Ajout d'un maillon en fin de liste
    def add_node(self, first_node:ANodeLinkedList):
        

        # print("Adding node to linked list: "+ self.get_last().get_value())
        # print("New node to add: "+ first_node.get_value())
        self.get_last().set_next(first_node)

    def remove_node(self, value: str) -> bool:
        # Cas où la liste est vide
        if self.first_node is None:
            return False

        # Cas où le premier élément est celui à supprimer
        if self.first_node.get_value() == value:
            self.first_node = self.first_node.get_next()
            return True

        # Parcourir la liste pour trouver le nœud à supprimer
        prev = self.first_node
        current = self.first_node.get_next()

        while current is not None:
            if current.get_value() == value:
                # On saute le node à supprimer
                prev.set_next(current.get_next())
                return True

            prev = current
            current = current.get_next()

        # Si aucun node trouvé
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