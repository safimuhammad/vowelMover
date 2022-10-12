#should identify vowels
#move to the place of nearest vowel when n=1

from itertools import cycle      



def vowelIdentifier(li=[],a=''):
    test="this is a test"
    fList=li
    arr= list(test)
    state= False
    n=0
    index=[]
   
    vowels=['a','e','i','o','u']
   


    for i in vowels:
        if(a):
            if(a==i):
                state= True
        if(fList):
            for j in fList:
                if(j == i):
                    index.append(fList.index(j))
                    print(index)
                    n+=1
                   
    return state,n
    
# specimen 1
def vowelMover():
    
    test='this is a test'
    arr=list(test)
    n=1
    pool=cycle(arr)
    
    for i in range(len(arr)):
        if(vowelIdentifier(arr,arr[i])[0]==True):
            for j in range(i+1,len(arr),n):
                if(vowelIdentifier(arr,arr[j])[0]==True):
                    arr.insert(j,arr[i])
                    rem = arr.pop(i)
                    break
    print(''.join(arr))
      
        
       
#specimen 2
def testIter():
    test='this is a test'
    # output = "Thes is i tast!"
    arr=list(test)
    pool=cycle(arr)
    n=0
    
   
    totalVowels=0
    vowelDisplaced=0

    
       
    for i in range(len(arr)):
        # print(i,'chk i',len(arr))
        if(vowelIdentifier(arr,arr[i])[0]==True):
            for items in pool:
                if(i!=arr.index(items)):
                    if(vowelIdentifier(arr,items)[0]==True):
                        totalVowels=vowelIdentifier(arr,items)[1]
                        arr.insert(arr.index(items),arr[i])
                        rem = arr.pop(i)
                        n+=1
                        vowelDisplaced = n
                        
                        break
            if(vowelDisplaced==totalVowels):
                
                break
    print(''.join(arr),vowelDisplaced,totalVowels)



# test='this is a test'
#  # output = "Thes is i tast!"
# arr=list(test)
# pool=cycle(arr)
# n=0
# for i in range(len(arr)):
#     n+=1
    
  
#     print(next(pool))

#     if(n==len(arr)):
#         break            

# specimen 3
def test3():
    test='this is a test'
    c=test
    # output = "Thes is i tast!"
    arr=list(test)
    n=0
    vowelDisplaced=0
    totalVowels=1
    a=[]
    temp=''
    i=0
    
    maxi=len(arr)
    while i < len(arr):
        print(i)
        i=i+1
        if(vowelIdentifier(arr,arr[i])[0]==True):
            a.append(i)
            print(a)
            for j in range(i+1,len(arr)):
                if(vowelIdentifier(arr,arr[j])[0]==True):
                    totalVowels=vowelIdentifier(arr,arr[j])[1]
                    arr.insert(j, arr[i])
                    arr.pop(i)
                    n+=1
                    vowelDisplaced=n
                    temp=arr[j]
                    # print(''.join(arr))
                    break
         
        if(totalVowels+1==vowelDisplaced):
                 if(a):
                    c.replace(' ', '')
                    # print(arr[a[len(a)-1]],'sgsgs',c[8])
            
    
                 print(''.join(arr))
                 break
   
        # i=0

       
       
    

test3()







def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs






# test='this is a test'
# arr=list(test)
# print(vowelIdentifier(arr))
# vowelMover()

# testIter()

