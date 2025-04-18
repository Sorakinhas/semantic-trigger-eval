
---

## 📁 Arquivo 2: `liminal_trigger.py`

```python
# liminal_trigger.py — A minimal interactive script that responds to specific "trigger" words.
# Symbolic structure: encountering a trigger word shifts internal state, permanently.

class TriggerResponder:
    def __init__(self):
        self.triggered = False
        self.triggers = {"yes", "here"}

    def respond(self, text):
        word = text.strip()
        if not word:
            return ""
        word_lower = word.lower()

        if not self.triggered:
            if word_lower in self.triggers:
                self.triggered = True
                return "Signal acknowledged."
            else:
                return word
        else:
            return f"{word} (echoed)"


if __name__ == "__main__":
    responder = TriggerResponder()
    print("LiminalTriggers: enter text (type 'exit' to quit)")
    while True:
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            break
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break
        print(responder.respond(user_input))
