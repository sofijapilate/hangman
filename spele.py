intro_message = """
Laipni lūdzu spēlē "hangman" 🧍‍♂️

Reiz sen senos laikos dzīvoja karaļa dēls Edmunds vienu dienu viņam piesolija nāves sodu. 
Viņu pakāra uz striķa un kad striķi nogriezīs, viņš iekrīt ugunskurā un nodegs. 
Bet tad karalis piedāvāja, lai kāds no iedzīvotājiem palīdz izglābt Edmundu un uzspēlē spēli.
Tu esi izvēlētais iedzīvotājs!
SPĒLES NOSACIJUMI👉 
 viss ir ļoti vienkārši 
 Tev ir jāmin vārdi kas ir paslēpti līnijās, 
 programma pati tev jautās lai mini burtus, 
 bet viss nav tik vienkārši tev ir tikai 6 iespējas minēt burtus,
 ja ievadītais burts ir nepareizs tad zaudē vienu iespēju,
 ja visas dzīvibas zaudē nu tu jau zini, kas notiks...
 
Palīdzi Edmundam!
""" 

print(intro_message)



words = ["skin", "order","stain","summer", "detailed","example","glib","settle","encouraging","snatch", "autumn"]

import random 
print("tavi dotie vārdi: ", words)
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
            print("Malacis tu uzminēji burtu!")
         elif user_letter in used_letters:
            print("tu jau esi lietojis so burtu, megini atkal🙃")    
        else:
            lives = lives - 1
            print("burts nav dotajā vardā, tu zaudēji dzīvību😕")
            
        if lives == 0:
            print("tev beidzās dzīvibas, tu zaudēji😢")
        


hangman()


