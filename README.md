# Adarts Browser Themes

Willkommen im Repository für benutzerdefinierte Browser-Themes für Adarts. Hier kannst du deine eigenen CSS-Kreationen teilen und die Themes anderer Nutzer finden.

## 🎨 Ein neues Theme erstellen

Um ein eigenes Theme beizusteuern, folge bitte diesen Schritten:

1.  **CSS erstellen**: Erstelle eine neue `.css` Datei im Hauptverzeichnis mit deinem Code. Wähle einen aussagekräftigen Dateinamen (z.B. `mein_cooles_theme.css`).
2.  **Screenshot erstellen**: Mache einen Screenshot deines Themes in Aktion.
    *   Speichere ihn im Ordner `screenshots/`.
    *   Benenne ihn exakt wie deine CSS-Datei, aber mit der Endung `.png` (z.B. `mein_cooles_theme.png`).
3.  **Registrieren**:
    *   Führe das Skript `python3 update_themes.py` aus. Dies fügt dein Theme automatisch zur `themes.json` hinzu.
    *   Öffne die `themes.json` und fülle das Feld `"description"` mit einer kurzen Beschreibung deines Themes aus.

## 📝 Pull Request (PR) Richtlinien

Damit dein Theme schnell akzeptiert werden kann, achte bitte auf folgende Punkte in deinem Pull Request:

*   **Dateien**: Der PR sollte mindestens 3 Änderungen enthalten:
    1.  Deine neue `.css` Datei.
    2.  Deinen Screenshot im `screenshots/` Ordner.
    3.  Die aktualisierte `themes.json`.
*   **Qualität**:
    *   Prüfe, ob dein CSS keine anderen wichtigen UI-Elemente ungewollt zerstört.
    *   Der Screenshot sollte das Theme klar zeigen.
*   **Beschreibung**: Gib deinem PR einen Titel wie `Add: Mein Cooles Theme` und beschreibe kurz, was dein Theme macht.

## ⚙️ Technische Details (`themes.json`)

Die `themes.json` steuert die Anzeige der Themes. Ein Eintrag sieht so aus:

```json
{
  "name": "Mein Cooles Theme",
  "description": "Dunkles Design mit roten Akzenten",
  "file": "mein_cooles_theme.css",
  "version": "1.0",
  "image": "screenshots/mein_cooles_theme.png"
}
```

*   `name`: Wird automatisch aus dem Dateinamen generiert.
*   `file`: Der Name deiner CSS-Datei.
*   `image`: Pfad zum Screenshot.
*   `version`: Startet bei "1.0". Wenn du dein Theme später aktualisierst, erhöhe diese Nummer bitte.

Vielen Dank für deinen Beitrag zur Community!
