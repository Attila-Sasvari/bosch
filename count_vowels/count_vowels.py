def count_vowels(word: str) -> int:
    """Return number of vowels in given word."""
    VOWELS = "aeiou"

    letters = [w for w in word]

    vowel_count = len([l for l in letters if l in VOWELS])

    return vowel_count
