if __name__ == "__main__":
    
    # add function
    def add(numbers):             # takes string of comma separated elements
        lst = numbers.split(",")  # splitting into a list
        
        # converting lowercase alphabets to integers
        for i in range(len(lst)):
            if ord(lst[i]) >= 97 and ord(lst[i]) <= 122:
                lst[i] = ord(lst[i]) - 96  
        
        for i in lst:
            print(i)
       
    add("5,6,2,a,b,c,d,z")
