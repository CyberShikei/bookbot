def count_words(s: str) -> int:
    return len(s.split())


def count_chars(s: str, char: str) -> int:
    return s.count(char)

# Count all alphabetical characters in a string


def count_each_char(s: str) -> dict:
    lower_s = s.lower()
    char_count = {}

    for char in lower_s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return sort_chars(char_count)


def sort_chars(c: dict, orient: str = "desc") -> dict:
    return dict(
        sorted(
            c.items(),
            key=lambda x: x[1],
            reverse=orient == "desc"
        )
    )
