# in this challenge we will check if a list is applicable to return a pythagoren triplets
# our assumptions 
#[3,4,5] = True
# [4] = False
# [12,1,7,9]= False
 
 # the code:

 #create a function to check if list is pythagoren triplets
lst = [3, 4, 6]
def p_t(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i]**2 + lst[j]**2 == lst[k]**2:
                    
                    #return True
                    print("we got pythagoren triplet")
                else:
    
    #return False
                    print("we dont have it!")
                    #return False
p_t(lst) 


    

