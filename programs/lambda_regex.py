import re
# Extract digits from strings
data = ["abc123", "hello2024 99 000", "no digits", "zip2007", "he77o"]
digits = list(map(lambda s: re.findall(r'\d+', s), data)) # returns only the digits (with the use of '\d+' in the string s - data)
print(digits)


# Replace all non-alphabetic characters
data2 = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]
cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]', '', s), data2))  # '^' means any one occurence
print(cleaned)


# Convert all email addresses to domain names
emails = ["alice@gmail.com", "bob@yahoo.in", "user@outlook.com"]
domains = list(map(lambda s: re.search(r'@(\w+)\.', s).group(1), emails))  # '\' means all the occurence
print(domains)


# Capitalize words that start with vowels
words = ["apple", "banana", "orange", "grape", "umbrella"]
# Capitalize the letter if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou]', lambda m: m.group(0).upper(), w), words))
print(vowel_caps)
# Capitalize the entire word if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)', w.upper(), w), words))
print(vowel_caps)


# Replace multiple spaces with a single space
texts = ["Hello   World", "Python    is great", "No extra   spaces please"]
normalized = list(map(lambda t: re.sub(r'\s+', ' ', t), texts))
print(normalized) 