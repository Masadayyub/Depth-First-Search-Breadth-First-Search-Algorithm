           #DEPTH FIRST SEARCH
def baalti(g,r):
    bucket = []
    q = []
    bucket.append(r)
    q.extend(g[r])
    while len(q)!=0:
        print("traversed Graph : " ,bucket,"Q:",q)
        r = q[0] #This will make the first element of Q "The Root"
        if r not in bucket:   # It will check whether it is already prsesnt or not in bucket
            bucket.append(r)
        q.pop(0)   #This will remove the first element so that new elements will be added at start
        c = g[r]   #The graph of that first element which has been removed
        d = []   #I made this empty list to add the next elements at start
        for i in c:   #This loop is used to add elements at start
            if i not in bucket:
                d.append(i)   #It will append the elements which belong to the root removed in new list 
                q = d+q #i added q in d to preserve order because we have to add new elements at start and assign it as q
    return bucket,q




graph = {'a':['f','k','b'],'b':['c','d','a'],'c':['k','b'],'d':['b','f','e'],'e':['d'],
'f':['g','a','d'],'g':['f','h'],'h':['g','i'],'i':['j','k','h'],'j':['i'],'k':['i','a','c']}
root = 'a'
print('Root:',root)
mybucket = baalti(graph,root)
print('Traversed graph:',mybucket)


