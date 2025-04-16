import re

scramble = ['gbson', 'rvuxyz', 'mopqi']
partial = ['AzzRExxIVE', 'AiiInAL', 'spNpsAL']

def checkWord2(rep_str, target):
    reList = []
    pattern = ''

    for ch in target:
        if ch.islower():
            pattern += f"[{rep_str}]"
        else:
            pattern += ch.lower()

    pattern += '$'

    with open('words.txt', 'r') as wordFile:
        for line in wordFile:
            word = line.strip().lower()
            if re.match(pattern, word):
                reList.append(word)

    return reList

final_results = []

for s in scramble:
    for p in partial:
        result = checkWord2(s, p)
        if result:
            final_results.append(result)

# calls and print
print("Final Matches:")
for match in final_results:
    print(match)
