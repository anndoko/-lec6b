# prompt the user for input
user_question = input("Please enter your question:")

# check if quesion mark is included:
user_q_lst = list(user_question)
if user_q_lst[-1] != "?":
    user_question += "?" # if not, add "?" to the string
