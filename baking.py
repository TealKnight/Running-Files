num_cookies = int(input("How many cookies do you want to make? "))
#print("type of num_cookies is", type(num_cookies))
recipe_mult = num_cookies/12
#print("num_cookies is", num_cookies)
#print("recipe_mult is", recipe_mult)
butter = str(125*recipe_mult) + "g butter"
sugar = str(225*recipe_mult) + "g sugar"
eggs = str(max(1,round(recipe_mult))) + " eggs"
vanilla = str(recipe_mult) + " tsp vanilla extract"
flour = str(225*recipe_mult) + "g flour"
salt = str(0.5*recipe_mult) + " tsp salt"
chips = str(200*recipe_mult) + "g chocolate chips"
print(butter)
print(sugar)
print(eggs)
print(vanilla)
print(flour)
print(salt)
print(chips)
