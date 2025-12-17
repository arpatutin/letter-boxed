# Letter-boxed game

Ciao! This game contains the following development structure:

1. Wordlist filtering & adjustment
2. Game functions, main loop, CLI implementation
3. Solving system implementation

## Introductory

1. We use [exceptions](https://www.w3schools.com/python/python_try_except.asp) in the code

   (However, we comment the places where we use exceptions in the code, so it should be clear)
2. In playing mode, the wordlist is kept in ```wordlists/files/path_to_wordlist.txt```
   
   However, if you need to use your own wordlist (for PLAYING ONLY), it is possible to do so by modifying 
   the WORDLIST_PATH variable in ```wordlists/wordlist_reader.py```
3. In solving mode, the path for the wordlist is entered through the CLI
4. The other settings for solving mode, such as:
   - minimal used words' length
   - maximal used words' length
   - maximal solution length (e.g. how many words can be at most in the solution)

   are specified in the config (```config.py```)
5. All the instructions are printed; read carefully!

## How to start

The only requirement for running is to have python3 installed.

To run the program, you need to type into the shell:
```bash
python3 main.py
```

## Good luck!