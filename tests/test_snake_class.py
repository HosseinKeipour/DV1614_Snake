"""
This file contains the classes handling the tests as described in the file 'run_tests'.

Each test method has the same description regarding the test as presented in 'run_tests'
"""

import unittest
from collections.abc import Iterable

from student_code.snake_class import Snake


class SnakeClassTestingStepOne(unittest.TestCase):
    """Handles the first part of the tests"""

    def test_snake_inside_bounds(self):
        """
        This test will create a Snake instance at given coordinates.
        Three bounds will then be created.
            One of the bounds will the Snake be completely inside of
            One will it be partially inside of
            And the last one will it be outside of
            (The first tuple is the top left coordinates of the bound)
            (The second tuple is the bottom right coordinates of the bound)
        """

        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [True, False, False]         
        results = []
        test_vectors = [
            [
                (0, 0),
                (150, 150)
            ],
            [
                (30, 30),
                (35, 35)
            ],
            [
                (70, 70),
                (100, 100)
            ]
        ]

        for test_vector in test_vectors:
            results.append(snake.inside_bounds(test_vector[0], test_vector[1]))

        self.assertListEqual(results, expected_results)

    def test_snake_check_collision(self):
        """
        This test will create a Snake instance at given coordinates.
        Two collision checks will then be conducted.
            One of the collision checks will be true.
            The other will be false.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [True, False]
        results = []
        test_vectors = [
            [
                (30, 30),
                (5, 5)
            ],
            [
                (70, 70),
                (10, 10)
            ]
        ]

        for test_vector in test_vectors:
            results.append(snake.check_collision(
                test_vector[0], test_vector[1]))

        self.assertListEqual(results, expected_results)

    def test_snake_check_collision_with_fruit(self):
        """
        This test will create a Snake instance at given coordinates.
        Two collision checks with fruit will then be conducted.
            One of the collision checks will be true.
            The other will be false.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [True, False]
        results = []
        test_vectors = [
            [
                (30, 30),
                (5, 5)
            ],
            [
                (70, 70),
                (10, 10)
            ]
        ]

        for test_vector in test_vectors:
            results.append(
                snake.check_collision_with_fruit(
                    test_vector[0], test_vector[1]
                )
            )

        self.assertListEqual(results, expected_results)

    def test_snake_check_collision_with_self(self):
        """
        This test will create a Snake instance at given coordinates.
        A collision with self check will then be conducted.
        This check is expected to be false.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        self.assertEqual(snake.check_collision_with_self(), False)

    def test_snake_grow(self):
        """
        This test will create a Snake instance at given coordinates.
        Grow will then be called to make sure that no chrash occour.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        self.assertIsNone(
            snake.grow(),
            "Snake.grow() should neither return an object nor raise an error."
        )

    def test_snake_iterable(self):
        """
        This test will create a Snake instance at given coordinates.
        An attempt will then be made to iterate over the instance.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        self.assertIsInstance(snake, Iterable)


class SnakeClassTestingStepTwo(unittest.TestCase):
    """Handles the second part of the tests"""

    def test_snake_internal_get_coordinates(self):
        """
        A Snake instance will be created at given coordinates.
        The instance will then be iterated over, and get_coordinates called,
        on the internal structure to make sure that the coordinates match the
        provided ones.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [(30, 30)]
        results = []

        for part in snake:
            results.append(part.get_coordinates())

        self.assertListEqual(results, expected_results)

    def test_snake_internal_get_colour(self):
        """
        A Snake instance will be created at given coordinates.
        The instance will then be iterated over, and get_colour called,
        on the internal structure to make sure that the colour match the
        provided one.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [(0, 0, 0)]
        results = []

        for part in snake:
            results.append(part.get_colour())

        self.assertListEqual(results, expected_results)

    def test_snake_internal_get_size(self):
        """
        A Snake instance will be created at given coordinates.
        The instance will then be iterated over, and get_size called,
        on the internal structure to make sure that the size match the
        provided one.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [(30, 30)]
        results = []

        for part in snake:
            results.append(part.get_size())

        self.assertListEqual(results, expected_results)


