import operator
import time

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
        print(f"Tempo impiegato per la ricerca = {time.time()}")


    def searchWord(self, words, language):
        """
        Crea una lista di oggetti richWord, per verificare la correttezza di una parola usa il metodo contains()
        :param words: stringa del testo dell'utente "pulito"
        :param language: stringa che indica la lingua
        :return: lista di richWord
        """
        self.dizionarioCorrente(language)
        rwList = []
        for w in words.split(" "):
            r_w = rw.RichWord(w)
            if operator.contains(self.dizionario,w):
                r_w.setCorretta(True)
            else:
                r_w.setCorretta(False)
            rwList.append(r_w)

        self.rwList = rwList

    def searchWordLinear(self, words, language):
        """
        Crea una lista di oggetti richWord, per verificare la correttezza di una parola implementa la ricerca lineare
        :param words: stringa del testo dell'utente "pulito"
        :param language: stringa che indica la lingua
        :return: lista di richWord
        """
        self.dizionarioCorrente(language)
        rwList =[]
        for w in words.split(" "):
            r_w = rw.RichWord(w)
        #implemento la ricerca lineare con un metodo
            if searchLinear(w, self.dizionario):
                r_w.setCorretta(True)
            else:
                r_w.setCorretta(False)
            rwList.append(r_w)
        self.rwList=rwList

    def searchWordDichotomic(self, word, language):
        """
        Crea una lista di oggetti richWord, per verificare la correttezza di una parola implementa la ricerca dicotomica
        :param words: stringa del testo dell'utente "pulito"
        :param language: stringa che indica la lingua
        :return: lista di richWord
        """
        self.dizionarioCorrente(language)
        rwList = []

        for w in word.split(" "):
            r_w = rw.RichWord(w)
            if searchDichotomic(w,self.dizionario):
                r_w.setCorretta(True)
            else:
                r_w.setCorretta(False)
            rwList.append(r_w)
        self.rwList=rwList


    def dizionarioCorrente(self , lingua):
        """
        Setter del dizionario corrente
        :param lingua: stringa che indica la lingua scelta dall'utente
        """
        self.dizionario = d.Dictionary().loadDictionary(lingua)


def searchLinear(w,dict):
    """
    Scorre un iterabile confrontando ogni elemento con quello da verificare, si ferma se lo trova
    :param w: parola da cercare
    :param dict: iterabile che funge da dizionario
    :return: True se la parola viene trovata, False altrimenti
    """
    correct = False
    for d in dict:
        if w == d:
            correct = True
            break
    return correct

def searchDichotomic(w,dict):
    """
    Implementa la ricerca dicotomica di una parola in un iterabile che funge da dizionario di parole
    :param w: parola da cercare
    :param dict: iterabile
    :return: True se la parola viene trovata, False altrimenti
    """

    correct= False
    sup = len(dict)-1
    inf = 0
    pos = (sup+inf)//2

    while ((not correct) and (inf < sup)):

        if dict[pos] == w:
            correct = True

        elif dict[pos] < w:
            inf = pos+1
            pos = (sup+inf)//2

        elif dict[pos] > w:
            sup = pos-1
            pos = (sup+inf)//2

    return correct