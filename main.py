if __name__ == "__main__":
    
    # add function
    def add(numbers): # takes string of comma separated elements
        lst = numbers.split(",")  # splitting into a list
        for i in lst:
            print(i)
       
    add("5,6,2,a")
