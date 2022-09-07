import re

if __name__ == "__main__":
    

    # add function
    def add(numbers):     # takes string of comma separated elements
    
        
        if(numbers == "" or numbers.strip() == ""):     # checking if the entered string is empty or not
            print(0)   
        else:
            # checking for special characters
            regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')     # defining regular expressions
            if((regex.search(numbers) != None)):             # checking special characters using regular expressions
                print('Special characters not allowed.')
            else:
                numbers = numbers.replace(' ', '')        # replacing spaces with empty characters in the string
                numbers = numbers.replace(r"\n", ',')     # replacing line break with comma
                lst = numbers.split(",")                  # splitting into a list
                
                
                # checking for capital letters
                capital_flag = 0
                for i in lst:
                    if (ord(i[-1]) >= 65 and ord(i[-1]) <= 90):     # checking for capital letters
                        capital_flag = 1
                        break
                    else:
                        continue
                if(capital_flag == 1):
                    print('Sorry, capital letters not allowed. Please use lowercase letters only.')
                else:
                    # converting alphabets to integers
                    for i in range(len(lst)):
                        if (ord(lst[i][-1]) >= 97 and ord(lst[i][-1]) <= 122):     # getting the alphabet from the string
                            lst[i] = ord(lst[i]) - 96
                        else:
                            lst[i] = int(lst[i])
        
        
                    # counting negative numbers
                    negatives = []
                    for i in lst:
                        if i < 0:
                            negatives.append(i)
        
        
                    if(len(negatives) > 0):   
                        print("You entered these negative numbers : "+ str(negatives) +". Negative numbers are not allowed.")     # printing all the negative numbers
                    else:
                        print("Addition of string : " + str(sum([j if j <= 1000 else 0 for j in lst])))     # adding string only if they are equal & less than 1000


    numbersString = input('Enter numbers string: ')
    add(numbersString)
