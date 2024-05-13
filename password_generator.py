import random
from colorama import Fore, Style

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []
password_len = int(input("How long would you like your password to be? "))

if password_len < 1:
    print(f"{Fore.RED}Password cannot be less then 1 character!!{Style.RESET_ALL}")
elif password_len <= 5:
    while password_len >= 1:
        char = random.choice(characters)
        password_len -= 1
        password_list.append(char)
    password = ''.join(password_list)
    print(f"This is a really {Fore.MAGENTA}feeble{Style.RESET_ALL} password!\nPassowrd is: {Fore.MAGENTA}{password}{Style.RESET_ALL}")
elif password_len <= 8:
    while password_len > 0:
        char = random.choice(characters)
        password_len -= 1
        password_list.append(char)
    password = ''.join(password_list)
    print(f"This is a {Fore.RED}weak{Style.RESET_ALL} password!\nPassowrd is: {Fore.RED}{password}{Style.RESET_ALL}")
elif password_len <= 10:
    while password_len > 0:
        char = random.choice(characters)
        password_len -= 1
        password_list.append(char)
    password = ''.join(password_list)
    print(f"This is a {Fore.YELLOW}average{Style.RESET_ALL} password!\nPassowrd is: {Fore.YELLOW}{password}{Style.RESET_ALL}")
elif password_len <= 12:
    while password_len > 0:
        char = random.choice(characters)
        password_len -= 1
        password_list.append(char)
    password = ''.join(password_list)
    print(f"This is a {Fore.CYAN}strong{Style.RESET_ALL} password!\nPassowrd is: {Fore.CYAN}{password}{Style.RESET_ALL}")
else:
    while password_len > 0:
        char = random.choice(characters)
        password_len -= 1
        password_list.append(char)
    password = ''.join(password_list)
    print(f"This is a {Fore.GREEN}mighty{Style.RESET_ALL} password!\nPassowrd is: {Fore.GREEN}{password}{Style.RESET_ALL}")
