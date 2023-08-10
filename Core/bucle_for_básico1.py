#Básico
for i in range(0, 151):
    print(i)

#Múltiplos de 5
for j in range(5, 1001):
    if j % 5 == 0:
        print(j) 

#Contar, a la manera del Dojo
for k in range(1, 101):
    if k % 5 == 0:
        print("Coding")
        if k % 10 == 0:
            print("Coding Dojo")  
    else:
        print(k)

#Whoa. Es un gran idiota
sum_impares = 0
for l in range(0, 500001):
    if l % 2 != 0:
        sum_impares += l
print(sum_impares)

#Cuenta regresiva de a 4
for m in range(2018, 0, -4):
    print(m)

#Contador flexible
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)