MAX_TRIES = 6

def print_opening():
    print("""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print(MAX_TRIES)

def choose_word(file_path, index):
    """
    the function get from the file path and location the specific word
    :param file_path: the adress of the file
    :type file_path: str
    :param index: the location of the word
    :type index: int
    :return: a tuple with the word and the amount of different words
    :rtype: tuple
    """
    my_file1 = open(file_path, "r")
    text1 = my_file1.read()
    text1 = text1.split()
    #print(text1)
    copy_list = list(dict.fromkeys(text1))
    length = len(copy_list)
    my_list = []
    my_list.append(length)
    total_length = len(text1)
    while index > total_length:
        index = index - total_length
    word = text1[index - 1]
    my_list.append(word)
    my_list = tuple(my_list)
    return my_list

def show_hidden_word(secret_word, old_letters_guessed):
    """
    function that make the frame of your progress
    :param secret_word: the word u need to guess
    :type secret_word: str
    :param old_letters_guessed:
    :type: list
    :return: string with the secret wort obly with using old letters
    :rtype: str
    """
    new_frame = []
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            new_frame.append(secret_word[i])
        else:
            new_frame.append("_")

    new_frame = " ".join(new_frame)
    return new_frame

def check_valid_input(letter_guessed):
    """
        the function is checking if the string is valid
        :param letter_guessed: the guess
        :type letter_guessed: str
        :return: true/false if the guess is valid
        :rtype: bool
        """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == 0:
        valid = False
    else:
        valid = True
    return valid

def check_win(secret_word, old_letters_guessed):
    """
    function that check if that a win by checking if u can make the secret word only with old letters
    :param secret_word: the word u need to guess
    :type secret_word: str
    :param old_letters_guessed: the letters u already guessed
    :type old_letters_guessed: list
    :return: true/false if that a victory
    :rtype: bool
    """
    x = len(secret_word)
    count = 0
    for i in range(x):
        if secret_word[i] in old_letters_guessed:
            count += 1
    if count == x:
        b = True
    else:
        b = False

    return b

def print_hangman(num_of_tries):
    """
    function that print the hangman depand on the number of fails
    :param num_of_tries: number of fails
    :type num_of_tries: int
    :return: string of the hangman (asci paint)
    :rtype: str
    """
    hangman_photos = {1: """x-------x""", 2: """x-------x
|
|
|
|
|""", 3: """x-------x
|       |
|       0
|
|
|""", 4: """x-------x
|       |
|       0
|       |
|
|""", 5: """x-------x
|       |
|       0
|      /|\\
|
|""", 6: """x-------x
|       |
|       0
|      /|\\
|      /
|""", 7: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}

    photo = hangman_photos[num_of_tries]

    print(photo)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
        the function is checking if the string is valid (and if it used before) and add unvalid numbers
        :param letter_guessed: the guess
        :type letter_guessed: str
        :param old_letters_guessed: the letters that you already guessed
        :type old_letters_guessed: str
        :return: true/false if the guess is valid
        :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == 0 or letter_guessed in old_letters_guessed:
        valid = False
        print("X")
        old_letters_guessed.sort(key=str)
        old_letters_guessed = " -> ".join(old_letters_guessed)
        print(old_letters_guessed)
    else:
        valid = True
        old_letters_guessed.append(letter_guessed)
        #print(old_letters_guessed)
    return valid

def main():
    print_opening()
    file_address = str(input("Enter file location of the word bank: "))
    word_location = int(input("Enter the location of the word (number): "))
    bank_words = choose_word(file_address, word_location)
    bank_words = list(bank_words)
    secret_word = bank_words[1]
    old_letters = []
    num_of_tries = 1
    print("\nLet's start! \n    ")
    win = False
    valid = False
    correct = False

    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters))

    while (win == 0) and (num_of_tries < 7):
        valid = False

        while valid == 0:
            letter = str(input("Guess a letter: "))
            valid = check_valid_input(letter)
            if valid == 0:
                print("X")
            else:
                valid = try_update_letter_guessed(letter, old_letters)

        if letter in secret_word:
            correct = True
        else:
            correct = False

        if correct == 0:
            print(":(")
            num_of_tries += 1
            print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters))

        win = check_win(secret_word, old_letters)
    if win == 1:
        print("WIN")
    else:
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters))
        print("LOSE")


if __name__ == "__main__":
    main()