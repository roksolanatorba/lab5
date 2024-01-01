Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from enum import Enum
... 
... class Gender(Enum):
...     FEMALE = 'FEMALE'
...     MALE = 'MALE'
...     NON_BINARY = 'NON_BINARY'
... 
... class Guest:
...     def __init__(self, guest_id, name, age, city, phone_number, gender):
...         self.id = guest_id
...         self.name = name
...         self.age = age
...         self.city = city
...         self.phone_number = phone_number
...         self.gender = gender
... 
... class Party:
...     def __init__(self, day, reason, guests):
...         self.day = day
...         self.reason = reason
...         self.guests = guests
... 
...     def find_average_age(self, gender):
...         selected_guests = [guest.age for guest in self.guests if guest.gender == gender]
...         if selected_guests:
...             return sum(selected_guests) / len(selected_guests)
...         else:
...             return 0
... 
...     def is_lucky_phone_number(self, phone_number):
...         return len([digit for digit in str(phone_number) if digit == '7']) > 3
... 
... guest1 = Guest(1, "Карина", 25, "Київ", +380123456789, Gender.FEMALE)
... guest2 = Guest(2, "Артем", 30, "Дніпро", +3980987654321, Gender.MALE)
... guest3 = Guest(3, "Женя", 22, "Тернопіль", +38061982777, Gender.NON_BINARY)
... 
... 
... party = Party('2023-15-01', 'Birthday', [guest1, guest2, guest3])
... 
... average_age_female = party.find_average_age(Gender.FEMALE)
... average_age_male = party.find_average_age(Gender.MALE)
... average_age_non_binary = party.find_average_age(Gender.NON_BINARY)
... 
... print(f"Average age of female guests: {average_age_female}")
... print(f"Average age of male guests: {average_age_male}")
print(f"Average age of non-binary guests: {average_age_non_binary}")


lucky_phone_number = party.is_lucky_phone_number(guest1.phone_number)
print(f"Is guest1's phone number lucky? {lucky_phone_number}")


sorted_guests = sorted(party.guests, key=lambda x: x.id)
for guest in sorted_guests:
    print(f"Guest {guest.id}: {guest.name}")

