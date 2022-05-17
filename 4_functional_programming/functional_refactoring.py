def calculate(a, b, action):
    if action == "+":
        return a + b
    elif action == "-":
        return a - b
    elif action == "*":
        return a * b
    elif action == "/":
        return a / b
    else: 
        return f"Unexpected action '{action}'"


while True:
    print(
        calculate(
            int(input("Input first number: ")),
            int(input("Input second number: ")),
            input("Input an action [+, -, *, /]: ")
        )
    )
    
    print("Done.")
