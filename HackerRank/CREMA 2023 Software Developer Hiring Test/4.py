#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#
#

def longestChain(words):
    # Write your code here
    words = sorted(words, key=len)

    chains = {}

    for word in words:
        chains[word] = 1

        for i in range(len(word)):
            reduced_word = word[:i] + word[i+1:]
            if reduced_word in chains:
                chains[word] = max(chains[word], chains[reduced_word] + 1)

    print(chains)
    return max(chains.values())


words = ['a', 'and', 'an', 'bear']
print(longestChain(words))
