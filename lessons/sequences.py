"""Examples pf the tuple and range sequences."""

#An example of a tuple without aliasing 
goat: tuple[str, int] = ("MJ", 23)

# Tumpes are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

#Seqeunces have length 
print(len(goat))

#Sequences are iterable with for...in loops 
#Meaninf you can loop over them with for...in 
for item in goat:
    print(item)

#Tuples, unlike lists, are immutable 
#which means we cannot reassign items, nor append, nor pop, etc.
#goat[0] = "LBJ"


#we can "invent our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type 
unc_pay: Player = ("Bacot", 5)

#In a strange world, where jersey number changes...
unc_pay = (unc_pay[0], unc_pay[1] + 1)

#A range is another common sequence type 
zero_to_nine: range = range(0, 10,1)

#We can access items of the range 
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print[i]

#   We can have different steps for more control 
odds_to_99: range(1, 100, 2)
for i in odds_to_99:
    print(i)