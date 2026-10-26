def repeat_greeting(name, times):
    for number in range(times):
        print("Hello", name)


name = input("Enter a name: ")
times_text = input("How many times? ")
times = int(times_text)
repeat_greeting(name, times)
print("Done")