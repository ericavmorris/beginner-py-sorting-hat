# beginner-py-sorting-hat
for harry potter loving people wanting to get their feet wet in python

<html>
<body>

this app is good for beginners as the code is easy to understand ...basic statements and basic intent... but if you get stuck.. keep going :)


<h2>topics covered</h2>
<ul>
  <li>declaring variables</li>
  <li>strings and user input</li>
  <li>conditionals</li>
  <li>sorting & lists</li>
</ul>  


<h4>1. first things first</h4>
The first thing we’re going to do is declare our variables. A variable is used to store a value, this is subject to change. In this case, each variable will store a number that corresponds to the number of times a user selected a statement that would put them in a specified house. For example, a user who picks mostly "a’s" will be sorted into Gryffindor, since the “a” answers correspond to Gryffindor traits. We'll calculate and sort at the end though. 
  
each variable will start out at zero.
  ```
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
  ```
  

<h4>2. strings and things</h4>
A string in Python is a sequence of characters. It is a derived data type. Strings are immutable. This means that once defined, they cannot be changed. Many Python methods, such as replace() , join() , or split() modify strings. Input() allow users to enter a value. In this case our input will contain a question that will allow our users to provide an answer.

use "q1_answer" to create a variable to store the 1st answer.
```
q1_answer = input("""\nWhile walking down the street you see a wallet on the side of the road. It has a small amount of money in it,
but no identification of any kind. There is nobody in sight.
a) Leave it there. Someone is probably looking for it.
b) Pocket the money. You don't know who it belongs to, so finder's keepers
c) Take it to the police in case anyone ever reports it.
d) Take the wallet, and go around the area asking anyone if they have lost a wallet recently.\n""")
  ```
  
<h4>3. if this, then that</h4>
Now that we have our questions, and variable to store the first answer, how do we figure out how to make sure each answer is tied to the right house?

We want the outcome to be:
<ul>
  <li>A’s → Gryffindor</li>
  <li>B’s → Ravenclaw</li>
  <li>C’s → Hufflepuff</li>
  <li>D’s → Slytherin</li>
</ul>

Let's use an IF/ELSE statement. 
An "IF" Statement is used for decision-making operations. It contains a body of code which runs only when the condition given in the if the statement is true. If the condition is false, then the optional else statement runs which contains some code for the else condition.

If the user selects "A" we want the program to count 1 for A and increase the increment for subsequent  A answers. If the user selects "B" we want the program to increase "B" by an increment of 1.

Let's see this in action.
  ```
if  q1_answer == 'a':
    gryffindor += 1
elif q1_answer == 'b':
    ravenclaw += 1
elif q1_answer == 'c':
    hufflepuff += 1
elif q1_answer == 'd':
    slytherin += 1
else:
    print("Sorry, I dont understand that answer.") #just in case :)
  ```


<h4>4. specialis-revelio-sort (this was a try, i know)</h4>
Now that we have our program adding up the inputs for house in which we belong, we want to add a sorting method so the program knows when to rank one house over the other.
If the user has 3 inputs for Hufflepuff and 1 input for Gryffindor, then we want to return Hufflepuff over Gryffindor.</p>

  ```
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("\nCongrats, you're a Gryffindor!\n")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("\nCongrats, you're a Ravenclaw!\n")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("\nCongrats, you're a Hufflepuff!\n")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("\nCongrats, you're a Slytherin!\n")
else:
   print("\nYou're so complex! \nThis is how you scored:") 
   ```
Due to this quiz only being 4 questions, it's very possible that a person can choose a different house for every answer. Too combat this from happening you can create more questions or put a catch all phrase along with how they scored. 

Let's try our hand at a catch all phrase and a score breakdown.

  ```
  #simply add an "else" to end of the sort statement if the user is unsortable. 
  else:
   print("\nYou're so complex! \nThis is how you scored:") 
  ```

<h4> a little math </h4>
We can add an extra element by showing all users how they scored. This is especially valuable to those unsortable users. 
This is going to require a bit of math to get the total percentage and also converting our data types.

Here we want the string "gryf_total" to be recognized as a numeric value, so we have to add "int" before the calculation.
We can then divide each house by 4 and multiply by 100 to get the percentage breakdown of each house. 


 ```
gryf_total = int(gryffindor / 4 * 100)
rav_total = int(ravenclaw / 4 * 100)
huff_total = int(hufflepuff / 4 * 100)
sly_total = int(slytherin / 4 * 100)
 ```

<h4>lists</h4>

Now we have a way to calculate user breakdown, we have to create a put our houses in a list to accompany. A list is exactly what it sounds like. A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
  ```
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
  ```
And now we want to go through the list and return every house that list contains. 


 ```
for house in houses:
  print(house)
 ```
 
 and.. that's it! if your friend thinks they're a griffyndor and you think otherwise, now you can put them to your test.


<h4> 5. challenge your new found wizardy </h4>
<ul>
<li>Good programmers wrap up reusable parts of their code in functions. Functions are "self contained" modules of code that accomplish a specific task. Functions usually "take in" data, process it, and "return" a result. Once a function is written, it can be used over and over and over again. Try to implement functions in your program.</li>

<li>Add more questions. More questions, can add a more accurate outcome.</li>

<li>Implement a loop. If a user enters a bad character, we gotta do more than just tell them the character is bad. We have to ask the question over again. A loop will help you do just that.</li> 


</body>
</html>
