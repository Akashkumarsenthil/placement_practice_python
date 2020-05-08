def alphabetDiamond(n):
    iSPoint = 1 + n//2                   # Starting point for first character
    iNofc   = ((n-1) // 2) + 1           # number of possible characters per line, sep. with - 
    if iNofc % 2 == 0:
        iNofc = iNofc - 1                # number of characters must be odd, otherwise we get no diamond
    iLines = (iNofc // 2) + 1            # number of lines to the widest extension
    hStartChar = chr(ord('a')+iNofc//2)  # what is the start character?
    hline = iSPoint - 1                  # number of '-' for the first line before the first character
    i = 0
    for i in range(iLines):              # prints the upper part of the diamond
        print((hline-2*i)*"-" + genCharChain(hStartChar,(1+i*2)) + (n-(1+4*i)-(hline-2*i))*'-')
    hline -= 2*i
    for i in range(1,iLines):            # prints the lower part of the diamond
        print((hline+2*i)*"-" + genCharChain(hStartChar,iNofc-i*2) + (n-(2*iNofc-i*4-1)-(hline+2*i))*'-')
#
# generates the character chain
#
def genCharChain(c,i):    
    sRes1 = c              # starting with one character  
    sRes2 = ""
    for k in range(1,i//2+1):
        sRes1 += "-" + chr(ord(c) - k)
        sRes2  = "-" + chr(ord(c) - k + 1) + sRes2
    return sRes1 + sRes2 

alphabetDiamond(63)







--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------