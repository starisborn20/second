# try:
#     print("Hello")
# except:
#     print("An error occurred")

# try :
#     print(x)
# except:
#     print("THe name is not defined")
# finally:
#     print("Process code executed")

# x = -1
# if x < 0:
#     raise Exception("No number below zero is required")

x = "hello"

if not type(x) is int:
    raise TypeError("Only Integers are allowed")