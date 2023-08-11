char_dict = {
    'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e',
    'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j', 
    'a': 'k', 's': 'l', 'd': 'm', 'f': 'n',  'g': 'o',
    'h': 'p',  'j': 'q',  'k': 'r', 'l': 's', 'z': 't',
    'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y',
    'm': 'z'
}

sentence = input()

out_sentence = str()

for ch in sentence:
    if ch in char_dict.keys():
        out_sentence = out_sentence + char_dict[ch]
    else:
        out_sentence = out_sentence + ch

print(out_sentence)