words = ["skin", "order","stain","summer", "detailed","example","glib","settle","encouraging","snatch", "autumn"]

import random 
print(words)
import string

def get_valid_word(words):
    word = random.choice(words) #randoma izvelas kadu vardu
    while '-' in word or ''in word:
        word = random.choice(words)

        return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #burti word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # ko speletajs jau ir minejis

    lives = 6 

    #speletajs ievada
    while len(word_letters) > 0 and lives > 0:
        #izmantotie burti
        print( "tev ir", lives ,"dzivibas palikusas un tu esi izmantojis sos burtus:", ''.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word: ",''.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
         used_letters.add(user_letter)
         if user_letter in word_letters:
            word_letters.remove(user_letter)

         else:
            lives = lives - 1
            print("burts nav dotajā vardā")
            
        elif user_letter in used_letters:
            print("tu jau esi lietojis so burtu, megini atkal")
        else:
            print("nepareiz burts, meginiet atkal")
            
            if lives == 0:
                print("tev beidzās dzīvibas")
            else:
                print("Tu uzvarēji")
# seit tiek kad len(word_letters) == 0 or when lives == 0

hangman()


