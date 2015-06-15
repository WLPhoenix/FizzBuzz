from __future__ import print_function

for n in range(1, 100):
    {
        (True, True): lambda: print("FizzBuzz"),
        (True, False): lambda: print("Fizz"),
        (False, True): lambda: print("Buzz"),
        (False, False): lambda: print(n),
    }[(n % 3 == 0, n % 5 == 0)]()
