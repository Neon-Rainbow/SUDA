def GetIntNumers(s):
    a=s.split()
    # b=map(int,a)
    # c=list(b)
    # res=[int(str(c[2*i])+str(c[2*i+1])) for i in range(len(c)//2)]
    # return res
    return [int(a[2*i]+a[2*i+1]) for i in range(len(a)//2)]

def DeleteRepeatedNumbers(a):
    return list(set(a))
    # a=a[::]
    # for i in range(len(a)-1,0,-1):
    #     if a.count(a[i])>1:
    #         a.pop(i)
    # return a

def MySort(a):
    a.sort(key=lambda x:int(str(x)[-1])+int(str(x)[-2]),reverse=True)
    return a

def Display(a,width=10, cols=2, direct=1):
    if direct==1:   #右对齐
        ft="%"+str(width)+"d"
    else:
        ft="%-"+str(width)+"d"
    for i in range(len(a)):
        print(ft%a[i],end='')
        if (i+1)%cols==0:
            print()
    if len(a)%cols!=0:
        print()

def GetMaxMinAver(a):
    a=a[::]

    res=[]
    res.append(max(a))
    res.append(min(a))
    res.append(sum(a)/len(a))
    return res

def main():
    s="24 53 91   70 70 1   12 87 102 46 70 1   33 7 9 13 70 1 5 3 11 2 70 1  5 67 453 54 78 32 58 561 902 32 34 21 1045 143 17 13 271 79 13 9 13"
    a=GetIntNumers(s)
    a=DeleteRepeatedNumbers(a)
    a=MySort(a)
    Display(a)
    res=GetMaxMinAver(a)
    print("%-10d"%res[0])
    print("%-10d" % res[1])
    print("%-10.3f" % res[2])