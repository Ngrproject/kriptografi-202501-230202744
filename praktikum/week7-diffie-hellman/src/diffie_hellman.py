import random

# parameter umum
p = 23
g = 5

# private key Alice dan Bob
a = random.randint(1, p-1)
b = random.randint(1, p-1)

# public key
A = pow(g, a, p)  # public Alice
B = pow(g, b, p)  # public Bob

print("Public Alice (A):", A)
print("Public Bob   (B):", B)

# ============================
#      SIMULASI MITM EVE
# ============================

# Eve memiliki private key-nya sendiri
e1 = random.randint(1, p-1)  # untuk menuju Alice
e2 = random.randint(1, p-1)  # untuk menuju Bob

# Public key Eve yang akan disisipkan
E1 = pow(g, e1, p)  # dikirim ke Alice (mengganti B)
E2 = pow(g, e2, p)  # dikirim ke Bob (mengganti A)

print("\nEve mengganti public key!")
print("Eve → Alice (E1):", E1)
print("Eve → Bob   (E2):", E2)

# Alice menghitung shared key palsu
shared_Alice = pow(E1, a, p)

# Bob menghitung shared key palsu
shared_Bob = pow(E2, b, p)

# Eve dapat menghitung kunci antara dirinya ↔ Alice dan dirinya ↔ Bob
shared_Eve_Alice = pow(A, e1, p)
shared_Eve_Bob = pow(B, e2, p)

# ============================
#        HASIL AKHIR
# ============================

print("\n=== Kunci yang dihasilkan ===")
print("Kunci Alice :", shared_Alice)
print("Kunci Bob   :", shared_Bob)

print("\n=== Kunci yang Eve tahu ===")
print("Kunci Alice–Eve :", shared_Eve_Alice)
print("Kunci Bob–Eve   :", shared_Eve_Bob)
