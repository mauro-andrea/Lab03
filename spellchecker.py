import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        rwList = []
        pass

    def handleSentence(self, txtIn, language):
        """
        Gestisce l'input dell'utente, rimuovendo la punteggiatura dalla stringa e passa gli input all'algoritmo di correzione
        :param txtIn: stringa che indica l'input dell'utente
        :param language: stringa che indica la lingua seleziona dall'utente
        :return:
        """

        testo = txtIn.strip("\n").lower()
        testo = replaceChars(testo)

        gestione = md.MultiDictionary()
        gestione.searchWord(testo, language)
        gestione.printError()
        print(time.process_time())

    def printMenu(self):
        """
        Stampa il menù di interfaccia con l'utente
        :return:
        """
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    """
    Rimuove la punteggiatura dalla stringa in input
    :param text: stringa
    :return: stringa senza punteggiatura
    """
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars :
        text = text.replace(c, "")
    return text
