"""
Modify each function until the tests pass
"""


def loops_one():
    """
    Return a list with ten items, each one
    a string with just one star in it
    """
    stars = []
    for i in range(10):
        stars.append("*")
    return stars


def loops_two(row_count=5, column_count=10):
    """
    Return a row_count lists with column_count items,
    each one a string with just one star in it
    """
    stars = []
    for i in range(row_count):
        starRow = []
        for j in range(column_count):
            starRow.append("*")
        stars.append(starRow)
    return stars


def loops_three():
    """
    return a list with the numbers 0-9
    """
    pass


def loops_four():
    """
    return 10 lists list with the numbers 0-9
    """
    pass


def loops_five():
    """
    return 10 lists, with 10 items. The first filled with the
    number 1, the second with the number 2 etc.
    """
    pass


def loops_six():
    """
    return a list with the numbers 0-9
    """
    pass


def list_printer(input_list, exercise_name):
    """
    you don't need to worry about this function, it's just
    to make it clearer what you are returning
    """
    print "\n" + exercise_name
    if input_list is not None:
        for thing in input_list:
            if type(thing) is list:
                for column in thing:
                    print column,
                print
            else:
                print thing,
    else:
        print "This exercise is still returning None."
        print "Either you haven't done it, or you aren't returning properly"


if __name__ == "__main__":
    list_printer(loops_one(), "loops_one")
    list_printer(loops_two(), "loops_two")
    list_printer(loops_three(), "loops_three")
    list_printer(loops_four(), "loops_four")
    list_printer(loops_five(), "loops_five")
    list_printer(loops_six(), "loops_six")
