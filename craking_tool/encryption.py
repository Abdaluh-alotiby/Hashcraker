import hashlib as HL

Input =str(input("ENTER TH PASSWORD: "))
Hashed = HL.md5(f"{Input}".encode("utf-8")).hexdigest()
print("\nThe Hashed is: "+Hashed)