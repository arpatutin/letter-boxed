from typing import Any


def check(word, letters):
    # Checks whether word consists of letters
    for c in word:
        if c not in letters:
            return False
    return True


def perform_filtering(arr, letters = None,  min_len = 3, max_len = 10000, sorting = False):
    """
    Performs wordlist filtering from given dictionary (arr: list of words)
    0. Capitalizes all the words in arr
    1. Checks the min_len and max_len
    2. If letters is given, checks if the word is only from the letters
    3. If sorting is True, sorts the array.
    """
    filtered_text = []
    for line in arr:
        if not line:  # If line is empty
            continue
        raw = line.split()[0]
        if min_len <= len(raw) <= max_len and not (letters and not check(raw, letters)):
            # not (letters and not check(raw, letters)) checks that either:
            # 1. letters isn't defined (hence, check wouldn't be called, the statement is true, and it is fine to add the word)
            # 2. letters is defined, the check is performed and the word consists of those letters
            filtered_text.append(raw.upper())
    if sorting:
        filtered_text.sort()
    return filtered_text


def filter_wordlist(filename, save = False, letters = None, sorting = False, min_len = 3, max_len = 10000):
    """
    Performs wordlist filtering from a file.
    """
    text_split = []
    with open(filename) as fp:
        text_split = fp.read().split('\n')
    filtered_text = perform_filtering(text_split, letters, min_len, max_len, sorting)
    if save:
        with open(filename.replace('.', '_filtered.'), 'w') as fp:
            # filename.replace('.', '_filtered.') turns blablabla.txt into blablabla_filtered.txt
            # restriction: no other dots in filename!
            fp.write('\n'.join(filtered_text))
    return filtered_text


if __name__ == "__main__":
    # DEBUG ONLY
    print(filter_wordlist("files/eng_nouns.txt", save=True))