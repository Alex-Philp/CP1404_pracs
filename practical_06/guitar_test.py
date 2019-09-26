from practical_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
someotherguitar = Guitar("someguitar", 2013, 2.55)

print("Gibson L-5 CES get_age() - Expected 97. Got {}".format(Gibson.get_age()))
print("someotherguitar get_age() - Expected 6. Got {}".format(someotherguitar.get_age()))
print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(Gibson.is_vintage()))
print("someotherguitar is_vintage() - Expected False. Got {}".format(someotherguitar.is_vintage()))
