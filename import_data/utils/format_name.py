import unicodedata
import re


def remove_special_characters(string):

    nfkd = unicodedata.normalize("NFKD", string)
    word = "".join([c for c in nfkd if not unicodedata.combining(c)])

    return re.sub("[^a-zA-Z0-9 \\\]", "", word)
