# Fortune-Cookie
This is a very basic program I made of a fortune cookie type thing

To do this, I first imported the module "random" as usual.

Then I created an array for all the possible fortunes That will be possible to get. I called this array "fortunes".

After that, I used the function **Random.choice** to choose a random fortune from the array.

I assigned the result of this function to the variable "RandomFortune"

I also wanted the fortune cookie to give a random lucky number to the user,

So I used the **Random.randint** function to choose an integer between 1 and 100.

I assigned the value of this to the variable "LuckyNumber"

Now that both the fortune and the lucky number had been chosen, I could create a print statement.

I turned the string into an f-string so that it would be easier for me to add in the variables.

If I wanted to use concatenation, I would have to convert the "LuckyNumber" from an integer to a string using the str() function.

This would have been more difficult.

Now, when you run the program, you get a random fortune and a lucky number.
