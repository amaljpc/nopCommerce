import string


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


def format_user_info(user):
    formatter = string.Formatter()

    template = "Name: {name}\nAge: {age}\nEmail: {email}"
    formatted_info = formatter.format(template, email=user.email, name=user.name, age=user.age)

    return formatted_info

def format_user_info1(*user):
    # print(user)
    print(f"Name: {user[0]}\nAge: {user[1]}\nEmail: {user[2]}")
# Create a User object
user = User("John Doe", 30, "johndoe@example.com")

# Format and print user information
# formatted_user_info = format_user_info(user)
# print(formatted_user_info)
format_user_info1("John Doe", 30, "johndoe@example.com")
