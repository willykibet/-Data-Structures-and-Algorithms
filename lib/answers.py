#question 1 stacks

def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

# question 2 remove duplicates

def remove_duplicates(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result


# question 3 dictionaries

import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)