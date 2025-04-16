with open('ciphertext.txt', 'r') as file:
    cipher = file.read().strip().lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def removeMatches(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr += ch
    return newStr

def letterFrequencyCount(text):
    nonLetters = removeMatches(text, alphabet)
    text = removeMatches(text, nonLetters)
    letter_count = {}

    for ch in alphabet:
        letter_count[ch] = 0  # default to 0

    for ch in text:
        letter_count[ch] += 1

    return letter_count

def letterFrequencyPercent(text):
    nonLetters = removeMatches(text, alphabet)
    text = removeMatches(text, nonLetters)
    letter_freq = {}
    total = len(text)

    for ch in alphabet:
        letter_freq[ch] = 0

    for ch in text:
        letter_freq[ch] += 1

    for ch in letter_freq:
        letter_freq[ch] = round((letter_freq[ch] / total) * 100, 2) if total > 0 else 0.0

    return letter_freq

# calls and prints

counts = letterFrequencyCount(cipher)
percentages = letterFrequencyPercent(cipher)

print("Letter Frequency (Counts):")
for ch in alphabet:
    print(f"{ch}: {counts[ch]}")

print("\nLetter Frequency (Percentages):")
for ch in alphabet:
    print(f"{ch}: {percentages[ch]}%")
