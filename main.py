import streamlit as st
from encrypt import encrypt
from decrypt import decrypt

st.set_page_config(
    page_title="S-DES João Saraiva",
    page_icon="🔐",
)

st.write("# S-DES João Saraiva! :closed_lock_with_key:")

st.sidebar.success("Veja o código no [GitHub](https://github.com/saraiva142/Lista-5-Criptografia).")

st.markdown(
    """
    - Esse projeto é uma implementação do algoritmo S-DES, que é um algoritmo de cifra de bloco de 8 bits. 
    - O S-DES é uma versão simplificada do DES (Data Encryption Standard) e é usado principalmente para fins educacionais.
    - O S-DES utiliza uma chave de 10 bits e realiza 2 rodadas de permutações e substituições para cifrar e decifrar os dados. O algoritmo é composto por várias etapas, incluindo permutações iniciais, expansões, substituições e permutações finais.
"""
)

with st.form(key="form"):
    st.subheader("Insira os dados para cifrar ou decifrar:")
    plaintext = st.text_input("Texto plano (8 bits):", "10101010")
    key = st.text_input("Chave (10 bits):", "1010001010")
    action = st.selectbox("Escolha a ação:", ["Cifrar", "Decifrar"])

    submit = st.form_submit_button("Executar")
    if submit:
        if action == "Cifrar":
            encrypted_text = encrypt(plaintext, key)  
            st.success(f"Texto cifrado: {encrypted_text}")
        else:
            decrypted_text = decrypt(plaintext, key)  
            st.success(f"Texto decifrado: {decrypted_text}")


