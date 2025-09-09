#!/bin/bash

# Nutzer gibt eine URL oder Suchanfrage ein
input=$(rofi -dmenu -p "Enter URL or search:")

# Falls keine Eingabe gemacht wurde, abbrechen
[ -z "$input" ] && exit

# Falls die Eingabe bereits mit http:// oder https:// beginnt → Direkt öffnen
if [[ "$input" =~ ^https?:// ]]; then
    url="$input"

# Falls es wie eine Domain aussieht, aber ohne http(s) → Präfix hinzufügen
elif [[ "$input" =~ \. ]]; then
    url="https://$input"

# Falls es keine URL ist, als DuckDuckGo-Suche behandeln
else
    url="https://duckduckgo.com/?q=$(echo "$input" | sed 's/ /+/g')"
fi

# Website im Standardbrowser öffnen
xdg-open "$url"
