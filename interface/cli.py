from .functions.wc import count_words, count_each_char


def format_output(output: dict) -> str:
    formatted_output = ""
    for key, value in output.items():
        formatted_output += f"{key}: {value}\n"
    return formatted_output


def start_cli(s: str) -> None:
    word_count = count_words(s)
    char_count = count_each_char(s)
    output = {"Word count": word_count, **char_count}
    formatted_output = format_output(output)
    print(formatted_output)
