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
    st.session_state["revenue"] = st.number_input("Client's annual revenue:", min_value=0, value=st.session_state["revenue"])

    # Display summary of input values
    st.write("**Client Discovery Summary:**")
    st.write(f"- Data Analysis Method: {st.session_state['data_analysis']}")
    st.write(f"- Reporting Hours: {st.session_state['reporting_hours']} hours")
    st.write(f"- Inventory Cost: ${st.session_state['inventory_cost']:,.2f}")
    st.write(f"- Revenue: ${st.session_state['revenue']:,.2f}")

# ROI Calculator Section
elif section == "ROI Calculator":
    st.header("ROI Calculator")
    st.write("Based on your client discovery data, here's the projected ROI breakdown:")

    # Constants for calculations
    HOURLY_RATE = 75  # Average hourly rate for employees
    AUTOMATION_EFFICIENCY = 0.8  # 80% time savings with automation
    INVENTORY_OPTIMIZATION = 0.1  # 10% inventory cost reduction
    DECISION_MAKING_IMPROVEMENT = 0.03  # 3% revenue improvement
    ERROR_REDUCTION = 0.02  # 2% error reduction in manual processes
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Values")
        # Display current values and allow for adjustments
        revenue = st.number_input("Annual Revenue ($):", 
                                min_value=0, 
                                value=st.session_state["revenue"],
                                format="%d")
        
        reporting_hours = st.number_input("Monthly Reporting Hours:",
                                        min_value=0,
                                        max_value=1000,
                                        value=st.session_state["reporting_hours"])
        
        inventory_cost = st.number_input("Annual Inventory Cost ($):",
                                       min_value=0,
                                       value=st.session_state["inventory_cost"],
                                       format="%d")
        
        data_analysis_method = st.selectbox("Current Data Analysis Method:",
                                          ["Manual", "Automated", "Mixed"],
                                          index=["Manual", "Automated", "Mixed"].index(st.session_state["data_analysis"]))

    with col2:
        st.subheader("Savings Breakdown")
        
        # 1. Time Savings from Automated Reporting
        annual_reporting_cost = reporting_hours * HOURLY_RATE * 12
        reporting_savings = annual_reporting_cost * AUTOMATION_EFFICIENCY
        st.write("**1. Reporting Automation Savings**")
        st.write(f"- Annual Hours Saved: {reporting_hours * 12 * AUTOMATION_EFFICIENCY:,.0f} hours")
        st.write(f"- Cost Savings: ${reporting_savings:,.2f}")
        
        # 2. Inventory Optimization (if applicable)
        if inventory_cost > 0:
            inventory_savings = inventory_cost * INVENTORY_OPTIMIZATION
            st.write("**2. Inventory Optimization Savings**")
            st.write(f"- Cost Reduction: ${inventory_savings:,.2f}")
        else:
            inventory_savings = 0
        
        # 3. Enhanced Decision Making Impact
        decision_making_benefit = revenue * DECISION_MAKING_IMPROVEMENT
        st.write("**3. Enhanced Decision Making Impact**")
        st.write(f"- Revenue Improvement: ${decision_making_benefit:,.2f}")
        
        # 4. Error Reduction Savings (based on revenue)
        error_reduction_savings = revenue * ERROR_REDUCTION
        st.write("**4. Error Reduction Savings**")
        st.write(f"- Cost Avoidance: ${error_reduction_savings:,.2f}")

    # Total ROI Calculation
    st.markdown("---")
    st.subheader("Total ROI Summary")
    
    # Calculate implementation costs (example values)
    implementation_cost = 50000  # Base implementation cost
    annual_subscription = 12000  # Annual subscription cost
    first_year_cost = implementation_cost + annual_subscription
    
    # Calculate total benefits
    total_annual_benefits = (
        reporting_savings +
        inventory_savings +
        decision_making_benefit +
        error_reduction_savings
    )
    
    # ROI Metrics with error handling
    if total_annual_benefits > 0:
        roi_percentage = ((total_annual_benefits - first_year_cost) / first_year_cost) * 100
        payback_months = (first_year_cost / total_annual_benefits) * 12
    else:
        roi_percentage = 0
        payback_months = float('inf')  # Represents infinite payback period
    
    # Display ROI metrics in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Annual Benefits", f"${total_annual_benefits:,.2f}")
    with col2:
        st.metric("First Year ROI", f"{roi_percentage:.1f}%")
    with col3:
        if payback_months == float('inf'):
            st.metric("Payback Period", "N/A")
        else:
            st.metric("Payback Period", f"{payback_months:.1f} months")
    
    # Additional ROI Details
    st.markdown("---")
    st.subheader("Implementation Details")
    
    # Show implementation details with appropriate messaging
    if total_annual_benefits > 0:
        st.write(f"""
        - One-time Implementation Cost: ${implementation_cost:,.2f}
        - Annual Subscription Cost: ${annual_subscription:,.2f}
        - First Year Total Cost: ${first_year_cost:,.2f}
        - Net First Year Benefit: ${(total_annual_benefits - first_year_cost):,.2f}
        """)
    else:
        st.warning("Please enter values in the Client Discovery section or above to calculate ROI metrics.")

# Sales Pitch Summary Section
elif section == "Sales Pitch Summary":
    st.header("Sales Pitch Summary")
    st.write("Here's a tailored pitch based on your client's needs:")

    st.write("""
    - **Enhanced Decision-Making**: By using Streamlit apps to visualize and simulate data, your decision-makers gain real-time insights, helping increase efficiency and avoid costly mistakes.
    - **Automated Reporting**: Save time and money by automating reporting tasks, freeing your team to focus on strategic activities.
    - **Customer Analytics**: Streamlit apps offer a personalized experience for customers, increasing conversion rates and revenue.
    - **Inventory Management**: With optimized inventory management, your business can reduce costs by avoiding overstock and reducing waste.
    - **Predictive Analytics**: Forecast demand and optimize strategic plans using real-time predictive analytics.
    """)

    st.write("Contact us to learn more about how Streamlit applications can add $1.5 million or more to your annual revenue!")
