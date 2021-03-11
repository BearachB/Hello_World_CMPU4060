country_dict = {}
country = ""
capital = ""
print("Enter your country, capital pairs to add them to the dictionary. If you want to exit enter a full stop ('.') into either input.")

while True:
    country = input("Enter a country: ")
    if country == ".":
        break
    capital = input("Enter a capital: ")
    if capital == ".":
        break
    country_dict[country] = capital

dict_sorted = sorted(country_dict.values())

print("Your capitals in alphabetical order are:", dict_sorted)
