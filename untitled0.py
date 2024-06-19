def my​func(x = 10, y, z = True):
    for i in ra​nge(y):
        if z​:
            x +​= 10
            Flag = n​ot z
        elif x >​= 30:
            Fl​ag = z
        else​:
            z = n​ot z
            Flag = x !​= 20
    retur​n Flag

prin​t(myfunc(20, 2))