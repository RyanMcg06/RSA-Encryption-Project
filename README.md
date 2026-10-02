# RSA Encryption from Scratch

A small Python implementation of RSA encryption and decryption, built to explore the number theory behind it, mainly Euler's theorem and modular inverses.

## How it works
- Two primes p and q give the modulus n = p × q and Euler's totient φ(n) = (p − 1)(q − 1).
- The public exponent e is chosen coprime to φ(n), and the private key d is its inverse mod φ(n).
- Each block of the message is encrypted as c = m^e mod n and decrypted as m = c^d mod n.
- The encryption script also checks Euler's theorem (m^φ(n) ≡ 1 mod n) for each block.

## How to run
Requires Python 3.8 or later. No external libraries.

    python RSA encryption.py
    python RSA decryption.py

## Example
Encrypting "hello world" produces a list of ciphertext blocks, which the decryption script turns back into "hello world".

## Limitations
This is an educational project. It uses small fixed primes, so it is not secure and should not be used for real encryption.

## Next steps
- Generate large random primes using the Miller–Rabin test
- Implement my own modular exponentiation and extended Euclidean algorithm
- Support larger key sizes and block-based encryption
