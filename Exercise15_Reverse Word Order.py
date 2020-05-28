# Print back to the user the same string, except with the words in backwards order

InputS = str(input("Please input a long string contains multiple words:"))
def Reverse_word_orderv1(S):
    result = S.split()
    result.reverse()
    return " ".join(result)

def Reverse_word_orderv2(S):
    return " ".join(S.split()[::-1])

print(Reverse_word_orderv1(InputS))
print(Reverse_word_orderv2(InputS))