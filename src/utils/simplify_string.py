def simplify_string(string):
    """
    Simplifies the content of a string by removing special characters, removing spaces and making it all lower case.

    Args:
        string: The string to be simplified.

    Returns:
        A new simplified string.
    """
    string = string.lower()
    string = string.replace(" ", "")
    string = string.translate(str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
    return string