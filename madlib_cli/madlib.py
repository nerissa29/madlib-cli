from textwrap import dedent

print(dedent("""
MadLib CLI Edition!
--------------------
Let's play a mad lib games, fill in the missing words!
Have fun!

"""))

user_response_list = []

madlib = ["adjective1", "adjective2", "adjective3", "adjective4", "adjective5",  >>> 4
          "adjective6", "First Name1", "First Name2", "First Name3", "past tense", >>> 5-9
          "plural noun1", "plural noun2", "plural noun3", "plural noun4",   >>> 10-13
          "plural noun5", "large animal", "small animal", "Girl's name", "number (1-50)",  >>> 14-18
          "number (1-50)", "number (1-50)"]
for index, item in enumerate(madlib):
    user_response_list.append(input(f"Enter {madlib[index]}: "))

print(user_response_list)

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
# with open("story.txt", "w") as f:
#     f.write(f"I the {user_response_list[0]} and {user_response_list[1]} {user_response_list[6]} "
#             f"have {user_response_list[9]} {user_response_list[7]}'s {user_response_list[2]} sister "
#             f"and plan to steal her {user_response_list[3]} {user_response_list[11]}! \n"
#             f"What are a {user_response_list[15]} and backpacking {user_response_list[16]} "
#             f"to do? Before you can help {user_response_list[17]}, you'll have to "
#             f"collect the {user_response_list[4]} {user_response_list[12]} and {user_response_list[13]} {user_response_list[14]} "
#             f"that open up the {user_response_list[18]} worlds connected to A {user_response_list[8]}'s Lair. "

#             f"There are {user_response_list[19]} {user_response_list[13]} and {user_response_list[20]} {user_response_list[14]} in the game, "
#             f"along with hundreds of other goodies for you to find.")


with open("story.txt", 'r') as  f:
    contents = f.read()

# print(contents)



