# Final Challenge Caesar cipher
words = "abcdefghijklmnopqrstuvwxyz"


def caesar(string_inp, move, direction):
    ans = ""
    if direction == "decode":
        move *= -1
    for i in range(len(string_inp)):
        if string_inp[i] in words:
            ans += words[(words.index(string_inp[i]) + move) % 25]
        else:
            ans += string_inp[i]
    return ans


# def encode(s, key):
#     ans = ""
#     for i in range(len(s)):
#         if s[i].lower() in words:
#             ans += words[(ord(s[i].lower())-ord('a')+key)%25]
#         else:
#             ans += s[i]
#     return ans
#
#
# def decode(ss, ke):
#     an = ""
#     for i in range(len(ss)):
#         if s[i].lower() in words:
#             an += words[(ord(ss[i].lower())-ord('a')-key)%25]
#         else:
#             an += ss[i]
#     return an
print("logo")
conti = "yes"
while conti == "yes":
    directio = input("encrypt or decrypt ")
    stri = input("Enter the message ").lower()
    mov = int(input("code "))
    print(f"The {directio}d message was {caesar(stri, mov, directio)}")
    conti = input("Do you want to continue ")
