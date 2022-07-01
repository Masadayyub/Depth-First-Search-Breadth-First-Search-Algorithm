def baalti(g,r):
    bucket = []
    q = []
    bucket.append(r)
    q.extend(g[r])
    while len(q)!=0:
        print("traversed Graph : " ,bucket,"Q:",q)
        r = q[0]   #This will make the first element of Q "The Root"
        if r not in bucket:   # It will check whether it is already prsesnt or not in bucket
            bucket.append(r)
        q.pop(0)    #Remove the first element which has been added in bucket
        c = g[r]      #The graph of that first element which has been removed
        for i in c:    #This loop adds the nodes of root in Q
            if i not in bucket:
                q.append(i)
    return bucket,q




graph = {'a':['f','k','b'],'b':['c','d','a'],'c':['k','b'],'d':['b','f','e'],'e':['d'],
'f':['g','a','d'],'g':['f','h'],'h':['g','i'],'i':['j','k','h'],'j':['i'],'k':['i','a','c']}
root = 'a'
print('Root:',root)
mybucket = baalti(graph,root)
print('Traversed graph:',mybucket)


