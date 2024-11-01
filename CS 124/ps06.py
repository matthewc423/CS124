num = 12403180369
exp = num + 1
pows = []
# find 2^(num - 1)

i = 1
while i < exp:
  pows.append(i)
  i *= 2

for i in range(len(pows)):
  



print(pows[len(pows) - 1])