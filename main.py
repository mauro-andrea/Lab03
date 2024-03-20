import spellchecker

sc = spellchecker.SpellChecker()
stop = False

while(not stop):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    controllo = [1,2,3,4]
    if not controllo.__contains__(int(txtIn)):
        raise IOError("Selezione non valida")

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        stop = True


