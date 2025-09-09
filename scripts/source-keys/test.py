import keyboard
import time

# Variable zur Steuerung, ob das Skript aktiv ist oder nicht
script_active = True

def toggle_script():
    """
    Schaltet das Skript ein/aus (entspricht AHK 'Suspend, Toggle' über F3).
    """
    global script_active
    script_active = not script_active
    if script_active:
        print("Skript AKTIVIERT.")
    else:
        print("Skript DEAKTIVIERT.")

def space_autohop():
    """
    Wird aufgerufen, wenn Space gedrückt wird. Sendet wiederholt 'Space',
    solange die Taste gehalten wird und das Skript aktiv ist.
    """
    while keyboard.is_pressed('space'):
        if not script_active:
            break
        # "Blind"-Äquivalent in AHK -> hier einfach direct send
        keyboard.send('space')
        # AHK Sleep 1 ~ 1ms; hier 0.001s
        time.sleep(0.001)

def x_autohop():
    """
    Wird aufgerufen, wenn X gedrückt wird. Sendet wiederholt 'Space' und 'E',
    solange X gehalten wird und das Skript aktiv ist.
    """
    while keyboard.is_pressed('x'):
        if not script_active:
            break
        keyboard.send('space')
        keyboard.send('e')
        time.sleep(0.001)

# Hotkeys registrieren
# F3 zum (De)Aktivieren des Skripts
keyboard.add_hotkey('f3', toggle_script)

# Space-Loop wie im AHK-Beispiel
keyboard.add_hotkey('space', space_autohop)

# X-Loop wie im AHK-Beispiel
keyboard.add_hotkey('x', x_autohop)

print("Autohop-Skript läuft. Drücke F3 zum Pausieren/Fortfahren.")
print("Zum Beenden einfach das Fenster schließen oder Strg+C im Terminal drücken.")

# Warten, bis das Skript manuell beendet wird
keyboard.wait()

