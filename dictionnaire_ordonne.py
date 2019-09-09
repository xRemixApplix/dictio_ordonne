#-*- coding: utf8 -*-

class DictionnaireOrdonne:
    """
        Classe de gestion d'un dictionnaire ordonné.

        Deux listes :
            - une contenant les clés : key_list.
            - une contenant les valeurs : value_list.
    """

    def __init__(self):
        """
            Constructeur :
                - vide : si dictionnaire créé sans aucun parametre.
                - copié : depuis un dictionnaire passé en parzametre.
                - pré-rempli : par l'intermediaire de clé et valeur passés en paramètres.
        """
        self.key_list=[]
        self.value_list=[]

    def __repr__(self):
        """
            Représentation de l'objet.
            Chaine de caractère retournée lors de la demande d'affichage du dictionnaire.
        """
        chaine="{"
        premier_passage=True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine+=", "
            else:
                premier_passage=False
            chaine=repr(cle)+": "+repr(valeur)
        chaine+="}"
        return chaine

    def items(self):
        """
            Renvoie un generateur de contenant les couples (cle: valeur)
        """
        for i, cle in enumerate(self.key_list):
            valeur=self.value_list[i]
            yield (cle, valeur)



###### AUTO-TEST ######
if __name__ == "__main__":
    fruits=DictionnaireOrdonne()

    print(fruits)
#######################