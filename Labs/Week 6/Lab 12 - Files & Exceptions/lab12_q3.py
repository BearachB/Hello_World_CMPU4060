def prompt_open(mode):
    while True:
        try:
            user_prompt = input("Input the filename:")
            file = open(user_prompt, mode)
        except FileNotFoundError:
            print("Try again!")
        else:
            break
    return(file)

print(prompt_open("r"))
