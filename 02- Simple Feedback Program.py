#! TITTLE ==>   A SIMPLE FEEDBACK PROGRAM

# So we are going to create a program where our users will be asked Some Simple Question and they will be expexted to supply an answer.

# So it is important to learn how to add comments in your code so as to enable someone else,
# maybe a contributor on your project to understand what your code does and what each line mean.

# So we will start by:
# 01- Creating a vairable name, which will hold some question detail, and what ever we type afterwards will be stored in the variable.

name = input ("Please, tell me your name (User): ") 

# And we can print the input of name as a variable that is print (name) , but then: we can further add 'hello' to the output
# meaning we will concatenate two words into the string output.
# ~ meaning hello + name so that the output will look different such as:

print ('hello ' + name)       # When we run this we will have the output as hello and the name that will be supplied,
                        # if you don't give space after o before the quote on the i.e  'hello '  then your result will be jam packed.

# 02- We can also ask our audience to tell us their age, we will add another input as this:
age = input('...what is your age: ')

print ('Okay ' + age)

# 03- Maybe you want to let them you may need other things from them,

""
print ('I will love to know more about you, are you willing to proceed ')
""

# 04- we can also ask them another question, if for instance we want to find out about there complaxion
complexion = input ('...what is your complexion, (black or white): ')

print ('cool, ' + complexion)


# 05- We can go further to ask them more questions if want, maybe favourite food 
food = input ('...what is your favourite food, (Garri & Soup or Rice): ')

print ('wow, same as me too ' + food)

# So you can see that for every input we customized the output result plus what the user supplied.

# 06- So to close out of our Simple Feedback program, we can say:

print ('Alright Bye, See you again. ')

