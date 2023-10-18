# WE CREATING THE BINARY SEARCH ALGORITHM 

num = 0
# Here we can create an global variable
def search(list,n):
# now we can create a funtion for search in a list
    l =0
# Here the l is the lower bound value of list 
    u = len(list)-1
# Here the u is the upper bound value of our list
    while l<=u:
# now we can use the loop here  to chk the lower and upper bound are equal or not
        mid = (l+u)//2
# if the mid value is equal to our desired value then simply our globle variable is equal to our desired value
        if list[mid] == n:
            globals()['num'] = mid
            return True
          
# if the mid value is not equal to n then we proceed as follow
            
        else:
            if list[mid] < n:
# if the mid value is smaller then n then we change the lower bound value
                l = mid+1
            else:
                u = mid-1
            return False

list = [2,6,0,87,57,89,56,34]
n= int(input('Enter any number :'))
# here we can call the funtion
if search(list,n):
    print('Found at',num+1)
    
else:
    print('Not Found')
     

