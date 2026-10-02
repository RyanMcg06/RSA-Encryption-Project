from math import gcd

print("RSA Demo using Euler's Theorem\n")

p = 79
q = 83
n = p * q
phi = (p - 1) * (q - 1)

print(f"p = {p}, q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")

e = 17
if gcd(e, phi) != 1:
    raise ValueError("e must be coprime to phi(n)")
d = pow(e, -1, phi)

print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")

msg = input("\nEnter a message to encrypt: ")
msg_bytes = msg.encode()

max_len = (n.bit_length() - 1) // 8
chunks = [msg_bytes[i:i+max_len] for i in range(0, len(msg_bytes), max_len)]

print("\nEncrypting chunks and demonstrating Euler's theorem")
cipher_blocks = []
for chunk in chunks:
    m = int.from_bytes(chunk, 'big')
    print(f"\nFor each chunk: bytes = {chunk}, integer m = {m}")
    g = gcd(m, n)
    print(f"  gcd(m, n) = {g}")
    if g == 1:
        euler_check = pow(m, phi, n)
        print(f"  Euler check: m^phi(n) mod n = {euler_check}")
        if euler_check == 1:
            print("  Euler's theorem holds")
        else:
            print("  Unexpected result")
    else:
        print("  gcd(m, n) != 1 so Euler's theorem doesn't strictly apply")
    c = pow(m, e, n)
    print(f"  Ciphertext c = {c}")
    cipher_blocks.append(c)

print("\nEncrypted blocks:")
print(cipher_blocks)
