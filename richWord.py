class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = None #this is a bool


    def getCorretta(self):
        # print("getter of parola called" )
        return self._corretta


    def setCorretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola