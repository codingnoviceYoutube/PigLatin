import tkinter as tk

def pig_latin(word):
    if len(word) < 1:
        return ""

    first_letter = word[0]
    rest_of_word = word[1:]

    return rest_of_word + first_letter + "ay"

def translate_sentence(sentence):
    words = sentence.split()
    pig_latin_words = [pig_latin(word) for word in words]
    return " ".join(pig_latin_words)

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pig Latin Translator")

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Translate", command=self.on_button_click)
        self.button.pack()

        self.label = tk.Label(self)
        self.label.pack()

    def on_button_click(self):
        sentence = self.entry.get()
        pig_latin_sentence = translate_sentence(sentence)
        self.label.config(text=pig_latin_sentence)

if __name__ == "__main__":
    app = PigLatinTranslator()
    app.mainloop()
