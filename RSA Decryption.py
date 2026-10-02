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

cipher_input = input("\nEnter the encrypted blocks (comma-separated): ")
cipher_blocks = [int(x.strip()) for x in cipher_input.split(",")]

print("\nDecrypting each chunk")
decrypted_bytes = b""
for c in cipher_blocks:
    m = pow(c, d, n)
    block = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    decrypted_bytes += block
    print(f"for each chunk: c = {c} then decrypted is m = {m} then bytes {block}")

decrypted_msg = decrypted_bytes.decode()
print(f"\nDecrypted message: {decrypted_msg}")

