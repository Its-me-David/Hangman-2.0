import random
import time

# Den Spieler einladen zu spielen
print("Willkommen bei Hangman")
name = input("Gib deinen Namen ein: ")
print("Hallo " + name + ", viel Glück!")
time.sleep(2)
print("Lasset die Spiele beginnen!")
time.sleep(3)

answerlist = []

answer = input("Bitte Wort eingeben: ")

# Überprüfen ob Wort mehr als einen Zeichen hat und aus Buchstaben besteht

if len(answer) > 1 and answer.isalpha():
    answerlist.append(answer)
    
    # Aufteilen des Wortes in seperate Buchstaben
    answer = list(answerlist[0])
    
    # Leere Liste "Display" erstellen
    display = []
    
    # Leere Liste der verwendete Buchstaben erstellen
    used = []
    
    # Buchstaben werden zu "Display" hinzugefügt wenn verwendet
    used.extend(display)
    
    # Inhalt der Liste "answer" wird zu "Display" hinzugefügt
    display.extend(answer)
    
    # Kopiert den Inhalt der Liste "Display" und fügt zu "answer" hinzu
    used.extend(display)
    
    # Iteriert durch "Display" und ersetzt Buchstaben mi "_"
    for i in range(len(display)):
        display[i] = "_"
        
    # Die "_" zusammenfügen und Leerzeichen zwischenfügen
    print(" ".join(display))
    print()
    
    # Bei count = len(answer) (Alle Buchstaben sind erraten worden) oder bei 5 falschen Rateversuchen ist das Spiel vorbei
    count = 0
    incorrect = 5
    
    # Fragt den Spieler weiter bis alle Buchstaben erraten sind (oder der Spieler stirbt)
    while count < len(answer) and incorrect > 0:
        guess = input("Bitte Buchstaben raten: ")
        guess = guess.lower()
        print(count)
        
        # Durch die Buchstaben iterieren und dabei richtige Buchstaben aus "used entfernen" und count weiter zählen lassen
        for i in range(len(answer)):
            if answer[i] == guess and guess in used:
                display[i] = guess
                count = count + 1
                used.remove(guess)
                
        if guess not in display:
            incorrect = incorrect -1
            print("Tut mir leid, das war ein falscher Buchstabe, du hast noch ",incorrect," Versuche")
            
        print("Du hast ",count," Buchstaben richtig erraten")
        
    if count == len(answer):
        print("Sehr gut, Du hast das Wort erraten!")
    else:
        print("Leider hast du keine Versuche mehe übrig, versuche es nocheinmal.")
        
        
else:
    print("Bitte ein Wort eingeben!")