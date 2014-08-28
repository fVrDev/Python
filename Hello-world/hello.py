# -*- coding: cp1251 -*-

f = int( input(u"Введите первое число[%d]: ") )
range_string = str( input(u"Введите диапазон второго числа [%d-%d]: ") )
range_value = range_string.split("-")
s0 = int(range_value[0])   
s1 = int(range_value[1]) + 1   
for s in range(s0,s1):
   print(str(f) + u" * " +str(s) + u" = " + str(f*s))
   
input(u"Нажмите любую клавишу для продолжения...")
