import streamlit as st
st.title("Primitive Root")

q_text = st.text_input("Prime number:")
g_text = st.text_input("Primitive root:")

if st.button("Submit"):
    try:
        q = int(q_text)
        g = int(g_text)

        def prime(q):
            if q > 1:
                for i in range(2, int(q / 2) + 1):
                    if (q % i) == 0:
                        return False
                else:
                    return True
            else:
                return False

        def primitive_check(g, q):
            primitive_roots = []
            for i in range(1, q):
                temp = set()
                output = ''
                for x in range(1, q):
                    result = pow(i, x, q)
                    output += f"{i}^{x} mod {q} = {result}"
                    if x < q - 1:
                        output += ", "
                    temp.add(result)
                    if result == 1:
                        break
                if len(temp) == q - 1:
                    primitive_roots.append(i)
                    output += f" ==> {i} is primitive root of {q}, "
                st.write(output)
            if g in primitive_roots:
                return True, primitive_roots
            else:
                return False, primitive_roots

        if prime(q):
            st.write("")
            st.subheader("Output:")
            st.write("")
            
            is_primitive_root = primitive_check(g, q)
            if is_primitive_root[0]:
                st.write(f"{g} is primitive root: {is_primitive_root[0]} {is_primitive_root[1]}")
            else:
                st.write(f"{g} is NOT primitive root of {q} - List of Primitive roots: {is_primitive_root[1]}")
        else:
            st.write(f"{q} is not a prime number!!")
        st.snow() 

    except ValueError:
        st.write("Invalid! Please Enter a Valid Integer Number For Prime Number.")