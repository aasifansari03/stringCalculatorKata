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

4. This condition is used to check if there's an uppercase letter in the string. If any uppercase letter is found then we break out of the for loop & throw an exception message conveying the same.

```
capital_flag = 0
            for i in lst:
                 if (ord(i[-1]) >= 65 and ord(i[-1]) <= 90):     # checking for capital letters
                     capital_flag = 1
                     break
                 else:
                     continue
```

5. This piece of code is used to get the ASCII values of the lowercase letters so that we can assign positional values to the lowercase letters & use it for addition.

```
for i in range(len(lst)):
            if (ord(lst[i][-1]) >= 97 and ord(lst[i][-1]) <= 122):     # getting the alphabet from the string
                lst[i] = ord(lst[i]) - 96
            else:
                lst[i] = int(lst[i])
```

6. All negative values are stored in the list called negatives which are displayed when negative numbers are entered in the string.

```
negatives = []
        for i in lst:
            if i < 0:
                negatives.append(i)
```

7. All valid characters in the string are added. Values greater than 1000 is ignored.

```
print("Addition of string : " + str(sum([j if j <= 1000 else 0 for j in lst])))     # adding string only if they are equal & less than 1000
```

