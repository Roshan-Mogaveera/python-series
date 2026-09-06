import random 
# ● ┌ ─ ┐ │ └ ┘
'''"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"'''


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│    ●    │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"), 


    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),  

    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),       
           
}

dice = []
total = 0
num = int(input("Enter the number of dice :  "))

for die in range(num):
    dice.append(random.randint(1,6))

for die in range(num):
    for line in dice_art.get(dice[die]):
        print(line)    
print(f"dice is {dice}")


for die in dice:
    total +=die
print(f"Total is : {total}")

