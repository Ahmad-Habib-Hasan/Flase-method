def my_function(x):
    return pow(x , 2) - x -1
    
a = -2
b = 0 
function_a = my_function(a)
function_b = my_function(b)

if(my_function(a)< 0 and my_function(b)> 0)or (my_function(a)> 0 and my_function(b)< 0):
    for i in range( 0 , 25):
        
        function_a = my_function(a)
        function_b = my_function(b)
        c = ((a*function_b) - (b* function_a))/(function_b - function_a)
        
        
        function_c = my_function(c)
        
        print("a:"+str(a))
        print("b:"+str(b))
        print("c:"+str(c))
        print("----------")
        if(function_c < 0 and function_a < 0) or (function_a>0 and function_c>0):
            a = c
        else:
            b = c 
else:
    print("it have not any root in this range")
