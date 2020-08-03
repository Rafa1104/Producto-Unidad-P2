import RPi.GPIO as GPIO
import math
import time

GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

class Calculadora_2v:

  number1 = 0
  number2 = 0

  def _init_(self,number1,number2):
    self.number1 = number1
    self.number2 = number2
  def suma(self,number1,number2):
    return(number1+number2)
  def resta(self,number1,number2):
    return(number1-number2)
  def multiplicacion(self,number1,number2):
    return(number1*number2)
  def division(self,number1,number2):
    return(number1/number2)
  def potenciacion(self,number1,number2):
    return(math.pow(number1,number2))
  def logaritmo(self,number1,number2):
    return(math.log(number1,number2))

  def leer(self,mensaje):
    print(mensaje)
    msg = float(input())
    return msg

  def imprimir(self,num1,num2,resultado,operacion):
    if operacion == 1:
      print(num1,"+",num2,"=",resultado)
    elif operacion == 2:
      print(num1,"-",num2,"=",resultado)
    elif operacion == 3:
      print(num1,"*",num2,"=",resultado)
    elif operacion == 4:
      print(num1,"/",num2,"=",resultado)
    elif operacion == 5:
      print(num1,"^",num2,"=",resultado)
    elif operacion == 6:
      print("Log",num2,"(",num1,") = ",resultado)

  def operar(self,opcion,num1,num2):
    resultado = 0
    if opcion == 1:
      resultado = self.suma(num1,num2)
    elif opcion == 2:
      resultado = self.resta(num1,num2)
    elif opcion == 3:
      resultado = self.multiplicacion(num1,num2)
    elif opcion == 4:
      resultado = self.division(num1,num2)
    elif opcion == 5:
      resultado = self.potenciacion(num1,num2)
    elif opcion == 6:
      resultado = self.logaritmo(num1,num2)
    return resultado

class Calculadora_1v:

  number = 0

  def _init_(self,number):
    self.number = number
  def raiz_cuad(self,number):
    return(math.sqrt(number))
  def fun_exp(self,number):
    return(math.exp(number))
  def log_natural(self,number):
    return(math.log(number))
  def log_base10(self,number):
    return(math.log10(number))
  def sin(self,number):
    return(math.sin(number))
  def arcsin(self,number):
    return(math.asin(number))
  def cos(self,number):
    return(math.cos(number))
  def arcos(self,number):
    return(math.acos(number))
  def tan(self,number):
    return(math.tan(number))
  def arctan(self,number):
    return(math.atan(number))

  def leer(self,mensaje):
    print(mensaje)
    msg=float(input())
    return msg

  def imprimir(self,num,resultado,operacion):
    if operacion == 7:
      print("√(",num,") =",resultado)
    elif operacion == 8:
      print("e ^",num,"=",resultado)
    elif operacion == 9:
      print("Ln","(",num,") = ",resultado)
    elif operacion == 10:
      print("Log10(",num,") =",resultado)
    elif operacion == 11:
      print("sin(",num,") =",resultado,"rad")
    elif operacion == 12:
      print("Arcsin(",num,") = ",resultado,"rad")
    elif operacion == 13:
      print("cos(",num,") = ",resultado,"rad")
    elif operacion == 14:
      print("Arcosn(",num,") = ",resultado,"rad")
    elif operacion == 15:
      print("tan(",num,") = ",resultado,"rad")
    elif operacion == 16:
      print("Arctan(",num,") = ",resultado,"rad")

  def operation(self,opcion,num):
    resultado = 0
    if opcion == 7:
      resultado=self.raiz_cuad(num)
    elif opcion == 8:
      resultado = self.fun_exp(num)
    elif opcion == 9:
      resultado = self.log_natural(num)
    elif opcion == 10:
      resultado = self.log_base10(num)
    elif opcion == 11:
      resultado = self.sin(num)
    elif opcion == 12:
      resultado = self.arcsin(num)
    elif opcion == 13:
      resultado = self.cos(num)
    elif opcion == 14:
      resultado = self.arcos(num)
    elif opcion == 15:
      resultado = self.tan(num)
    elif opcion == 16:
      resultado = self.arctan(num)
    return resultado

#clase  
class detectOP():
  def read(self):
#Constructor   
    if GPIO.input(3) == GPIO.HIGH:
      nmop = "Suma"
      opt = 1
    elif GPIO.input(5) == GPIO.HIGH:
      nmop = "Resta"
      opt = 2
    elif GPIO.input(7) == GPIO.HIGH:
      nmop = "Multiplicación"
      opt = 3
    elif GPIO.input(8) == GPIO.HIGH:
      nmop = "División"
      opt = 4
    elif GPIO.input(10) == GPIO.HIGH:
      nmop = "Potenciación"
      opt = 5
    elif GPIO.input(11) == GPIO.HIGH:
      nmop = "Logaritmo de x en base y"
      opt = 6
    elif GPIO.input(12) == GPIO.HIGH:
      nmop = "Raiz cuadrada de x"
      opt = 7
    elif GPIO.input(13) == GPIO.HIGH:
      nmop = "Función Exponencial"
      opt = 8
    elif GPIO.input(15) == GPIO.HIGH:
      nmop = "Logaritmo Natural"
      opt = 9
    elif GPIO.input(16) == GPIO.HIGH:
      nmop = "Logaritmo Base 10"
      opt = 10
    elif GPIO.input(18) == GPIO.HIGH:
      nmop = "Seno"
      opt = 11
    elif GPIO.input(19) == GPIO.HIGH:
      nmop = "Arco Seno"
      opt = 12
    elif GPIO.input(21) == GPIO.HIGH:
      nmop = "Coseno"
      opt = 13
    elif GPIO.input(22) == GPIO.HIGH:
      nmop = "Arco Coseno"
      opt = 14
    elif GPIO.input(23) == GPIO.HIGH:
      nmop = "Tangente"
      opt = 15
    elif GPIO.input(24) == GPIO.HIGH:
      nmop = "Arco Tangente"
      opt = 16
    else:
      print("Operación no Disponible.")
      print("Ingrese Nuevamente el Pin")
      print("\n")
      return(0)
    
    print("∙Ha escogido la operación: " + nmop)
    return(opt)
  
calcu = Calculadora_2v()
calculadora = Calculadora_1v()
option = detectOP()
print("********************************")
print("     CALCULADORA CIENTÍFICA     ")
print("********************************")
print("\n")
print("Operaciones Disponibles:")
print("-Pin3: Suma               -Pin11: Logaritmo de x en Base y     -Pin18: Seno")
print("-Pin5: Resta              -Pin12: Raiz Cuadrada de x           -Pin19: Arco Seno")
print("-Pin7: Multiplicación     -Pin13: Función Exponencial          -Pin21: Coseno")
print("-Pin8: División           -Pin15: Logaritmo Natural            -Pin22: Arco coseno")
print("-Pin10: Potenciación      -Pin16: Logaritmo Base 10            -Pin23: Tangente")
print("\n")

pinState = 0
while pinState == 0:
  print("Ingrese Pin...")
  print("\n")
  time.sleep(15)
  opcion = option.read()
  pinState = opcion
  
#print(opcion)

if opcion <=6:  
  num1 = calcu.leer("Ingresar Valor de x")
  num2 = calcu.leer("Ingresar Valor de y")
  resultado = calcu.operar(opcion,num1,num2)
  calcu.imprimir(num1,num2,resultado,opcion)

elif opcion >=7: 
  num = calculadora.leer("Ingresar Valor de x")
  resultado = calculadora.operation(opcion,num)
  calculadora.imprimir(num,resultado,opcion)