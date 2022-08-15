# Py To CPP
## Convert Python Code To C++

![logo](https://user-images.githubusercontent.com/84334654/184727184-4c00ace5-46c1-4527-b081-ebf60692dc8b.png)

Py To CPP searches files for Python-unique syntax and converts it to the C++ equivalent. 

### It doesn't work perfectly yet:
| Statements/Syntax  | Status |
| ------------- | ------------- |
| If/Else If/Else  | ❌  |
| For Loops | ✅  |
| While Loops | ❌  |
| Print Statements | ✅  |
| Input (int/str) | ✅  |
| Variable Assignments (int/str) | ✅  |
| Format Conversions | ❌  |

Feel free to contribute and add/improve any of these features. 

My email address is kopichiki@gmail.com if you need it.

### Keep these things in mind:
- Don't use unnecessary brackets in your output/print statement.

  #### DO NOT code like this (❌):
  ```
  a = 100
  b = 10

  for i in range(10):
    print((a+b)*10)
  ```
  #### Code like this (✅):
  ```
  a = 100
  b = 10
  c = a+b
  
  for i in range(10):
    print(c*10)
  ```
- Don't rely entirely on Py To CPP.
  
  #### It's important to have some C++ skills, even when using this automated converter. It will help you debug potential issues and/or optimization opportunities for   very large script conversions.
  
### Take a look at the examples included in this repository (both Python and C++).

## What it can do (in depth):
- Convert print statements to std::cout (by simply replacing "print(" with "cout << " and replacing ")" with either " << endl;" or another string of your choice).
- Convert both string inputs and integer inputs to std::cin (through removal of " = input()" and addition of " >> cin").
- Convert for loops by replacing relevant syntax and adding "}" to the next unindented line.
- Convert lists to std::vector by (inefficiently) analysing list's contents (int/str).
- Convert integers to strings and vice versa by detecting and replacing the relevant syntax if "input" is not present in the line.
- Convert pass statements to ";" (by literally finding "pass" and changing it to ";").
- Output new C++ file contents in shell window.
- Ask to save C++ file (.cpp) in the same directory.
- Check if files actually exist in directory, if not, return an error and restart.

Thank you for spending the time to look at my repository. I hope it benefits you and you learn something new from it! I feel it's pretty amazing that I was able to make this without using any artificial intelligence packages (I didn't want it to have any dependencies).

I must admit, I will be using this in future!

- Savir Singh (kopichiki@gmail.com)
