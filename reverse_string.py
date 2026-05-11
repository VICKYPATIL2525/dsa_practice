# Reverse a string using a manual loop

def rev(a:str):
    result = ""
    for i in a:
        result = i+result
    return result

string1 = "Vicky-Patil"

print(rev(string1))