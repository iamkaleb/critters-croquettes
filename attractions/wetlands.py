from .attraction import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        Attraction.__init__(self, name, description)