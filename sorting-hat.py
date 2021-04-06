print ("Welcome to Erica's Hogwarts Sorting App.")
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#declaring variables / if this, then that
q1_answer = input("""\nWhile walking down the street you see a wallet on the side of the road. It has a small amount of money in it,
no identification of any kind and nobody in sight.
a) Take it to the police in case anyone ever reports it.
b) Leave it there. Someone is probably looking for it.
c) Take the wallet, and go around the area asking anyone if they have lost a wallet recently.
d) Pocket the money. You don't know who it belongs to, so finder's keepers.\n""")
if  q1_answer == 'a':
    gryffindor += 1
elif q1_answer == 'b':
    ravenclaw += 1
elif q1_answer == 'c':
    hufflepuff += 1
elif q1_answer == 'd':
    slytherin += 1
else:
    print("Sorry, I dont understand that answer.") #just in case:)

q2_answer = input("""\nWhat can you be found doing on the weekends?
a) Going on adventures
b) Reading a book
c) Spending time with family or friends
d) Plotting revenge on enemies\n""")
if  q2_answer == 'a':
    gryffindor += 1
elif q2_answer == 'b':
    ravenclaw += 1
elif q2_answer == 'c':
    hufflepuff += 1
elif q2_answer == 'd':
    slytherin += 1
else:
    print("Sorry, I dont understand that answer.")

q3_answer = input("""\nWhat would do if the Dark Lord were to invade your school?
a) Fight him
b) Look up some good defensive curses in a book
c) Stand by my friends no matter what
d) Help the Dark Lord invade the school\n""")
if  q3_answer == 'a':
    gryffindor += 1
elif q3_answer == 'b':
    ravenclaw += 1
elif q3_answer == 'c':
    hufflepuff += 1
elif q3_answer == 'd':
    slytherin += 1
else:
    print("Sorry, I dont understand that answer.")

q4_answer = input("""\nYou would be most hurt if someone called you...
a) Weak
b) Ignorant
c) Unkind
d) Boring\n """)
if  q4_answer == 'a':
    gryffindor += 1
elif q4_answer == 'b':
    ravenclaw += 1
elif q4_answer == 'c':
    hufflepuff += 1
elif q4_answer == 'd':
    slytherin += 1
else:
    print("Sorry, I dont understand that answer.")


#finding total percentage
gryf_total = int(gryffindor / 4 * 100)
rav_total = int(ravenclaw / 4 * 100)
huff_total = int(hufflepuff / 4 * 100)
sly_total = int(slytherin / 4 * 100)

#breakdown
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("\nCongrats, you're a Gryffindor!\n Breakdown:")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("\nCongrats, you're a Ravenclaw!\n Breakdown:")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("\nCongrats, you're a Hufflepuff!\n Breakdown:")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("\nCongrats, you're a Slytherin!\n Breakdown:")
else:
    print("\nYou're so complex! \nThis is how you scored:")

#create a list
houses = []
if gryf_total > 0:
    houses.append(" {}% Gryffindor".format(gryf_total))
if rav_total > 0:
    houses.append(" {}% Ravenclaw".format(rav_total))
if huff_total > 0:
    houses.append(" {}% Hufflepuff".format(huff_total))
if sly_total > 0:
    houses.append(" {}% Slytherin".format(sly_total))
for house in houses:
    print(house)
