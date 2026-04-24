#Give user multiple choice to choose gun in game:

Gun = ["AK-47","M4A4","AWP","Dessert Eagle","MP9"]

print(Gun)
Gun1 = int(input("Select Gun 1 To 5:"))
Gun2 = int(input("Select Gun 1 To 5:"))

Nades = ["HE Grenade","Falshbang","Smoke Grenade","Molotov"]

print(Nades)
Nades1 = int(input("Select Nades 1 To 4:"))
Nades2 = int(input("Select Nades 1 To 4:"))

Knife = ["Main Knife","Machete","Sickle","Pan"]

print(Knife)
Knife1 = int(input("Select Knife 1 To 4:"))
Knife2 = int(input("Select Knife 1 To 4:"))
Knife3 = int(input("Select Knife 1 To 4:"))

Medi_kit = ["Med Kit","First Aid Kid","Bandage"]

print(Medi_kit)
Medi_kit1 = int(input("Select Medi_kit 1 To 3:"))

Boost = ["Energy Drink","Pain_killer","Adrenaline Syringe"]

print(Boost)
Boost1 = int(input("Select Boost 1 To 3:"))
Boost2 = int(input("Select Boost 1 To 3:"))


Bag = {"Gun1":Gun[Gun1-1],"Gun2":Gun[Gun2],"Nades1":Nades[Nades1-1],"Nades2":Nades[Nades2-1],
        "Knife1":Knife[Knife1-1],"Knife2":Knife[Knife2-1],"Knife3":Knife[Knife3-1],
        "Medi_kit1":Medi_kit[Medi_kit1-1],"Boost1":Boost[Boost1-1],"Boost2":Boost[Boost2-1]}
 
print(Bag)