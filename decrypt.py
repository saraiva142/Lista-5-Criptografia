import streamlit as st

# Tabelas do S-DES (repetidas para decrypt também)
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]
IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

# S-boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Funções auxiliares (mesma bosta que às do encrypt)

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    return ''.join('0' if b1 == b2 else '1' for b1, b2 in zip(bits1, bits2))

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    value = sbox[row][col]
    return format(value, '02b')

def generate_keys(key):
    key_p10 = permute(key, P10)
    left = key_p10[:5]
    right = key_p10[5:]
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    k1 = permute(left + right, P8)
    left = left_shift(left, 2)
    right = left_shift(right, 2)
    k2 = permute(left + right, P8)
    return k1, k2

def fk(bits, subkey):
    left = bits[:4]
    right = bits[4:]
    right_expanded = permute(right, EP)
    xor_result = xor(right_expanded, subkey)
    left_part = xor_result[:4]
    right_part = xor_result[4:]
    s0_output = sbox_lookup(left_part, S0)
    s1_output = sbox_lookup(right_part, S1)
    sbox_output = s0_output + s1_output
    p4_output = permute(sbox_output, P4)
    result = xor(left, p4_output)
    return result + right

#Decrypt

def decrypt(ciphertext: str, key: str) -> str:
    if len(ciphertext) != 8 or len(key) != 10:
        st.error("Texto cifrado deve ter 8 bits e a chave deve ter 10 bits!")
        return ""

    st.info("Iniciando a decifragem do S-DES...")

    # 1. Gerar subchaves
    k1, k2 = generate_keys(key)

    # 2. Permutação inicial IP
    ip_bits = permute(ciphertext, IP)

    # 3. Primeira função Fk com K2 (troca a ordem das chaves!)
    first_fk = fk(ip_bits, k2)

    # 4. Switch SW
    switched = first_fk[4:] + first_fk[:4]

    # 5. Segunda função Fk com K1
    second_fk = fk(switched, k1)

    # 6. Permutação final IP⁻¹
    plaintext = permute(second_fk, IP_INV)

    return plaintext
