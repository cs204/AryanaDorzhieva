hi = input("Приветствие: ")
if hi.startswith("здравствуйте"):
    print("$0")
elif hi.startswith("з"):
    print("$20")
else:
    print("$100")