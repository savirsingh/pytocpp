# Py To CPP
## Convert Python Code To C++

Py To CPP searches files for Python-unique syntax and converts it to the C++ equivalent. 

### It doesn't work perfectly yet:
| Statements/Syntax  | Status |
| ------------- | ------------- |
| If/Else If/Else  | ❌  |
| For Loops | ✅  |
| While Loops | ❌  |
| Print Statements | ✅  |
| Input (int/str) | ✅  |
| Variable Assignments (int, str) | ✅  |
| Format Conversions | ❌  |

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
