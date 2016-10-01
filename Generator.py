def compute(s):
    n = len(s)
    ans = "No solution"
    depth = 0
    i = n-1
    while(i>=0):
        if(s[i] == '('):
            depth-=1
        else:
            depth+=1
        if (s[i] == '(' and depth > 0):
            depth-=1
            open = (n-i-1 - depth) // 2
            close = n-i-1 - open
            ans = s[0:i] + ')' + str(open*'(') + str(close*')')
            break
        i-=1
    return ans

l = int(input())
s = ['(' if i<l else ')' for i in range(2*l)]
s = "".join(s)
count =0
while(s!="No solution"):
    print(s)
    s = compute(s)
    count+=1
print(count)