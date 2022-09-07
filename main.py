if __name__ == "__main__":
    
    # add function
    def add(numbers):     # takes string of comma separated elements
    
        if(numbers == "" or numbers.strip() == ""):
            print(0)   
        else:
            lst = numbers.split(",")  # splitting into a list
            
            # converting alphabets to integers
            for i in range(len(lst)):
                if ord(lst[i][-1])>=97 and ord(lst[i][-1])<=122:     # getting the alphabet from the string
                    lst[i] = ord(lst[i]) - 96
                else:
                    lst[i] = int(lst[i])
                             
            # counting negative numbers
            negatives = []
            for i in lst:
                if i< 0:
                    negatives.append(i)

            if(len(negatives)>0):
                print("You entered these negative numbers : "+ str(negatives) +". Negative numbers are not allowed")
            else:
                print("Addition of numbers : "+ str(sum(lst)))
                  
    add("5,1,a,d,3,-1,-4")
