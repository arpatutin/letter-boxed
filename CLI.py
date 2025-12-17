from time import sleep

from config import MAX_WORDS


def print_rules():
    print("The main goal of LETTER-BOXED is to create a sequence of words\n"
          "that uses all of the letters displayed on the game field.")
    print("The rules of the game are following:")
    print("1. All words you use should contain only letters from the game field")
    print("2. Each word, starting from the second, must begin with the last letter of the previous one")
    print("3. All words must contain at least 3 letters")
    print("4. Consecutive letters of a single word must not be on the same side of the square")


def choose_mode(invalid_input=False):
    if invalid_input:
        print("Invalid input! Let's try again.")
    else:
        print("WELCOME TO LETTER-BOXED!")
        print()
        print_rules()
        print()
        print("Because we are a progressive game, you are able to choose between two different game modes.")
    print()
    print("Mode 1: Play letter-boxed yourself")
    print("Mode 2: Let the \"AI\" solve the puzzle for you")
    print()
    mode = input("Please, make a choice now (1/2): ")
    print()
    print()
    return mode


def print_field(field, guessed):
    print("     " + " ".join(field[:3]))
    print("     " + " ".join(guessed[:3]))
    print(" " + field[9] + " " + guessed[9] + "       " + guessed[3] + " " + field[3])
    print(" " + field[10] + " " + guessed[10] + "       " + guessed[4] + " " + field[4])
    print(" " + field[11] + " " + guessed[11] + "       " + guessed[5] + " " + field[5])
    print("     " + " ".join(guessed[6:9]))
    print("     " + " ".join(field[6:9]))
    print()


def print_current_state(prev, words):
    if prev:
        print("Previous letter:", prev)
    print("Words used:", (" ".join(words) + " " if len(words) > 0 else "") + f"(in total of {len(words)})")
    # (" ".join(words) + " " if len(words) > 0 else "") prepares a string like "word word " or "" if there are no
    # + f"(in total of {len(words)})" means that in final it's either "word word (in total of 2)" or "(in total of 0)"
    print("Words allowed:", MAX_WORDS)
    print()


def print_mode_1_guide():
    print("Great choice! Now just enter your words one by one.")
    print("Each time you will see the current words used and the allowed number of words.")
    print("After that, there will be the field for you to enter your next guess.")


def print_mode_2_guide():
    print("Good! Our progressive AI can to the job for you right away.")
    print("It will only need you to input the field that is being solved and give a list of words to it.")


def get_wordlist():
    content = None
    wordlist_read = False
    while not wordlist_read:
        filename = input("Please, enter the path to the wordlist now: ")
        print()
        try:
            with open(filename) as fp:
                content = fp.read()
            wordlist_read = True
        except FileNotFoundError:
            # If the file does not exist, instead of doing the block above, we appear in this block.
            print("The file was not found!")
            print("Please, try again.")
        except Exception as e:
            # File exists, but another error occured.
            print(f"There was an error:")
            print(e)
            print("Please, try again.")
        else:
            # If we succeed with the try block, we are here.
            print("Great, thanks! The wordlist is now read.")
        print()
        print()
    return content.split('\n')


def get_field():
    field = ""
    wordlist_read = False
    print("Please, enter the field now.")
    print()
    print("For entering the field, it is not important which order of the sides you use.")
    print("It is also not important in which order the letters go (inside of a side).")
    print("However, it IS IMPORTANT that the letters from different sides appear in different 3-letter-combinations.")
    print("That means, if a side has the letters A, B and C, it doesn't matter in which order they are put,")
    print("however, they have to be put together, like ABC, BCA, ACB and so on.")
    print()
    print("The ONLY accepted format is XXX XXX XXX XXX, for example, you can input:")
    print()
    print("ABC DEF GHI JKL")
    print()
    print("The case of the input doesn't matter -- you can use both upper and lower case letters.")
    print("Please, input the field in the following format now.")
    while not wordlist_read:
        field = input("XXX XXX XXX XXX: ").upper()
        if len(field) == 15 and field.replace(' ', '').isalpha() and len(field.split(' ')) == 4:
            print("Perfect, thank you!")
            wordlist_read = True
        else:
            print("Sorry, but your input is incorrect.")
            print("Please, try again!")
        print()
        print()
    return field


def get_user_input(invalid_message=None):
    if invalid_message:
        print(f"Error! {invalid_message}")
        print()
    word = input("Now please enter a word: ").upper()
    print()
    return word


def print_solutions(solutions):
    print("So, here are the solutions:")
    sleep(1)  # Just waiting; for the sake of convenience
    for s in solutions:
        print(" ".join(s))
    print()
    print("Total solutions found:", len(solutions))
    print("Thank you!")


def game_finished(positive_ending):
    print()
    if positive_ending:
        print("Congratulations! You finished tha game :)")
        print("Hope you liked it.")
        print("Bye!")
    else:
        print("Oopsie! You ran out of words to use.")
        print("Please restart the game to try again! :D")
    print()


if __name__ == "__main__":
    # DEBUG ONLY
    print_field(list('RAB IDG UKE NCM'.replace(' ', '')), list('*** *** *•* ***'.replace(' ', '')))
