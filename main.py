if __name__ == "__main__":
    
    # add function
    def add(numbers):     # takes string of comma separated elements
        if(numbers == "" or numbers.strip() == ""):     # empty string is handled here
            print(0)
            
        else:
            lst = numbers.split(",")     # splitting into a list
            
            # converting alphabets to integers
            for i in range(len(lst)):
                if ord(lst[i])>=97 and ord(lst[i])<=122:
                    lst[i] = ord(lst[i]) - 96
            
            for i in lst:
                print(i)
                
    add("")
