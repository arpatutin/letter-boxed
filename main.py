from CLI import *
from solve import solve
from wordlists.wordlist_reader import WORDLIST
from config import *
from game import generate_field, listify_field, check_word, IncorrectWordError

game_mode = choose_mode()

while game_mode not in ["1", "2"]:
    game_mode = choose_mode(invalid_input=True)

if game_mode == "1":
    print_mode_1_guide()
    field = listify_field(generate_field())
    guessed = ['*', '*', '*'] * 4
    prev = ''
    finished = False
    input_error_message = None
    words_used = []
    while not finished and len(words_used) <= MAX_WORDS:
        # 1. Print field and read user input
        print_field(field, guessed)
        print_current_state(prev, words_used)
        word = get_user_input()

        # 2. Try to perform the turn
        try:
            # Calling check_word() "safely"
            guessed, prev = check_word(word, prev, field, guessed, WORDLIST)
        except IncorrectWordError as error:
            # If we're not there, we put the message into the variable
            input_error_message = error
        else:
            # If we're there, we put the word into the list
            words_used.append(word)

        # Then we'd be getting input more and more until we're good
        while input_error_message:
            word = get_user_input(invalid_message=input_error_message)
            try:
                # Calling check_word() "safely"
                guessed, prev = check_word(word, prev, field, guessed, WORDLIST)
            except IncorrectWordError as error:
                # If we're not there, we put the message into the variable
                input_error_message = error
            else:
                # If we succeed, we put None into the variable so that we can exit the loop
                input_error_message = None
                # and put the word into the list
                words_used.append(word)

        # 3. We check if there are any unknown letters.
        # If no, we finish the game. (finished = False makes us exit the loop)
        finished = True
        for side in guessed:
            for character in side:
                if character == '*':
                    finished = False
                    break
            if not finished:
                break

    print_field(field, guessed)
    game_finished(positive_ending=len(words_used) <= MAX_WORDS)

else:
    print_mode_2_guide()
    with open(DICT_PATH) as fp:
        wordlist = fp.read()
    field = listify_field(get_field())

    solutions = solve(wordlist, field, min_length=MIN_WORD_LENGTH, max_length=MAX_WORD_LENGTH, word_limit=MAX_CHAIN_LENGTH)

    print_solutions(solutions)

