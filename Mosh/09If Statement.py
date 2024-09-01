temperature=12

if temperature>30:
    print("it's a hot day")
    print("Drink plenty of water")
elif temperature>20: # (20, 30]
    print("it's a nice day")
elif temperature>10:
    print( " it is a bit cold day")
else:
    print("It's a cold day")
print('Done')