from collections import Counter


def check_palindrome(text: str) -> bool:
    text = Counter(text)
    if len(list(filter(lambda key: text[key] % 2 != 0, text))) <= 1:
        return True
    else:
        return False


print(check_palindrome('adaaadf'))
