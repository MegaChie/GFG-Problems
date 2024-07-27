#!/usr/bin/python3


def removeDups(string):
    """
    Remove the duplicates from the passed string,
    keeping only the first ocurrunce and then returns it.

    Args:
    - string: the string to process.

    Returns:
    - A string with no duplicates.
    """
    if string:
        checked = set()
        string_order = []
        
        for letter in string:
            if letter not in checked:
                string_order.append(letter)
                checked.add(letter)

        return "".join(string_order)

    return ""


if __name__ == "__main__":
    print(removeDups("zvvo"))
    print(removeDups("gfg"))
    print(removeDups("clear"))
    print(removeDups(""))
