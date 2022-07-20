# Print name and welcome the person
def print_name(name):
    return f"Hello {name}. Welcome to my Daisi account."

def introduction(name, age):
    sent1 = print_name(name)
    sent2 = "You may Introduce yourself to anyone in this way."
    sent3 = f"My name is {name}. I am {age} years old." 
    return f"{sent1}\n{sent2}\n{sent3}"
