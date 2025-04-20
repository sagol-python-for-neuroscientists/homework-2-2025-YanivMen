
# Mapping of letters, digits, and a few punctuation marks to Morse code
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', ':': '---...',
    "'": '.----.', '-': '-....-',
}


def english_to_morse(Str):
    """Convert the contents of a text file to Morse code and save the result.

    Parameters
    ----------
    str : str
        Path to the input text file (e.g., 'lorem.txt').

    Returns
    -------
    str
        The name of the output file that now holds the Morse‐encoded text.
    """

    # --- Read, normalise, and prepare the text ---------------------------------
    lorem = open(Str)                 # open the source file for reading
    lorem_str = lorem.read()          # pull the entire file into one string
    lorem_str = lorem_str.upper()     # make text uppercase to match keys in MORSE_CODE
    lorem_str = lorem_str.replace(" ", "\n")  # each word on its own line

    # --- Perform the character‑by‑character translation ------------------------
    table = lorem_str.maketrans(MORSE_CODE)  # build translation table from the dict
    lorem_trans = lorem_str.translate(table) # convert the text to Morse code

    # --- Write the result to a new file ----------------------------------------
    output_file_name = "lorem_morse.txt"
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(lorem_trans)           # dump the converted string to disk

    return output_file_name            # let caller know where the result lives

    

if __name__ == '__main__':
    # Question 1
    Str= "lorem.txt"
    OUTPUT_FILE_NAME = english_to_morse(Str)
    print(f"Question 1 solution: {OUTPUT_FILE_NAME}")



 