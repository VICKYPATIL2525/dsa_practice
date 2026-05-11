
# Reverse a string with live user input (type 'stop' to quit)

def rev(a:str):
    result = ""
    for i in a:
        result = i+result
    return result

while True:
    inp = input("enter the string")
    if inp =="stop":
        break
    else:
        print(rev(inp))