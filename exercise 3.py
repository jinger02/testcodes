x = input('Enter score\n')

try:
    x=float(x)
        
    if x>=0.9 and x<=1.0:
         print('A')
            
    elif x>=0.8 and x<0.9:
         print ('B')
            
        
    elif x>=0.7 and x<0.8:
        print('C')
           
       
    elif x>=0.6 and x<0.7:
        print ('D')
            
      
    elif x<0.6 and x>=0:
        print ('F')
            
    elif x>1.0:
        print ('Please enter a number between 0 to 1')
            
    else:
        print ('Enter a positive number')

except (ValueError):
    print ('Please enter a number between 0 to 1')
    
