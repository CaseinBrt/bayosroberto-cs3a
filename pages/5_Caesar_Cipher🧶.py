import streamlit as st

st.header("Caesar Cipher")

text = st.text_area("Text:")
shift_keys_input = st.text_input("Shift Keys:")

if shift_keys_input:
    shift_keys = list(map(int, shift_keys_input.split()))
else:
    shift_keys = []

if st.button("Submit"):
    if not text or not shift_keys:
        st.write("Text and Shift should not be empty!")
    else:
        st.write("")
        st.subheader("Your Output:")
        st.write("")

        def encrypt_decrypt(text, shift_keys, ifdecrypt):
            """
            Encrypts a text using Caesar Cipher with a list of shift keys.
            Args:
                text: The text to encrypt.
                shift_keys: A list of integers representing the shift values for each character.
                ifdecrypt: flag if decrypt or encrypt
            Returns:
                A string containing the encrypted text if encrypt and plain text if decrypt
            """

            result = ""

            if len(shift_keys) <= 1 or len(shift_keys) > len(text):
                raise ValueError("Invalid shift keys length") 

            for i, char in enumerate(text):
                shift_key = shift_keys[i % len(shift_keys)]

                if 32 <= ord(char) <= 125:
                    if ifdecrypt:
                        asc = ord(char) - shift_key
                    else:
                        asc = ord(char) + shift_key

                    new_ascii = ord(char) + shift_key if not ifdecrypt else ord(char) - shift_key

                    while new_ascii > 125:
                        new_ascii -= 94
                    while new_ascii < 32:
                        new_ascii += 94

                    result += chr(new_ascii)
                else: 
                    result += char
                st.write(i, char, shift_key, result[i])
            return result

        # Example usage
        enc = encrypt_decrypt(text, shift_keys, False)
        st.write("----------")
        dec = encrypt_decrypt(enc, shift_keys, True)
        st.write("----------")

        # Results of the Output
        st.write("Text:", text)
        st.write("Shift keys:", *shift_keys)
        st.write("Cipher:", enc)
        st.write("Decrypted text:", dec)
