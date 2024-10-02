# s = [1, 2, 3]

# len(s)

# from math import sqrt

# sqrt(4)


# def func_1():
#     print("running func_1")


# func_1()


# def func_2(a, b):
#     return a * b


# print(func_2(3, 5))
# print(func_2([1, 2, 3], 5))


# def func_1():
#     return func_2()


# def func_4():
#     return

# i = 0

# while i < 5:
#     print(i)
#     i += 1

# i = 5

# while True:
#     print(i)
#     if i >= 5:
#         break

# input()

# min_length = 2

# while True:
#     name = input("Please Enter your name: ")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
# print("Hello, {0}".format(name))

# a = 0

# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)

# l = [1, 2, 3]
# val = 10

# found = False
# idx = 0
# while idx < len(l):
#     if l[idx] == val:
#         found = True
#         break
#     idx += 1

# if not found:
#     l.append(val)

# print(l)

# l = [1, 2, 3]
# val = 10
# idx = 0
# while idx < len(l):
#     if l[idx] == val:
#         break
#     idx += 1
# else:
#     l.append(val)

# print(l)

# a = 10
# b = 0
# try:
#     a / b
# except ZeroDivisionError:
#     print("division by 0")
# finally:
#     print("this always runs")


# while a < 4:
#     print("--------------------")
#     a += 1
#     b -= 1

#     try:
#         a / b
#     except ZeroDivisionError:
#         print("{0}, {1} - division by 0".format(a, b))
#         continue
#     finally:
#         print("{0}, {1} - always executes".format(a, b))

#     print("{0}, {1} - main loop".format(a, b))

# input()

# a = 0
# b = 10

# while a < 4:
#     print("--------------------")
#     a += 1
#     b -= 1

#     try:
#         a / b
#     except ZeroDivisionError:
#         print(f"{a}, {b} - division by 0")
#         break
#     finally:
#         print(f"{a}, {b} - always executes")

#     print(f"{a}, {b} - main loop")
# else:
#     print("Code executed without a zero division error")

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# i = None

# for i in range(5):
#     print(i)

# for i in [1, 2, 3, 4]:
#     print(i)

# for c in "hello":
#     print(c)

# for x in ("a", "b", "c", 4):
#     print(x)

# for i, j in [(1, 2), (3, 4), (5, 6)]:
#     print(i, j)

# for i in range(5):
#     if i ==3:
#         break
#     print(i)

# for i in range(1,5):
#     print(i)
#     if i % 7 == 0:
#         print('multiple of 7 found')
#         break
# else:
#     print('no multiple of 7 in the range')

# for i in range(5):
#     print("-----------------")
#     try:
#         10 / (i - 3)
#     except ZeroDivisionError:
#         print("divided by 0")
#     finally:
#         print("always runs")

#     print(i)


# s = "hello"
# for c in s:
#     print(c)


# s = "hello"
# i = 0
# for c in s:
#     print(i, c)
#     i += 1

# s = "hello"

# for i in range(len(s)):
#     print(i, s[i])

# s = "hello"
# for i, c in enumerate(s):
#     print(i, c)

# input()


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height


# r1 = Rectangle(10, 20)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# str(r1)
# hex(id(r1))


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def __str__(self):
#         return f"Rectangle: width={self.width}, height={self.height}"

#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"


# r1 = Rectangle(10, 20)
# print(str(r1))


# input()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def __str__(self):
#         return f"Rectangle: width={self.width}, height={self.height}"

#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"

#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.width == other.width and self.height == other.height
#         else:
#             return False

#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
#         else:
#             return NotImplemented

# r1 = Rectangle(10, 20)
# r2 = Rectangle(100, 200)
# print(r1 < r2)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def __str__(self):
#         return f"Rectangle: width={self.width}, height={self.height}"

#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"

#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.width == other.width and self.height == other.height
#         else:
#             return False

#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
#         else:
#             return NotImplemented


# r1 = Rectangle(10, 20)
# r2 = Rectangle(100, 200)
# print(r1 < r2)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")  # Corrected to 'raise'
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")  # Corrected to 'raise'
        else:
            self._height = height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)
