from .attraction import Attraction

class PettingZoo(Attraction):

    def __init__(self, name, description):
        Attraction.__init__(self, name, description)