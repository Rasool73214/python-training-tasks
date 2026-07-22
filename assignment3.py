
def display_frequency(words):
    print("\nWord Frequencies:")
    for word in words:
        print(word, ":", words[word])
frequency = {}
try:
    file = open("words.txt", "r")
    for line in file:
        word = line.strip()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    file.close()
except FileNotFoundError:
    print("words.txt file not found.")
display_frequency(frequency)