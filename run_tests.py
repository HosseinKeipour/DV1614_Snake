"""
This file contains the tests given for assignment 2.
Each of these tests must pass for your assignment to be assessed.

The following unit tests are conducted on the class Snake:
    1. test_snake_inside_bounds
            This test will create a Snake instance at given coordinates.
            Three bounds will then be created.
                One of the bounds will the Snake be completely inside of
                One will it be partially inside of
                And the last one will it be outside of

    2. test_snake_check_collision
            This test will create a Snake instance at given coordinates.
            Two collision checks will then be conducted.
                One of the collision checks will be true.
                The other will be false.

    3. test_snake_check_collision_with_fruit
            This test will create a Snake instance at given coordinates.
            Two collision checks with fruit will then be conducted.
                One of the collision checks will be true.
                The other will be false.

    4. test_snake_check_collision_with_self
            This test will create a Snake instance at given coordinates.
            A collision with self check will then be conducted.
                This check is expected to be false.

    5. test_snake_grow
            This test will create a Snake instance at given coordinates.
            Grow will then be called to make sure that no chrash occour.

    6. test_snake_iterable
            This test will create a Snake instance at given coordinates.
            An attempt will then be made to iterate over the instance.

If these pass, the following unit tests are conducted on the internal class:
    7. test_snake_internal_get_coordinates
            A Snake instance will be created at given coordinates.
            The instance will then be iterated over, and get_coordinates called,
            on the internal structure to make sure that the coordinates match the
            provided ones.

    8. test_snake_internal_get_colour
            A Snake instance will be created at given coordinates.
            The instance will then be iterated over, and get_colour called,
            on the internal structure to make sure that the colour match the
            provided one.

    9. test_snake_internal_get_size
            A Snake instance will be created at given coordinates.
            The instance will then be iterated over, and get_size called,
            on the internal structure to make sure that the size match the
            provided one.

If these pass, the following unit tests are conducted on the snake class:
    10. test_snake_move_left
        A Snake instance will be created at given coordinates.
        The instance will then be moved to the left. The new
        coordinates will be controlled using the internal
        get_coordinates.

    11. test_snake_move_right
        A Snake instance will be created at given coordinates.
        The instance will then be moved to the right. The new
        coordinates will be controlled using the internal
        get_coordinates.

    12. test_snake_move_up
        A Snake instance will be created at given coordinates.
        The instance will then be moved up. The new
        coordinates will be controlled using the internal
        get_coordinates.

    13. test_snake_move_down
        A Snake instance will be created at given coordinates.
        The instance will then be moved down. The new
        coordinates will be controlled using the internal
        get_coordinates.

If all unit tests pass, integration tests will be conducted:

    14. test_snake_moving
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern.
        Each movement will carry with it a control to make sure that
        the head moves as expected.

    15. test_snake_growing_while_moving
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern, growing after each movement.
        Each movement will carry with it a control to make sure that
        the entire body moves as expected.

    16. test_snake_collision_while_growing_and_moving
        A snake instance will be created at given coordinates.
        It will then be moved in a pattern, growing after each movement.
        After each movement is done, a collision_with_self check will be conducted.

    17. test_snake_inside_bounds_while_moving
        A Snake instance will be created at given coordinates.
        It will then be moved in a pattern. After each movement,
        a inside_bounds test will be conducted.
"""

import unittest
import sys

import tests.test_snake_class


def is_finished_with_step(test_case_class_to_use):
    """Helper function to initialize, load, and run tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(
        loader.loadTestsFromTestCase(
            test_case_class_to_use
        )
    )

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.skipped:
        return False

    return result.wasSuccessful()


def is_finished_with_step_one():
    """Run the first batch of tests"""
    print('-'*70 + "\nStarting test suite 1:\n")
    return is_finished_with_step(tests.test_snake_class.SnakeClassTestingStepOne)


def is_finished_with_step_two():
    """Run the second batch of tests"""
    print('-'*70 + "\nStarting test suite 2:\n")
    return is_finished_with_step(tests.test_snake_class.SnakeClassTestingStepTwo)


def is_finished_with_step_three():
    """Run the third batch of tests"""
    print('-'*70 + "\nStarting test suite 3:\n")
    return is_finished_with_step(tests.test_snake_class.SnakeClassTestingStepThree)


if __name__ == "__main__":
    if is_finished_with_step_one() is not True:
        print("\n\tThe first testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    elif is_finished_with_step_two() is not True:
        print("\n\tThe second testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    elif is_finished_with_step_three() is not True:
        print("\n\tThe third and final testing step did not pass," +
              "either because of a failed or a skipped test.")
        sys.exit(1)

    sys.exit(0)
