name = input()

lastname, firstname = name.split(", ")

print(f"{firstname[:1].upper()}. {lastname.capitalize()}")
