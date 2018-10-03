#
# Faded Palindrome
# check & construct a lexicographically smallest palindrome by replacing the '.' with suitable characters
#
def fadedPalindrome(s):
    hlen = len(s)
    slist = []
    slist.extend(s)
    for i in range(hlen//2):   # check, if given characters fulfill palindrome condition
        if slist[i] != '.' and slist[hlen-1-i] != '.' and slist[i] != slist[hlen-1-i]: 
            print(-1)
            return
    for i in range(hlen):      
        if slist[i] == '.' and slist[hlen-1-i] != '.': # fill '.' with character, which can be found symmetrical
            slist[i] = slist[hlen-1-i]
        elif slist[i] == '.':                          # fill '.' with 'a'
            slist[i] = 'a'
    print("".join(slist))

#
# demo
#
fadedPalindrome('a..ba...ca')  # output: acabaabaca
fadedPalindrome('a..ba...cb')  # output: -1 