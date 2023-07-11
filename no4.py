def kata_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return True
    else:
        return False

kata = input("Masukkan kata : ")

if kata_palindrome(kata):
    print("Kata","'",kata,"'", "merupakan palindrome")
else:
    print("Kata","'",kata,"'", "bukan merupakan palindrome")
