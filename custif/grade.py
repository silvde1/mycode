#!/usr/bin/env python3
message = 'Your grade is a '
print('What is your numeric score?')
score = float(input())
if score >= 90:
    message = message + 'A.'
elif score >= 80:
    message = message + 'B.'
elif score >= 70:
    message = message + 'C.'
elif score >= 60:
    message = message + 'D.'
elif score >= 0:
    message = message + 'F.'
else:
    message = message + 'Did you even take the test?'
print(message)