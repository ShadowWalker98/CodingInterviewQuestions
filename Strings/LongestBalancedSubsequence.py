
'''
Given a string S, find the length of longest balanced subsequence in it. A balanced string is defined as:-

A Null string is a balanced string.
If X and Y are balanced strings, then (X)Y and XY are balanced strings.

'''
def longestCommonSubsequence(qstring):
    # init a var to keep track of invalid open braces
    invalidOpenBraces = 0
    # init a var to keep track of invalid closed braces
    invalidClosedbraces = 0
    # loop through the input
    for i in range(len(qstring)):
        # check if the char at position i is '('
        if qstring[i] == '(':
            # increase the invalidOpenBraces
            invalidOpenBraces += 1
        else:
            # check if there are any leftover open braces
            if invalidOpenBraces == 0:
                # since there aren't any, we increase the closed braces counter
                invalidClosedbraces += 1
            else:
                # otherwise we decrement the invalidOpenBraces count
                invalidOpenBraces -= 1
    return len(qstring) - (invalidOpenBraces + invalidClosedbraces)

if __name__ == "__main__":
    ans = longestCommonSubsequence('()(((((()')
    print("Ans is: ", ans)

