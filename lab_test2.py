# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# Panagiotis Bampilis - C19764485
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    @property
    def insert_values(self):
        """
         Created getter to return self.characters
         to the user.
        """
        return self.characters

    @insert_values.setter
    def insert_values(self, value):
        """
        Created setter to set the user characters
        into value which is returned in its decorator.
        """
        # variable that returns self.characters
        self.characters = value

    # Changed the class method from delete to remove
    def remove(self):
        """
        Method remove a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        # For loop that removes safely this time
        # Unlike delete function
        try:
            for letter in self.characters:
                self.characters.remove(letter)
        except:
            raise ValueError

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        # Error catching by using try except
        # to prevent the user from entering above 12
        try:
            if steps > 12 or steps < 1:
                raise ValueError("You need to enter a number below 12")
            else:
                self.cursor -= steps
        except:
            print("You can't enter above 12")

# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

# Exception handling to prevent the program from crashing
try:
    doc.backward(4)
    doc.remove()
    doc.insert('n')
    doc.save()
except:
    print("Unexpected error")