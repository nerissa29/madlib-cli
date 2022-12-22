from textwrap import dedent

print(dedent("""
MadLib CLI Edition!
--------------------
Let's play a mad lib games, fill in the missing words!
Have fun!

"""))

user_response_list = []


adjective1 = input("Enter Adjective: ")
user_response_list.append(adjective1)

adjective2= input("Enter another adjective: ")
user_response_list.append(adjective2)

first_name1 = input("Enter First Name: ")
user_response_list.append(first_name1)

past_tense = input("Enter Past Tense Verb: ")
user_response_list.append(past_tense)

first_name2 = input("Enter another First Name: ")
user_response_list.append(first_name2)

adjective3 = input("Enter another Adjective: ")
user_response_list.append(adjective3)

adjective4 = input("Enter another Adjective: ")
user_response_list.append(adjective4)

plural = input("Enter Plural Noun: ")
user_response_list.append(plural)

plural = input("Enter Large Animal: ")

plural = input("Enter Small Animal: ")

plural = input("Enter a Girl's Name: ")

adjective5 = input("Enter another Adjective: ")

plural2 = input("Enter Plural Noun: ")

adjective5 = input("Enter another Adjective: ")

plural2 = input("Enter Plural Noun: ")

plural2 = input("Enter a number (1-50): ")

plural2 = input("Enter First Name: ")

plural2 = input("Enter a number: ")

plural2 = input("Enter Plural Noun: ")

plural2 = input("Enter a number: ")

plural2 = input("Enter Plural Noun: ")




"""
I the {Adjective} and {Adjective} {A First Name} have 
{Past Tense Verb} {A First Name}'s {Adjective} sister 
and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} 
to do? Before you can help {A Girl's Name}, you'll have to 
collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} 
that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. 
There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, 
along with hundreds of other goodies for you to find.

"""
# read in the story.txt file
with open("story.txt", "w") as f:
    f.write(f"I the {user_response_list[0]} and {user_response_list[1]} {user_response_list[2]} "
            f"have {user_response_list[3]} {user_response_list[4]}'s {user_response_list[5]} sister "
            f"and plan to steal her {user_response_list[6]} {user_response_list[7]}! \n"
            f"What are a {Large Animal} and backpacking {Small Animal} ")


print(user_response_list)



