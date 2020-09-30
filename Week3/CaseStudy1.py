"""A cipher is a secret code for a language. In this case study, we will explore a cipher that is reported by
 contemporary Greek historians to have been used by Julius Caesar to send secret messages to generals during times
 of war.
The Caesar cipher shifts each letter of a message to another letter in the alphabet located a fixed distance from
the original letter. If our encryption key were 1, we would shift h to the next letter i, i to the next letter j,
and so on. If we reach the end of the alphabet, which for us is the space character, we simply loop back to a.
To decode the message, we make a similar shift, except we move the same number of steps backwards in the alphabet.
In the five exercises of this homework, we will create our own Caesar cipher, as well as a message decoder for this
cipher."""


import string

alphabet = " " + string.ascii_lowercase
positions = {}
i = 0

for letter in alphabet:
    positions[letter] = i
    i += 1
print(positions)

message = "hi my name is caesar"


def encoding(message, key=0):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string


encoded_message = encoding(message, 3)
print(encoded_message)
decoded_message = encoding(encoded_message, -3)
print(decoded_message)


