*************************MAIN GOAL************
This is a small Python program that works like a coffee vending machine.
You choose a drink, put in money, and the machine tells you if you get the drink or not.
****************************************************************************************
What this program does
Shows a menu of drinks (like espresso, latte, cappuccino)

Checks if the machine has enough ingredients

Asks the user to insert money

Calculates if the money is enough

Makes the drink if everything is OK

Gives back change

Lets you turn the machine off

Lets you check the machine’s ingredient report

How it works (super simple explanation)
1. Menu
The program has a dictionary that stores:

the ingredients needed for each drink

the cost of each drink

2. Resources
Another dictionary stores how much water, milk, and coffee the machine has.

3. Money
The user enters how much money they are inserting.
The program checks:

If money < drink cost → “Not enough money”

If money ≥ drink cost → drink is made and change is returned

4. Making the drink
If the machine has enough ingredients, it subtracts the used amount from the resources.

5. Commands
off → turns the machine off

report → shows remaining water, milk, coffee, and money
