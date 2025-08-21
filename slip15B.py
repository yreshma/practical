def MyStr():
    Str = input("Enter any String: ")
    cnt = len(Str)
    newStr = ""
    for i in range(cnt):
        if i % 2 == 0:
            newStr = newStr + Str[i]
    print("New String with removed odd Index Character: ", newStr)

# Main body
MyStr()
