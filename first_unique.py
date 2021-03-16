def firstUnique(var):
    emptydict = {}
    for z in "abcdefghijklmnopqrstuvwxyz":
        emptydict.update({z:[0,0]})
    
    ## first pass
    for z in var:
        emptydict[z][1]+=1
    
    unique_exists = False
    unique_letters = ""
    for z in "abcdefghijklmnopqrstuvwxyz":
        if emptydict[z][1] == 1:
            unique_exists = True
            unique_letters+=z     
            
    ## 2nd pass
    if unique_exists == False:
        return -1
    else:
        counter = -1
        arr = list(unique_letters)
        for z in arr:
            if counter == -1:
                counter = var.find(z)
            elif var.find(z) < counter:
                counter = var.find(z)
        return counter
        
            
