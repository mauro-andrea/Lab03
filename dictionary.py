class Dictionary:
    def __init__(self):
        pass

    def loadDictionary(self,path):
        """
        Crea e ritorna la lista delle parole di un dizionario
        :param path: stringa che indica la lingua
        :return: lista delle parole del dizionario
        """
        nome = "resources/"+path+".txt"
        lista_dizionario=[]
        f = open(nome , "r")
        r = f.readline()
        while r!="":
            r = r.strip("\n")
            lista_dizionario.append(r)
            r = f.readline()
        f.close()

        return lista_dizionario
    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict