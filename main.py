from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_discs = int(input("\nHow many discs do you want to play with?\n"))

while num_discs < 3:
  num_discs = int(input("\nEnter a number greater than or equal to 3\n"))
for i in range(num_discs, 0, -1):
  left_stack.push(i)
num_optimal_moves = 2**num_discs - 1
print('\nThe fastest you can solve this game is in {} moves'.format(num_optimal_moves))
#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter, name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]



        
#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_discs:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\n/Which stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disc = from_stack.pop()
      to_stack.push(disc)
      num_user_moves += 1
      break
    else:
      print("\nInvalid Move. Try Again.")
print("\n\nYou have completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves, num_optimal_moves))


