from .attraction import Attraction

class SnakePit(Attraction):

    def __init__(self, name, description):
        Attraction.__init__(self, name, description)