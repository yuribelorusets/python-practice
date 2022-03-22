def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # select the substring of characters in phrase that match toswap
    # swapcase on substring

    word = []

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            word.append(letter.swapcase())
        else:
            word.append(letter)
    return ''.join(word)

