import random

answerlist = []

answer = input("Bitte Wort eingben: ")

# Überprüfen ob Wort mehr als einen Zeichen hat und aus Buchstaben besteht

if len(answer) > 1 and answer.isalpha():
    answerlist.append(answer)
    
    # Aufteilen des Wortes in seperate Buchstaben
    answer = list(answerlist[0])
    
    # Leere Liste "Display" erstellen
    display = []
    
    # Leere Liste der verbrauchten Buchstaben erstellen
    used = []
    
    # Buchstaben werden zu "Display" hinzugefügt wenn verwendet
    used.extend(display)
    
    # Inhalt der Liste "answer" wird zu "Display" hinzugefügt
    display.extend(answer)
    
    # Kopiert den Inhalt der Liste "Display" und fügt inn "answer" hinzu
    used.extend(display)
    
    # Iteriert durch "Display"
    for i in range(len(display))