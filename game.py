from wordlists.filter_wordlist import check


class IncorrectWordError(Exception):
    """
    Introducing IncorrectWordError as a specific validation Error signalizing a player-side problem.
    This will be used for Error handling later.
    """
    pass


def generate_field():
    # Fields won't be generated. Playing is suspended on one field only.

    # return "ძვე ლთბ წის ურგ".upper()
    # return "იდგ ოხს ნეა ვრლ".upper()  # ივედრა, აგონია, არხი, იოლი, ისევ
    return "BEG LOC SUP MNQ"


def listify_field(field):
    # Returns the field as a list
    return list(field.replace(' ', ''))


def check_neighbours(word_fields):
    for i in range(len(word_fields) - 1):
        if word_fields[i] == word_fields[i + 1]:
            return False
    return True


def check_for_a_field(word, field):
    """
    Raises IncorrectWordError if a word can't be used because of the different sides rule.
    """
    def get_letter_side(letter):
        """
        Returns the index of the side on which a letter is.
        Declared inside a function because we need to use the local field.
        """
        index = field.index(letter)
        return index // 3

    word_fields = list(map(get_letter_side, word))
    if not check_neighbours(word_fields):
        raise IncorrectWordError("Consecutive letters of a single word must not be on the same side of the square!")


def check_word(word, prev, field, guessed, wordlist):
    """
    Checks whether a word is an answer for the game.

    If not, it raises IncorrectWordError and explains why.

    If yes, it returns (guessed, prev) to be unpacked into variables.
    """
    if word not in wordlist:
        raise IncorrectWordError("Word not present in wordlist!")

    if not check(word, field):
        raise IncorrectWordError("The word must contain only letters from the game field!")

    if not word.startswith(prev):
        raise IncorrectWordError(f"The word must begin with the last letter of the previous word! (with {prev})")

    def get_letter_side(letter):
        """
        Returns the index of the side on which a letter is.
        Declared inside a function because we need to use the local field.
        """
        index = field.index(letter)
        return index // 3

    word_fields = list(map(get_letter_side, word))
    if not check_neighbours(word_fields):
        raise IncorrectWordError("Consecutive letters of a single word must not be on the same side of the square!")

    for i in range(12):
        if field[i] in word and guessed[i] == "*":
                guessed[i] = "•"

    return guessed, word[-1]


if __name__ == "__main__":
    print(check_for_a_field("ABUNDANCE", list("RABIDGUKENCM")))