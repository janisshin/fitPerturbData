import tellurium as te



class rxnModel():

    def __init__(self, antimonyStr): # constructor
        """
        Creates a model object with various properties
        """        
        self.antimonyStr = antimonyStr

        self.Km_list = [p for p in te.loada(antimonyStr).getGlobalParameterIds() if "Km" in p]

        self.parameters = [p for p in te.loada(antimonyStr).getGlobalParameterIds() if "k" in p]

        self.enzymes = [p for p in te.loada(antimonyStr).getGlobalParameterIds() if "e" in p]


