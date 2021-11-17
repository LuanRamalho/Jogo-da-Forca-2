# i know its very messy but it was my first try to make something with python ~regards vga
import random

words = ['árvore', 'manga', 'codificação', 'humano', 'python', 'java',
         'jogo da forca', 'Amazona', 'ajuda', 'futebol', 'críquete', 'direção', 'vestir', 'apologia', 'motorista',
         'nave', 'piloto']
guess = words[random.randint(0, len(words)-1)].upper()
display = []
for x in guess:
    display.append("_")
print("*** JOGO INICIADO ****")
print("")
print("Adivinhe a palavra ! ", end=" ")
indexes = []
limbs = 6
userWon = False
userLost = False
guessedLetters = []


def start(word, indexes, display, limbs, userWon, userLost, guessedLetters):
    chance = False  # to stop recursion
    wrong_guess = False
    word_found = ""  # change it to True or False based on word found in the word array
    if userLost == False:
        if len(indexes) > 0:  # check on recursion if user entered any correct letter
            for val in indexes:
                # loop to change "_" with the correct letter in array
                display[val] = word[val]
        if len(guessedLetters) > 0:
            # display how many limbs left
            print("Você tem ", limbs, " chances restantes")
            print("")
            print("Suposições erradas", guessedLetters)
            print("")
        for dash in display:
            # print the display of "_" or the correct letter in the array
            print(dash, end=" ")
        print("")
        print("")
        user_guessed = input(
            "Adivinhe digitando uma letra ou a palavra completa para ganhar!: ").upper()
        if len(user_guessed) == 1:  # if user entered only a letter
            word_found = False
            for i in range(len(word)):  # to get the index of word array
                if(word[i] == user_guessed):  # match every single letter
                    if i in indexes:  # if user already guessed correct letter
                        print("Você já adivinhou a letra ", word[i])
                        chance = True
                        word_found = True
                        break
                    else:
                        indexes.append(i)
                        print("Bom palpite foi ", word[i])
                        word_found = True
        elif len(user_guessed) > 1:  # if used tried to guess by a word
            if(word == user_guessed):
                print("Uau, a sorte está do seu lado, você venceu !")
                print("A palavra correta era ", word)
                userWon = True
            else:
                wrong_guess = True
        if user_guessed in guessedLetters:  # if user guessed wrong again with the same word/letter
            print("Você já tentou ", user_guessed)
            chance = True
        elif wrong_guess == True or word_found == False:  # when user guessed wrong reduce limbs
            guessedLetters.append(user_guessed)
            print("Eh, palpite errado")
            limbs -= 1
            if limbs == 0:
                userLost = True
            else:  # when limbs are not 0 user can still play with chance = true
                chance = True
        if chance == True:
            start(word, indexes, display, limbs,
                  userWon, userLost, guessedLetters)
            chance = False  # to stop recursion :X aryan
        elif len(indexes) > 0 and userWon == False and userLost == False and chance == False:
            if len(indexes) == len(word):  # if user guessed all letters
                print("Uau, você venceu ! :)")
                print("A palavra correta era ", word)
            else:
                start(word, indexes, display, limbs,
                      userWon, userLost, guessedLetters)
        elif userLost == True:  # all limbs are 0 so user lost
            print("Você tem ", limbs, " chances restantes")
            print("Desculpe, você perdeu :(")
            print("A palavra correta era ", word)


start(guess, indexes, display, limbs, userWon, userLost, guessedLetters)
