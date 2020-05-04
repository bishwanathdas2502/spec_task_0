# Accept a string from user and display only those character which are present at even index number

def even_character(s):
    ans = []
    n = len(s)
    for i in range(len(s)):
        if i&1 == 0:
           ans.append(s[i])
    return ans

if __name__=='__main__':
    s = input('Enter a string')
    ans = even_character(s)
    for i in ans:
        print(i,end = " ")

