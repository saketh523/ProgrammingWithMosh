#GuessingGame
secret_number = 9
loop_count = 0
target_count = 3

while loop_count < target_count:
  guess_number = int(input('Guess: '))
  loop_count+=1
  if(guess_number == secret_number):
    print('Yay! You guessed it right')
    break
else:
  print("Oops, you couldn't guess the number")
