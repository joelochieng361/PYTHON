# A dictionary  is a data type that stores data in terms of keys - value pairs
# It is introduced by the use of calibraces {}
# The values stored within the dictionary can be of any data type.abs

phonebook = {
    "Benson" : "0726252423",
    "Mary" : "0726252423",
    "Stephen" : "0726252423"
    }

#showing the entire phonebook
print(phonebook)
print(type(phonebook))

player = {
    "name" : "Messi",
    "Age" : "41",
    "teams" : ["PSG", "BARCELONA", "ARGENTINA"]
}

#print barcelona - the second team he played for

print(player["teams"][1])