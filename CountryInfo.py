

from countryinfo import CountryInfo
count = input("enter a country name: ")

country = CountryInfo(count)

print("capital of this country is: ", country.capital())
print("currencies of this country is: ", country.currencies())
print("language of this country is: ", country.languages())
# print("other names of this country is :", country.alt_spelling())
print("Border: ", country.borders())
