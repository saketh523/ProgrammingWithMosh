#CarGame

input_value = ""
started = False
stopped = False
while input_value.lower() != 'quit':
  input_value = input("> ")
  if input_value.lower() == 'help':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit')
  elif input_value.lower() == 'start':
    if started:
      print('Car already started')
    else:
      started = True
      print('Car started... Ready to go!')
  elif input_value.lower() == 'stop':
    if stopped:
      print('Car already stopped')
    else:
      stopped = True
      print('Car stopped')
  elif input_value.lower() == 'quit':
    break  
  else:
    print("I don't understand")