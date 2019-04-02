def check_brackets(your_brackets):
    """
    >>> check_brackets('()')
    True

    >>> check_brackets('{{')
    False

    >>> check_brackets('{{(())')
    False

    >>> check_brackets('{{]')
    False

    >>> check_brackets('{{}}[]')
    True

    >>> check_brackets('((([(])))')
    False
    """
    copy_brackets = your_brackets[:]
    search_for = ['()', '[]', '{}']

    for x in range(len(copy_brackets)):
        for pair in search_for:
            if pair in copy_brackets:
                index = copy_brackets.index(pair)

                copy_brackets_list = list(copy_brackets)
                del copy_brackets_list[index]
                del copy_brackets_list[index]

                copy_brackets = "".join(copy_brackets_list)

    return not copy_brackets



