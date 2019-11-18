#! /usr/bin/python

# Generate a big list of usernames.
# Currently assumes firstinitial + lastname
# Plenty of room for tweaks and expansion.

alpha = "abcdefghijklmnopqrstuvwxyz"
names = open("lastnames")
out = open("usernames", "w")
for name in names:
    for letter in alpha:
        out.write("{}{}".format(letter, name))
