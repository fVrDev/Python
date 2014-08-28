# -*- coding: cp1251 -*-

code = input()
number = ""
symb = prev_symb = ''
repeate = False

for i in range(1,len(code)):
   prev_symb = code[i-1]
   symb      = code[i]
   
   print(prev_symb + ", " + symb + " : ")
   
   if symb == prev_symb:
      if symb == '#':
         if not repeate:
            number += number[-1]
            repeate = True
      else:
         if not repeate:
            number += symb
            repeate = True
   else:
      repeate = False

print(number)

input()  
