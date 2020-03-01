"""
This module contains a basic wrapper for a window class.
"""

import pygame


class Window:
    """
    The Window class is a wrapper around a pygame window.
    It provides very basic rendering functionallity.

    Attributes:
    -----------------
        background_colour : list(int, int, int)
            The background colour provided to the constructor.
            Used when the method clear is called to determine the clearing colour.

        screen : pygame.Surface
            The underlying pygame screen that Window is a wrapper for.

        screen_size : tuple(int, int)
            The size of the screen as provided to the constructor.
            Mostly here for ease of access, could be fetched from the screen.

    Methods:
    -----------------
        draw_rect(background_colour : list(int, int, int), width : int, height : int):
            Draw a rectangle on the screen with the given data

        clear():
            Clear the screen with the background colour provided in the constructor

        height():
            Returns the height of the window

        width():
            Returns the width of the window
    """
    #pylint: disable=no-member

    def __init__(self, background_colour, width, height):
        """Initialize the window class.

        Parameters:
        ------------------------------------------
        background_colour : list(int, int, int)
            A triple of values between 0 and 255 indicating the r, g, b value to clear

        width : int
            The width of the window

        height : int
            The height of the window
        """
        pygame.init()
        self.background_colour = background_colour
        self.screen_size = (width, height)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('DV1614 Assignment 2: Snake')
        self.screen.fill(background_colour)

    def draw_rect(self, colour, top_left, size):
        """Draw a rectangle on the screen.

        Parameters:
        ------------------------------------------
        colour : list(int, int, int)
            A triple of values between 0 and 255 indicating the r, g, b value of the rectangle

        top_left : tuple(int, int)
            The x- and y-coordinates for the top left corner of the rectangle

        size : tuple(int, int)
            The width and height of the rectangle
        """
        pygame.draw.rect(self.screen, colour, (top_left, size))

    def clear(self):
        """Clear the screen to the background colour given in the init-function"""
        self.screen.fill(self.background_colour)

    def width(self):
        """Return the width of the screen"""
        return self.screen_size[0]

    def height(self):
        """Returns the height of the screen"""
        return self.screen_size[1]
