# From here, the WORDLIST variable is imported, in case one needs to play the game (mode 1).
# This works, because each time something is imported, the script is run,
# so, the WORDLIST is read from the file during that process.
# Please Note 1: This is only imported in main.py, for the sake of not reading the wordlist multiple times
# Please Note 2: The wordlist for solving the puzzle is entered by the user through CLI.

WORDLIST_PATH = "wordlists/files/eng_nouns_filtered.txt"

with open(WORDLIST_PATH) as fp:
    WORDLIST = fp.read().split("\n")
