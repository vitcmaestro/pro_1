s = "dhoni"
test = input("")
if(len(s) != len(test)):
    print("no")
else:
    if(test.count('d') == test.count('h') == test.count('o') == test.count('n') == test.count('i')):
        print("yes")
    else:
        print("no")
