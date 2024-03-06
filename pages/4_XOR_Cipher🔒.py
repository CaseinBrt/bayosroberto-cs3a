import streamlit as st 

st.header("XOR Cipher")
plaintext = bytes(st.text_area("Plain text:").encode())

key = bytes(st.text_input("Key:").encode())

if st.button("Submit"):

    def xor_encrypt(plaintext, key):
        """Encrypts plaintext using XOR cipher with the given key, st.writeing bits involved."""

        ciphertext = bytearray()
    
        for i in range(len(plaintext)):
            plaintext_byte = plaintext[i]
            key_byte = key[i % len(key)]
            xor_result = plaintext_byte ^ key_byte
            ciphertext.append(xor_result)
        
            st.write(f"Plaintext byte: {format(plaintext_byte, '08b')} = {chr(plaintext_byte)}")
            st.write(f"Key byte:       {format(key_byte, '08b')} = {chr(key_byte)}")
            st.write(f"XOR result:     {format(xor_result, '08b')} = {chr(xor_result)}")
            st.write("-"*20)

        return ciphertext

    def xor_decrypt(ciphertext, key):
        """Decrypts ciphertext using XOR cipher with the given key."""
        return xor_encrypt(ciphertext, key)  # XOR decryption is the same as encryption

    if plaintext.decode() == key.decode():
        st.write("Plaintext should not be equal to the key")
    elif not plaintext or not key: 
        st.write("Invalid Key!")
    elif len(plaintext.decode()) < len(key.decode()):
        st.write("Plaintext length should be equal or greater than the length of key")
    else:
        encrypted_text = xor_encrypt(plaintext, key)
        st.write(f"Ciphertext:", encrypted_text.decode())

        decrypted_text = xor_encrypt(encrypted_text, key)
        st.write(f"Decrypted:", decrypted_text.decode())
    st.balloons()