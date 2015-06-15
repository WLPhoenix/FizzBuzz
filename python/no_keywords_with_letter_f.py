import sys

map(sys.stdout.write,
    map(
        lambda n: "%s\n" % {
            (True, True): "FizzBuzz",
            (True, 1 == 0): "Fizz",
            (1 == 0, True): "Buzz",
            (1 == 0, 1 == 0): str(n)
        }[(n % 3 == 0, n % 5 == 0)],
        range(1, 100)
    ))
