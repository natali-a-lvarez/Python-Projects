# x = 10
# while x > 0:
#     print("the value is " + str(x))
#     x -= 1

# x = 1
# while x < 10:
#     print('this is the second value: ' + str(x))
#     x += 1

input = "Four score and seven years ago"
for c in range(len(input)):
  if c in ['a', 'e', 'i', 'o', 'u']:
    print(c)