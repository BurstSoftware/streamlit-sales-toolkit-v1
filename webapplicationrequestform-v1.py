import streamlit as st

def main():
    st.title("Web Application Request Form")

    # User input fields
    name = st.text_input("Your Name")
    business_name = st.text_input("Business Name")
    email = st.text_input("Email Address")
    description = st.text_area("Describe the Web Application You Need", 
                               "Please provide details about the features, purpose, etc.")

    # Checkbox for additional services
    need_hosting = st.checkbox("Do you need hosting services?")
    need_domain = st.checkbox("Do you need a domain name?")

    # Submit button
    if st.button("Submit Request"):
        # This is a placeholder for where you'd handle the data, 
        # e.g., saving to a database or sending via email
        st.success("Your request has been submitted!")
        st.write(f"Name: {name}")
        st.write(f"Business Name: {business_name}")
        st.write(f"Email: {email}")
        st.write(f"Description: {description}")
        st.write(f"Hosting Needed: {'Yes' if need_hosting else 'No'}")
        st.write(f"Domain Name Needed: {'Yes' if need_domain else 'No'}")

if __name__ == "__main__":
    main()
