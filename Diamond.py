# Give me a Diamond

def diamond(n):
    if n%2==0 or n<=0:
        return None
    else:
        diamond = ""
        for i in range(1,n+1):
            if i%2!=0:
                diamond += " "*((n-i)//2) + "*"*i + "\n"

        for j in range(n-2,0,-1):
            if j%2!=0:
                diamond += " "*((n-j)//2) + "*"*j + "\n"

        return diamond