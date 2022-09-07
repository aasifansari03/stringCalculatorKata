# stringCalculatorKata
## Problem Statement 

A string must be taken as an input. This string can contain all positive numbers & lowercase alphabets (alphabets will have the value as per their position for e.g. a=1, b=2...z=26). This string cannot have negative numbers, special characters, uppercase letters. Output of the add method should be the addition of all the valid characters. Add method should return 0 if the string is empty. Characters separated by commas and line break should only be considered for the addition.


1. This condition is used to check if the entered string is empty or not. If the string is empty it will return 0.

```
if(numbers == "" or numbers.strip() == ""):     # checking if the entered string is empty or not
            print(0)
```

2. Regular expression is defined and used to check if the string has a special character or not. If any special character is found, an exception message is given.

```
if((regex.search(numbers) != None)):             # checking special characters using regular expressions
                print('Special characters not allowed.')
```

3. This code block ignores blank spaces in the string if any then replaces the line break command with the comma. This string is split into a list using split() method.

```
numbers = numbers.replace(' ', '')        # replacing spaces with empty characters in the string
numbers = numbers.replace(r"\n", ',')     # replacing line break with comma
lst = numbers.split(",")                  # splitting into a list
```

4. 
