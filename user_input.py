# user_input.py

def get_user_input():
    name = input("What's your name? ")

    while True:
        age = input("How old are you? ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a valid age (a number).")

    location = input("Where do you live? ")
    favorite_color = input("What's your favorite color? ")

    return name, age, location, favorite_color

def print_personalized_message(name, age, location, favorite_color):
    print(f"Hello {name}, you are {age} years old, live in {location}, and your favorite color is {favorite_color}.")

# Main program
if __name__ == "__main__":
    user_info = get_user_input()
    print_personalized_message(*user_info)