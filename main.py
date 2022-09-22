s = input()
s = s.replace('\r', "")
n = int(input())
h = []
for i in range(0, len(s), n):
  h.append(s[i:i+n])
for i in range(len(h)):
  if i%2==0:
    print(h[i], end="")
  else:
    print(h[i])