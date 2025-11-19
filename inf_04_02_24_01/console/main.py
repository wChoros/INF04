class Text:
    _VOWELS = "aąeęiouóyAĄEĘIOUÓY"

    @staticmethod
    def count_vowels(text: str):
        if not text:
            return 0
        count = 0
        for letter in text:
            count += 1 if letter in Text._VOWELS else 0
        return count

    @staticmethod
    def remove_repeated_characters(text: str):
        new_text = text[0]
        previous_character = text[0]
        for character in text[1:]:
            if character != previous_character:
                new_text += character
            previous_character = character
        return new_text


if __name__ == "__main__":
    input_text = input("Podaj tekst do przetestowania: ")
    vowels = Text.count_vowels(input_text)
    not_repeated_text = Text.remove_repeated_characters(input_text)

    print(f"""
Ilość samogłosek - {vowels}
Tekst bez powtórzonych znaków obok siebie - {not_repeated_text}
""")
