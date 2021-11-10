class GotCharacter:
    """
        Game of Thrones is an American fantasy drama television series created
        by David Benioff and D. B. Weiss for HBO. It is an adaptation of A
        Song of Ice and Fire, a series of fantasy novels by George R. R.
        Martin, the first of which is A Game of Thrones.
    """
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. \
Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
