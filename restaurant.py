
#CS175
#Ludrianna Bazile
#restaurant
vegetarian = False
vegan = False
gluten_free = False

vegetarianResponse = input("Is anyone in your party a vegetarian ")
if vegetarianResponse == "yes":
    vegetarian = True
if vegetarianResponse == "no" :
    vegetarian == False

veganResponse = input("Is anyone in your party a vegan ")
if veganResponse == "yes":
    vegan = True
if veganResponse == "no" :
    vegan == False

gluten_freeResponse = input("Is anyone in your party a gluten free ")
if gluten_freeResponse == "yes":
    gluten_free = True
if gluten_freeResponse == "no" :
    gluten_free == False

print("\n")

print("Here are your restaurant choices.")


if vegetarian == False and vegan == False and gluten_free == False:
   print("Joe's Gourmet Burgers")

if vegan == False and gluten_free == False:
   print("Mama Fine Italian")

if vegan == False:
   print("Main Street Pizza")

print("Corner Café")
print("The Chef's Kitchen") 
