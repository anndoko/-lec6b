# prompt the user for input
user_question = input("Please enter your question:")

# check if quesion mark is included:
user_q_lst = list(user_question)
if user_q_lst[-1] != "?":
    user_question += "?" # if not, add "?" to the string

# create the list of standard Magic 8 Ball answers
magic_ans = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
]

# pick a random answer for the user's question
from random import randrange
random_index = randrange(len(magic_ans)) # get a random index
random_ans = magic_ans[random_index]
print(random_ans)
