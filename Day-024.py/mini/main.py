with open("Input/Names/names.txt") as name:
  names = name.readlines()

with open("Input/Letters/letter.txt") as letter:
  letter_content = letter.read()
  for name in names:
    new_file = letter_content.replace("[name]", name.strip())
    with open(f"Output/ReadyToSend/l_{name.strip()}.txt", mode="w") as ready:
      ready.write(new_file)