class SnakeClassTestingStepThree(unittest.TestCase):
    """Handles the final part of the tests"""

    def test_snake_moving(self):
        """
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern.
        Each movement will carry with it a control to make sure that
        the head moves as expected.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [
            [(30, 0)],
            [(60, 0)],
            [(60, 30)],
            [(60, 60)],
            [(30, 60)],
            [(0, 60)],
            [(0, 90)],
            [(30, 90)]
        ]
        test_vector = [
            Snake.move_up,
            Snake.move_right,
            Snake.move_down,
            Snake.move_down,
            Snake.move_left,
            Snake.move_left,
            Snake.move_down,
            Snake.move_right
        ]

        for expected, test_move in zip(expected_results, test_vector):
            with self.subTest("Snake.{}".format(test_move.__name__)):
                test_move(snake)
                result = []
                for parts in snake:
                    result.append(parts.get_coordinates())

                self.assertListEqual(result, expected)

    def test_snake_growing_while_moving(self):
        """
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern, growing after each movement.
        Each movement will carry with it a control to make sure that
        the entire body moves as expected.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [
            [(30, 0), (30, 30)],
            [(60, 0), (30, 0), (30, 30)],
            [(60, 30), (60, 0), (30, 0), (30, 30)],
            [(60, 60), (60, 30), (60, 0), (30, 0), (30, 30)],
            [(30, 60), (60, 60), (60, 30), (60, 0), (30, 0), (30, 30)],
            [(0, 60), (30, 60), (60, 60), (60, 30), (60, 0), (30, 0), (30, 30)],
            [(0, 90), (0, 60), (30, 60), (60, 60),
             (60, 30), (60, 0), (30, 0), (30, 30)],
            [(30, 90), (0, 90), (0, 60), (30, 60), (60, 60),
             (60, 30), (60, 0), (30, 0), (30, 30)]
        ]
        test_vector = [
            Snake.move_up,
            Snake.move_right,
            Snake.move_down,
            Snake.move_down,
            Snake.move_left,
            Snake.move_left,
            Snake.move_down,
            Snake.move_right
        ]

        for expected, test_move in zip(expected_results, test_vector):
            with self.subTest("Snake.{}".format(test_move.__name__)):
                snake.grow()
                test_move(snake)
                result = []
                for parts in snake:
                    result.append(parts.get_coordinates())

                self.assertListEqual(result, expected)

    def test_snake_collision_while_growing_and_moving(self):
        """
        A Snake instance will be created at given coordinates.
        It will then be moved in a pattern. After each movement,
        a inside_bounds test will be conducted.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results_inside_bounds = [
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            False,
            True
        ]

        expected_results_collision_with_self = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True
        ]

        test_vector = [
            Snake.move_up,
            Snake.move_right,
            Snake.move_down,
            Snake.move_down,
            Snake.move_left,
            Snake.move_left,
            Snake.move_down,
            Snake.move_right,
            Snake.move_up
        ]

        for expected_bounds, expected_collision, test_move in zip(expected_results_inside_bounds, expected_results_collision_with_self, test_vector):
            with self.subTest("Snake.{}".format(test_move.__name__)):
                snake.grow()
                test_move(snake)

                self.assertEqual(snake.inside_bounds((0, 0), (90, 90)), expected_bounds)
                self.assertEqual(snake.check_collision_with_self(), expected_collision)

    def test_snake_inside_bounds_while_moving(self):
        """
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern, growing after each movement.
        After each movement is done, a collision_with_self check will be conducted.
        """
        snake = Snake((30, 30), (30, 30), (0, 0, 0))

        expected_results = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True
        ]
        test_vector = [
            Snake.move_up,
            Snake.move_right,
            Snake.move_down,
            Snake.move_down,
            Snake.move_left,
            Snake.move_left,
            Snake.move_down,
            Snake.move_right,
            Snake.move_up
        ]

        for expected, test_move in zip(expected_results, test_vector):
            with self.subTest("Snake.{}".format(test_move.__name__)):

                snake.grow()
                test_move(snake)

                self.assertEqual(snake.check_collision_with_self(), expected)

    def test_snake_check_collision_with_fruit_while_moving(self):
        """
        A Snake instance will be created at given coordinates.
        It will then be moved in a pattern around a fruit,
        not being able to take it before the last move. 
        After each movement, a test will be conducted.
        """

        fruit_coordinates = (60, 60)
        fruit_size = (30, 30)
        snake = Snake((30, 30), (30, 30), (0, 0, 0))


        expected_results = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True
        ]

        test_vector = [
            Snake.move_down,
            Snake.move_down,
            Snake.move_right,
            Snake.move_right,
            Snake.move_up,
            Snake.move_up,
            Snake.move_left,
            Snake.move_down
        ]
        for expected, test_move in zip(expected_results, test_vector):
            with self.subTest("Snake.{}".format(test_move.__name__)):
                test_move(snake)

                self.assertEqual(snake.check_collision_with_fruit(fruit_coordinates, fruit_size), expected)