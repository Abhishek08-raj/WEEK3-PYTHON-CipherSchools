#word counter
d={'h':2, 'a':1, 'h':2}
print(d)


def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_counter("Ankit"))