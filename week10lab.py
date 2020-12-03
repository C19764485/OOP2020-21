# Week 10 labwork - Games
# Abstract classes and more
# Author: Panagiotis Bampilis

from abc import ABC, abstractmethod

class MathsGame(ABC):
    """
    The abstract base class that defines the scaffold of
    how to play a maths game for children.
    ...
    Attributes:
    -----------
        user_input_property : abstract property
            Getter method to control access to user input
            type to be decided by derived class(es).
    Methods:
    --------
        __init__ : abstract method
            Prints out a welcome message.
        play_game : abstract method
            Provides the game play.
            Logic to be implemented by the derived class(es).
    """

    @abstractmethod
    def __init__(self):
        """
        Currently sets a welcome message.
        Any instance variables necessary for game play should
        be declared here.
        Derived classes must implement this abstract method.
        """
        print("Welcome to the Math Game")


    @property
    @abstractmethod
    def user_input_property(self):
        """
        Abstract method.
        To be a property to control access to the user input.
        If a setter method is necessary for the specific game
        to play, please implement this in the derived class(es).
        """
        pass

    @abstractmethod  # using the decorator
    def play_game(self):
        """
        Abstract method.
        Access method to start the playing of a game.
        """
        pass

class Fibonacci(MathsGame):
    """
    Class derived from the MathsGame abstract class.
    FibonacciGame provides a game that prints a certain
    number of terms in the Fibonacci sequence. Then the
    user is asked for the next number. This game can be
    played endlessly. After finishing the game play there
    will be output in how many games the next in the
    sequence was guessed correctly.
    Attributes:
    -----------
        self.__input : int
            Holds the user input.
    Methods:
    --------
        __init__(self)
            Sets the input variable to 0
            Also calls parent class's init
        user_input_property : property
            Getter returns the value of the instance
            variable self.__input
            Setter sets the value of the instance
            variable self.__input
        play_game(self)
            Returns : none
            Handles the game playing logic. Makes a
            call to the calculate_fibonacci static
            method
        calculate_fibonacci(terms)
            Calculates the Fibonacci sequence for a given
            number of terms.
            Argument: takes the number of terms to play
            Returns: list that holds the amount of
                Fibonacci terms
            Raises:
                TypeError if terms is not of type int
                ValueError if terms is 0 or below
    """
    def __init__(self):
        super().__init__()
        self.__input = 0

    @property
    def user_input_property(self):
        """
        Getter method to return the value of the instance
        variable self.__input.
        """
        return self.__input

    @user_input_property.setter
    def user_input_property(self, value):
        """
        Setter method to set user input in self.__input
        to a specific value. Currently no validation check.
        """
        self.__input = value

    def play_game(self):
        """
        Implementation of the abstract method play_game.
        Attributes: none
        returns: none
        """
        keep_playing = True

        while keep_playing:
            try:
                self.user_input_property = int(input("Enter 1 to play, Enter 2 to exit: "))
                if self.user_input_property not in range(1, 3):
                    print("Wrong input. Allowed are 1 to play or 2 to exit.")
            except:
                print("Enter a whole number: either 1 or 2")
                continue

                # we want to play is option 1
            if self.user_input_property == 1:
                try:
                    terms = int(input("How many terms: "))

                    if terms != 0:
                        # we want it to calculate one extra because we want to
                        # check that the user understood the sequence so we
                        # need the next number even if we won't display it
                        fibs = self.calculate_fibonacci(terms + 1)

                        # displaying all but the last one
                        # remember: slicing always EXCLUDES the element at the
                        # end position
                        print(fibs[:-1])

                        right_or_wrong = int(input("Guess the next number: "))
                        if right_or_wrong == fibs[-1]:
                            print("Well done")
                        else:
                            print("sorry, this was wrong.\n The right number is: ", fibs[-1])

                    else:  # means we don't want to return anything
                        print("Nothing to play.")
                except:
                    # this currently jumps back to the decision if play or not play
                    print("Terms must be a whole number.")

            elif self.user_input_property == 2:
                print("We feel sad to see you go... ;(")
                keep_playing = False

    @staticmethod
    def calculate_fibonacci(terms):
        """
        Static method to calculate the Fibonacci sequence.
        ...
        Arguments:
        ----------
            terms : int
                A whole number to indicate how many terms in the
                Fibonacci sequence should be displayed.
                If a non-int term is entered a TypeError is thrown.
                If a number smaller equal 0 is entered a
                ValueError is thrown.
        Raises:
        -------
            TypeError if the function argument is not of type int.
            ValueError if the function argument is zero or below.
        """
        # as part of our game structure, this is already
        # caught at the level of user error.
        # But as this is a static method, it should be
        # able to act independently and catch these issues.
        if type(terms) is not int:
            raise TypeError("Fibonacci terms need to be a whole number greater than zero.")

        # first two terms
        number1, number2 = 0, 1
        count = 0

        # check if the number of terms is valid
        if terms <= 0:
           print("Please enter a positive integer")
        elif terms == 1:
           print("Fibonacci sequence up to", terms,":")
           print(number1)
        else:
           print("Fibonacci sequence:")
           while count < terms:
               print(number1)
               nth = number1 + number2
               # update values
               number1 = number2
               number2 = nth
               count += 1

# Object instantiation
f = Fibonacci()
f.play_game()