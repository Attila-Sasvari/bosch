def count_vowels(word: str) -> int:
    """Return number of vowels in given word."""
    VOWELS = "aeiou"

    vowel_count = len([l for l in list(word) if l in VOWELS])

    return vowel_count
