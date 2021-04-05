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
A string in Python is a sequence of characters and a mutable data type. What does that mean? This basically means that once defined, they cannot be changed. Many Python methods, such as replace(), join(), or split() modify strings. However, they do not modify the original string. They create a copy of a string which they then modify and return to the caller. Input() allows users to enter a value. In this case our input will contain a question that will allow our users to provide an answer.

use "q1_answer" to create a variable to store the 1st answer.
```
#declaring variables / if this, then that

q1_answer = input("""\nWhile walking down the street you see a wallet on the side of the road. It has a small amount of money in it,
no identification of any kind and nobody in sight.
a) Take it to the police in case anyone ever reports it.
b) Leave it there. Someone is probably looking for it.
c) Take the wallet, and go around the area asking anyone if they have lost a wallet recently.
d) Pocket the money. You don't know who it belongs to, so finder's keepers.\n""")
  ```
  
<h4>3. if this, then that</h4>
Now that we have our questions, and a variable to store the first answer, how do we figure out how to make sure each answer is tied to the right house?

We want the outcome to be:
<ul>
  <li>A’s → Gryffindor</li>
  <li>B’s → Ravenclaw</li>
  <li>C’s → Hufflepuff</li>
  <li>D’s → Slytherin</li>
</ul>


<p>Let's use an IF/ELSE statement. 
An "IF" Statement is used for decision-making operations. So essentially, _If_ X happens do Y, _Else_ do Z. 

If the user selects "a" we want the program to count 1 for a and increase the increment for subsequent "a" answers. 
If the user selects "b" we want the program to increase "b" by an increment of 1.

Let's see this in action. </p>
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
Now that we have our program adding up the inputs for the house in which we belong, we want to add a sorting method so the program knows when to rank one house over the other.

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
Note: Mitigate dissapointment for your users
Due to this quiz only being 4 questions, it's very possible that a person can choose a different house for every answer. To combat this from happening you can create more questions or put a catch all phrase along with how they scored. 

Let's try our hand at a catch all phrase and a score breakdown.

  ```
  #simply add an "else" statement to end of the sort statement if the user is unsortable. 
  else:
   print("\nYou're so complex! \nThis is how you scored:") 
  ```

<h4> a little math </h4>
We can add an extra element by showing all users how they scored. This is especially valuable to those unsortable users. 
This is going to require a bit of math to get the total percentage and we also have to convert our data types.

Here we want the string "gryf_total" to be recognized as a numeric value, so we have to add "int" before the calculation.
We can then divide each house by 4 and multiply by 100 to get the percentage breakdown of each house.
 ```
gryf_total = int(gryffindor / 4 * 100)
rav_total = int(ravenclaw / 4 * 100)
huff_total = int(hufflepuff / 4 * 100)
sly_total = int(slytherin / 4 * 100)
 ```
 Note: Please add this calculation before the previous sorting method.
 
<h4>lists</h4>

Now we have a way to calculate user breakdown, we have to create a put our houses in a list. A list is exactly what it sounds like, a data structure in Python that is a ordered sequence of elements.
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
And now we want to go through the list and return every house that the user could've been sorted into based on their answers. This is called _Iteration._

 ```
for house in houses:
  print(house)
 ```
 
 and.. that's it! if your friend thinks they're a griffyndor and you think otherwise, now you can put them to your test.


<h4> 5. challenge your new found wizardry </h4>
<ul>
<li>Good programmers wrap up reusable parts of their code in "functions." Functions are self contained modules of code that accomplish a specific task. Functions usually take in data, process it, and return a result. Once a function is written, it can be used over and over and over again. Try to implement functions in your program.</li>

<li>Add more questions. More questions can create a more accurate outcome.</li>

<li>Implement a loop. If a user enters a bad character, we gotta do more than just tell them the character is bad. We have to ask the question over again. A loop will help you do just that.</li> 


</body>
</html>
