print("Given a series of words, each on a separate line,")
print("this program finds the length of the longest word.")
print("Please enter several sentences, one per line.")
print("Finish with a blank line.")
maxi = 0
word = "."
while len(word) > 0:
    word = input()
    if len(word) > maxi:
        maxi = len(word)

if maxi == 0:
    print("There were no words.")
else:
    print("The longest sentence was " + str(maxi) + " characters long.")
