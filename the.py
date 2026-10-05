members = []
print("Gym Management System")
def add_member():

    name = st.text_input("Enter member name")
    age = st.number_input("Enter age")
    fee = st.number_input("Enter membership fee")

    if age <= 15:
        st.error("Member must be older than 15 years.")
        return None

    member = {
        "name": name,
        "age": age,
        "fee": fee,
        "status": "Active"
    }

    return member


member = add_member()

if member:
    st.write(member)