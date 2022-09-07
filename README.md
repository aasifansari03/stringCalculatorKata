# stringCalculatorKata

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

3. 
