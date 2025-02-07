import streamlit as st
import re
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Simulated database function (replace with real database in production)
def save_to_database(data):
    # This would be where you save data to a database
    st.write("Data saved to database (simulated)")
    return True

# Email validation function
def is_valid_email(email):
    email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.match(email_regex, email) is not None

def send_email(to_email, subject, body):
    message = Mail(
        from_email='your_email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=body)
    try:
        sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')
        response = sg.send(message)
        st.success('Email sent')
        return True
    except Exception as e:
        st.error(f'Error sending email: {e}')
        return False

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
        if name and business_name and email and description:
            if is_valid_email(email):
                # Simulate saving to database
                if save_to_database({
                    'name': name,
                    'business_name': business_name,
                    'email': email,
                    'description': description,
                    'need_hosting': need_hosting,
                    'need_domain': need_domain
                }):
                    # Send email confirmation
                    email_body = f'''Thank you for your submission, {name}.

                    We've received your request for a web application for {business_name}.

                    You will be contacted via {email} soon.'''
                    if send_email(email, "Web Application Request Received", email_body):
                        st.success("Your request has been submitted and an email confirmation has been sent!")
                    else:
                        st.warning("Your request has been saved, but there was an issue sending the confirmation email.")
                else:
                    st.error("Failed to save your request. Please try again.")
            else:
                st.error("Please provide a valid email address.")
        else:
            st.error("Please fill out all fields before submitting.")

if __name__ == "__main__":
    main()
