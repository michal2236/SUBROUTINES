text = "You never get a second chance to make a first impression"

def calculate(t, l):
    times = 0
    for i in range(0, len(t)):
        if text[i] == l:
            times += 1
    print(f"{times} times")
    
calculate(text, "e")