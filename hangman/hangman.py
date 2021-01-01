import output
import time

# Den Spieler einladen zu spielen
print("Willkommen bei Hangman")
name = input("Gib deinen Namen ein: ")
print("Hallo " + name + ", viel Glück!")
time.sleep(1)
print("Lasset das Spiel beginnen!")
time.sleep(2)


class visualisation:
    def __init__(self, word):
        self.word = word.upper()
        self.shown = ""
        self.guessed = []
        self.step = 0
        for i in word:
            if i != " ":
                self.shown += "-"
            else:
                self.shown += " "
    
    def trial(self, guess):
        if len(guess) != 1:
            print("Bitte nur einen Buchstaben eingeben!")
        elif guess.upper() in self.guessed:
            print("Diesen Buchstaben hast du bereits probiert!")
        elif guess.upper() in self.word:
            s = list(self.shown)
            for i in range(len(self.word)):
                if self.word[i] == guess.upper():
                    s[i] = guess.upper()
            self.shown = "".join(s)
            self.guessed.append(guess.upper())
            self.guessed.sort()
            return True
        else:
            self.guessed.append(guess.upper())
            self.guessed.sort()
            self.step += 1
            return False
    
    def print_shown(self):
        print(self.shown)
            
    def print_visualisation(self):
        for i in output.visualisation[self.step]:
            print(i)

    def print_guessed(self):
        if len(self.guessed) == 0:
            print("Du hast noch keine Buchstaben geraten...")
        else:
            tried = "Bisher versuchte Buchstaben: "
            for i in self.guessed:
                tried += i
                tried += " "
            print(tried)

    def is_dead(self):
        return self.step == len(output.visualisation) - 1

    def is_won(self):
        return not "-" in self.shown

    def go(self):
        while not self.is_won() and not self.is_dead():
            self.print_shown()
            self.print_visualisation()
            self.print_guessed()
            print("Rate einen Buchstaben!")
            guess = input(">> ")
            self.trial(guess)

        self.print_shown()
        self.print_visualisation()
        self.print_guessed()
        if self.is_won():
            print("Gratuliere, du hast das Wort erraten!")
        elif self.is_dead():
            print("Tut mir leid, das war wohl nichts!")
            