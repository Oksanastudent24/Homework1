n = int(input("Введите число:"))

def fizz_buzz(n):
     for i in range (1, n+1):
         if i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
         elif i % 5 == 0:
            print("Buzz")
         elif i % 3 == 0:
            print("Fuzz")
         else:
            print(i)
     
fizz_buzz(n)