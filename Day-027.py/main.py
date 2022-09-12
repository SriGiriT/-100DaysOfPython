def add(*args):
  return sum(args)

print(add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]
  return n

print(calculate(2, add=3, multiply=5))