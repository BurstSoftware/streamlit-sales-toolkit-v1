import streamlit as st

# App Title
st.title("Streamlit Sales Toolkit")
st.write("Welcome to the Streamlit Sales Toolkit! This application guides you through sales steps and tailors your pitch based on client needs.")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Client Discovery", "ROI Calculator", "Sales Pitch Summary"])

# Initialize session state for each input if it doesn't already exist
if "data_analysis" not in st.session_state:
    st.session_state["data_analysis"] = "Manual"
if "reporting_hours" not in st.session_state:
    st.session_state["reporting_hours"] = 0
if "inventory_cost" not in st.session_state:
    st.session_state["inventory_cost"] = 0
if "revenue" not in st.session_state:
    st.session_state["revenue"] = 0

# Home Section
if section == "Home":
    st.header("Why Streamlit Applications?")
    st.write("""
    Streamlit applications provide high ROI by helping businesses streamline operations, enhance decision-making, and increase productivity.
    Using Streamlit, we offer:
    - **Enhanced Data-Driven Decision-Making**
    - **Automated Reporting**
    - **Customer Analytics**
    - **Inventory and Supply Chain Optimization**
    - **Predictive Analytics**
    - **Reduced IT Dependency**
    - **Real-Time Business Intelligence**
    """)

# Client Discovery Section
elif section == "Client Discovery":
    st.header("Client Discovery")
    st.write("Answer the following questions to assess the client's needs:")

    # Input fields that save directly to session state
    st.session_state["data_analysis"] = st.selectbox("How does your client handle data analysis?", ["Manual", "Automated", "Mixed"], index=["Manual", "Automated", "Mixed"].index(st.session_state["data_analysis"]))
    st.session_state["reporting_hours"] = st.number_input("Estimate hours spent on manual reporting monthly:", min_value=0, max_value=1000, value=st.session_state["reporting_hours"])
    st.session_state["inventory_cost"] = st.number_input("Annual inventory cost (if applicable):", min_value=0, value=st.session_state["inventory_cost"])
    st.session_state["revenue"] = st.number_input("Client’s annual revenue:", min_value=0, value=st.session_state["revenue"])

    # Display summary of input values
    st.write("**Client Discovery Summary:**")
    st.write(f"- Data Analysis Method: {st.session_state['data_analysis']}")
    st.write(f"- Reporting Hours: {st.session_state['reporting_hours']} hours")
    st.write(f"- Inventory Cost: ${st.session_state['inventory_cost']}")
    st.write(f"- Revenue: ${st.session_state['revenue']}")

# ROI Calculator Section
elif section == "ROI Calculator":
    st.header("ROI Calculator")
    
    # Editable fields to calculate ROI, directly accessing session state values
    revenue = st.number_input("Client's Annual Revenue:", min_value=0, value=st.session_state["revenue"], key="roi_revenue")
    reporting_hours = st.number_input("Hours Spent on Reporting Monthly:", min_value=0, max_value=1000, value=st.session_state["reporting_hours"], key="roi_reporting_hours")
    inventory_cost = st.number_input("Annual Inventory Cost:", min_value=0, value=st.session_state["inventory_cost"], key="roi_inventory_cost")

    # Calculate ROI based on user inputs
    if revenue > 0:
        roi = revenue * 0.03  # Assuming a 3% improvement in decision-making
        st.write(f"**Enhanced Decision-Making ROI:** ${roi:,.2f}")

    if reporting_hours > 0:
        reporting_savings = reporting_hours * 75 * 12 * 0.8  # Estimating an 80% time-saving with automation
        st.write(f"**Automated Reporting ROI:** ${reporting_savings:,.2f}")

    if inventory_cost > 0:
        inventory_savings = inventory_cost * 0.1  # Estimating a 10% cost reduction in inventory
        st.write(f"**Inventory Management ROI:** ${inventory_savings:,.2f}")

# Sales Pitch Summary Section
elif section == "Sales Pitch Summary":
    st.header("Sales Pitch Summary")
    st.write("Here’s a tailored pitch based on your client’s needs:")

    st.write("""
    - **Enhanced Decision-Making**: By using Streamlit apps to visualize and simulate data, your decision-makers gain real-time insights, helping increase efficiency and avoid costly mistakes.
    - **Automated Reporting**: Save time and money by automating reporting tasks, freeing your team to focus on strategic activities.
    - **Customer Analytics**: Streamlit apps offer a personalized experience for customers, increasing conversion rates and revenue.
    - **Inventory Management**: With optimized inventory management, your business can reduce costs by avoiding overstock and reducing waste.
    - **Predictive Analytics**: Forecast demand and optimize strategic plans using real-time predictive analytics.
    """)

    st.write("Contact us to learn more about how Streamlit applications can add $1.5 million or more to your annual revenue!")
