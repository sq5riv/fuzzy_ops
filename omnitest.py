go = [1,4,6,4,12]
out =[3, 5,10,11,15]

def maker(go, out):
    tmp = go+out
    tmp.sort()
    var = 0
    retgo = []
    retout = []
    for i in tmp:
        if i  in go and  i not in out:
            var+=1
            if var == 1:
                retgo.append(i)
        elif i in go and i in out:
            pass
        elif i in out:
            var -=1
            if var == 0:
                retout.append(i)
            

    print(retgo, retout)

maker(go, out)
            
            
