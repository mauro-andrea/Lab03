import operator

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        dizionario = []
        errori = []
        rwList = []

    def printError(self):
        numero = 0
        for w in self.rwList:
            if w.getCorretta() == False:
                print(w)
                numero+=1
        print(f"Il testo contiene {numero} errori")


    def searchWord(self, words, language):
        """
        Crea una lista di oggetti richWord
        :param words: stringa del testo dell'utente "pulito"
        :param language: stringa che indica la lingua
        :return: lista di richWord
        """
        self.dizionarioCorrente(lingua=language)
        rwList = []
        for w in words.split(" "):
            r_w = rw.RichWord(w)
            if operator.contains(self.dizionario,w):
                r_w.setCorretta(True)
            else:
                r_w.setCorretta(False)
            rwList.append(r_w)

        self.rwList = rwList

    def dizionarioCorrente(self , lingua):
        """
        Setter del dizionario corrente
        :param lingua: stringa che indica la lingua scelta dall'utente
        """
        self.dizionario = d.Dictionary().loadDictionary(lingua)
