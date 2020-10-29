from math import gcd
from sympy import isprime


def main():
    print("Start of Program! We advise you to pick very large p and q numbers")

    # the user picks a valid p
    while True:
        try:
            p = int(input("Enter p: "))
            if not isprime(p):
                raise ValueError
            break
        except ValueError:
            print("Invalid Input. p is not a prime number!")

    # the user picks a valid q
    while True:
        try:
            q = int(input("Enter q: "))
            if not isprime(q):
                raise ValueError
            break
        except ValueError:
            print("Invalid Input. q is not a prime number!")

    # calculating N
    N = p * q

    # calculating V
    V = (p - 1) * (q - 1)

    # the user picks a valid Npri
    while True:
        try:
            Npri = int(input("Enter Npri: "))
            # checks that the GCD of Npri and V is equal to 1
            if gcd(Npri, V) != 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input. The GCD of Npri and V has to be equal to 1!")

    # picking the smallest Npub possible
    Npub = 0
    while (Npub * Npri) % V != 1:
        Npub += 1

    # printing the private and public key
    print(f"The private key is ({N}, {Npri})")
    print(f"The public key is ({N}, {Npub})")

    # asking the user if he wants to encrypt a message
    while True:
        try:
            flag = input("Do you want to try encrypting a message (Y/N)? ").upper()
            if flag == "YES" or flag == "Y":
                print("Cipher text: " + rsa_encrypt(input("Enter Plain Text: "), N, Npub))
            elif flag == "NO" or flag == "N":
                pass
            else:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input!")

    # asking the user if he wants to decrypt a message
    while True:
        try:
            flag = input("Do you want to try decrypting a message (Y/N)? ").upper()
            if flag == "YES" or flag == "Y":
                print("Plain Text: " + rsa_decrypt(input("Enter Cipher Text: "), N, Npri))
            elif flag == "NO" or flag == "N":
                pass
            else:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input!")

    print("Program terminated!")


# RSA encryption
def rsa_encrypt(plain_text, N, Npub):
    res = ""
    # cycles through every char in the plain text
    for m in plain_text:
        # RSA encryption formula (fills with 0s so that every encrypted char has the same len(str(N)) length)
        res += f"%0{len(str(N))}d" % ((ord(m) ** Npub) % N)
    return res


# RSA decryption
def rsa_decrypt(cipher_text, N, Npri):
    res = ""
    # cycles through the cipher text divided in arrays of len(str(N)) length
    for c in [int(cipher_text[i:i+len(str(N))]) for i in range(0, len(cipher_text), len(str(N)))]:
        # RSA decryption formula
        res += chr((c ** Npri) % N)
    return res


# starts main function if the main script is directly run
if __name__ == "__main__":
    main()
