print 'step 1'
def speak(message):
  return message

print 'step 2'

message = "happy"
message = "sad"
message = "IDK"

if message == "happy":
  response = speak("I'm happy!")
elif message == "sad":
  response = speak("I'm sad.")
else:
  response = speak("I don't know what I'm feeling.")

print response

print 'step 3'

def biggest_number(*args):
  print max(args)
  return max(args)

print 'step 4'
    
def smallest_number(*args):
  print min(args)
  return min(args)

print 'step 5'

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

print 'step 6'

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print 'step 7'