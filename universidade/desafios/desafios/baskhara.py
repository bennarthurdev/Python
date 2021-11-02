#import math module
import math
#input of all coefficients
try:
    a = float(input("Digite o coeficiente a, para uma função f(x) = ax² + bx +x:"))
    b = float(input("Digite o coeficiente b, para uma função f(x) = ax² + bx +x :"))
    c = float(input("Digite o coeficiente b, para uma função f(x) = ax² + bx +x :"))
    x = "false"    
except:
    x = "true"
    
if (x == "true"):
    print("Code runtime be stoped here")
elif(x == "false"):    
    #delta
    delta = b**2 - 4*a*c
    #square root delta
    Sqrt_delta = math.sqrt(delta)
    x = (-b + Sqrt_delta)/(2*a)
    x2 = (-b - Sqrt_delta) / (2*a)
    print("As raízes dessa equação são x = " + str(x) + " e x2 = " + str(x2))
else:
    print("Raíz não está entre os reais")
