#task 1

email = input("Enter an email: ")

# Check if the email is valid
if email.count("@") != 1:
    print("Invalid email")
else:
    at = email.find("@")
    dot = email.rfind(".")

    if dot < at:
        print("Invalid email")
    else:
        # Username
        username = email[:at]

        # Domain
        domain = email[at + 1:dot]

        # Domain type
        if email.endswith(".com"):
            domain_type = "Commercial Domain"
        elif email.endswith(".edu"):
            domain_type = "Educational Domain"
        else:
            domain_type = "Other Domain"

        print("Username:", username)
        print("Domain:", domain)
        print(domain_type)


# Task 2


message = "###!!@mocleW EPGTQ!!!6789"

# Keep only letters and spaces
core = ""
for ch in message:
    if ch.isalpha() or ch == " ":
        core += ch

words = core.split()

# Reverse first word
first_word = words[0][::-1]

# Second word
second_word = words[1]

print("\nTask 2")
print(first_word, second_word)



# Task 3


message = "&&&**$gnirtS PLIO!!@1234"

core = ""
for ch in message:
    if ch.isalpha() or ch == " ":
        core += ch

words = core.split()

first_word = words[0][::-1]

second_word = words[1]
second_word = second_word.replace("I", "E")
second_word = second_word.replace("O", "U")

print("\nTask 3")
print(first_word, second_word)



# Task 4


message = "##$$$@!yalpstcejorp EPUVT****9887"

core = ""
for ch in message:
    if ch.isalpha() or ch == " ":
        core += ch

words = core.split()

first_word = words[0][::-1]

second_word = words[1]
second_word = second_word.replace("E", "A")
second_word = second_word.replace("U", "O")

print("\nTask 4")
print(first_word, second_word)