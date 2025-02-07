import streamlit as st
import re
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import hashlib  # For password hashing (if needed for user accounts)
import uuid  # For generating unique IDs for submissions

# Simulated database interaction
def save_to_database(data):
    # In production, use a database like PostgreSQL, MySQL, or MongoDB
    # This would involve creating a connection, executing queries, etc.
    st.write("Data saved to database (simulated)")
    return True

# Email validation function
def is_valid_email(email):
    email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.match(email_regex, email) is not None

# Function to interact with CRM (simulated)
def update_crm(data):
    # In reality, this would involve API calls to CRM like Salesforce, HubSpot, etc.
    st.write("CRM updated with new lead information (simulated)")
    return True

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

# Security: Basic CSRF protection
def check_csrf_token():
    # In a real app, you'd need to handle CSRF tokens more securely
    # This is a very basic check
    if 'csrf_token' not in st.session_state:
        st.session_state['csrf_token'] = str(uuid.uuid4())
    return st.experimental_get_query_params().get('csrf_token', [None])[0] == st.session_state['csrf_token']

def main():
    st.title("Web Application Request Form")

    if not check_csrf_token():
        st.error("CSRF token mismatch. Please refresh the page.")
        return

    # User input fields
    name = st.text_input("Your Name")
    business_name = st.text_input("Business Name")
    email = st.text_input("Email Address")
    description = st.text_area("Describe the Web Application You Need", 
                               "Please provide details about the features, purpose, etc.")

    # Security: Sanitizing user inputs (very basic)
    name = name.strip()
    business_name = business_name.strip()
    email = email.strip().lower()

    # Checkbox for additional services
    need_hosting = st.checkbox("Do you need hosting services?")
    need_domain = st.checkbox("Do you need a domain name?")

    # Submit button
    if st.button("Submit Request"):
        if name and business_name and email and description:
            if is_valid_email(email):
                # Construct data for backend
                data = {
                    'id': str(uuid.uuid4()),  # Unique identifier for each submission
                    'name': hashlib.sha256(name.encode()).hexdigest(),  # Hashing for privacy
                    'business_name': business_name,
                    'email': email,
                    'description': description,
                    'need_hosting': need_hosting,
                    'need_domain': need_domain
                }

                # Save to database
                if save_to_database(data):
                    # Update CRM
                    update_crm(data)

                    # Send email confirmation
                    email_body = f'''Thank you for your submission, {name}.

                    We've received your request for a web application for {business_name}.

                    You will be contacted via {email} soon.'''
                    if send_email(email, "Web Application Request Received", email_body):
                        st.success("Your request has been submitted and an email confirmation has been sent!")
                    else:
                        st.warning("Your request has been saved and CRM updated, but there was an issue sending the confirmation email.")
                else:
                    st.error("Failed to save your request. Please try again.")
            else:
                st.error("Please provide a valid email address.")
        else:
            st.error("Please fill out all fields before submitting.")

if __name__ == "__main__":
    main()
