def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "no. of upper case characters : %s,no. of lower case characters : %s"%(u,l))
up_low("'The quick Brow Fox'")
