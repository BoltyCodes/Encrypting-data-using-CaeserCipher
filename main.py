#Encrypting messages in a text file


#ceaser cipher; method for encrypting messages
def CaeserCipher(string, k):

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefgihjklmnopqrstuvwxyz'

    newCipher = ''

    for letter in string:
        if letter in upper:
            if upper.index(letter) + k > 25:
                indexPosition = (upper.index(letter) + k) - 26
                newCipher = newCipher + upper[indexPosition]
            else:
                indexPosition = upper.index(letter) + k
                newCipher = newCipher + upper[indexPosition]
        elif letter in lower:
            if lower.index(letter) + k > 25:
                indexPosition = (lower.index(letter) + k) - 26
                newCipher = newCipher + lower[indexPosition]
            else:
                indexPosition = lower.index(letter) + k
                newCipher = newCipher + lower[indexPosition]

    return newCipher




true = True
message = input("Enter the message you want to encrypt: ") 
print(CaeserCipher(message, 3))
    


