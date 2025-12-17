from game import IncorrectWordError, check_for_a_field
from wordlists.filter_wordlist import perform_filtering


def get_from_letter(wordlist, letter):
    return [word for word in wordlist if word.startswith(letter)]


def check_letters_known(field, letters_known):
    for letter in field:
        if letter not in letters_known:
            return False
    return True


def merge_letters_known(base, new):
    ans = list(base)
    for e in new:
        if e not in ans:
            ans.append(e)
    return ans


def solve(wordlist, field, min_length = 3, max_length = 10000, word_limit = 500):
    wordlist = perform_filtering(wordlist, letters=field, min_len=min_length, max_len=max_length)
    solutions = []

    # This function is introduced inside a function because it uses a list solutions,
    # which is introduced hereby.
    def recursive_solve(wordlist, field, letters_known, words_known, word_limit):
        if check_letters_known(field, letters_known):
            solutions.append(words_known)
            return
        if word_limit and len(words_known) >= word_limit:
            return
        for word in get_from_letter(wordlist, words_known[-1][-1]):
            if word not in words_known:
                try:
                    check_for_a_field(word, field)
                except IncorrectWordError:
                    pass
                else:
                    recursive_solve(
                        wordlist,
                        field,
                        merge_letters_known(letters_known, list(word)),
                        words_known + [word], word_limit=word_limit
                    )

    for w in wordlist:
        recursive_solve(wordlist, field, list(w), [w], word_limit=word_limit)

    return solutions


if __name__ == "__main__":
    # DEBUG ONLY
    from wordlists.wordlist_reader import WORDLIST
    # solutions = solve(WORDLIST, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    solutions = solve(WORDLIST, list("RAB IDG UKE NCM"), min_length=4, word_limit=5)
    print()
    print()
    for s in solutions:
        print(' '.join(s))
    print(len(solutions), "solutions found")
