import random

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def short_unique(unchoosable=[]):
    selection = "".join(random.sample(ALPHABET, 6))
    while selection in unchoosable:
        selection = "".join(random.sample(ALPHABET, 6))
    return selection
