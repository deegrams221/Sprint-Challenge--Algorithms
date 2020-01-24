'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    test_th = 0

    # if the len of word is equal to 0, return 0
    if len(word) == 0:
        return 0

    # else if the first letter of the word is equal to 't' and the next letter is equal to 'h'
        # set to lower case
    # elif word[0].lower() == 't' and word[1].lower() == 'h':
    #     test_th += 1
    #     count_th(word[1: ])
    # this was my first attemt, it only has 3 tests pass becasue it only looked at the first 2 letters
        # in a word - need to account for words that don't have 'th' as the first letters in the word


    # else if 'th' is in the word, then return 1 + the function replace the first time 'th' shows in
        # a word for the recursive call to work
    elif 'th' in word:
        return 1 + count_th(word.replace('th', ' ', 1))

    # else the function(using slice notation '1: ')
    else:
        count_th(word[1: ])

    # return the test_th
    return test_th