"""The module containing the basic game-loop script for the game snake"""


from provided_code.snake_game import SnakeGame


def main():
    """The main entry point for the game script"""
    #pylint: disable=no-member
    game = SnakeGame((61, 196, 63), 600, 600)
    game.game_loop()


if __name__ == "__main__":
    main()
