elif section == "ROI Calculator":
    st.header("ROI Calculator")
    st.write("Adjust the ROI parameters based on your client's specific situation:")

    # First display the values from Client Discovery
    st.subheader("Client Information (from Discovery)")
    st.info(f"""
    - Current Data Analysis: {st.session_state['data_analysis']}
    - Monthly Reporting Hours: {st.session_state['reporting_hours']}
    - Annual Inventory Cost: ${st.session_state['inventory_cost']:,.2f}
    - Annual Revenue: ${st.session_state['revenue']:,.2f}
    """)

    # Create columns for ROI-specific parameters
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cost Parameters")
        implementation_cost = st.number_input(
            "Implementation Cost ($):",
            min_value=0,
            value=50000,
            help="One-time cost to implement the solution"
        )
        annual_subscription = st.number_input(
            "Annual Subscription ($):",
            min_value=0,
            value=12000,
            help="Yearly subscription cost for the solution"
        )
        hourly_rate = st.number_input(
            "Average Employee Hourly Rate ($):",
            min_value=0,
            value=75,
            help="Average hourly cost of employees doing manual work"
        )

    with col2:
        st.subheader("Efficiency Parameters")
        automation_efficiency = st.slider(
            "Automation Efficiency",
            min_value=0.0,
            max_value=1.0,
            value=0.8,
            format="%d%%",
            help="Percentage of time saved through automation"
        )
        inventory_optimization = st.slider(
            "Inventory Optimization",
            min_value=0.0,
            max_value=0.3,
            value=0.1,
            format="%d%%",
            help="Expected inventory cost reduction"
        )
        decision_improvement = st.slider(
            "Revenue Improvement",
            min_value=0.0,
            max_value=0.1,
            value=0.03,
            format="%d%%",
            help="Expected revenue improvement from better decision making"
        )
        error_reduction = st.slider(
            "Error Reduction",
            min_value=0.0,
            max_value=0.1,
            value=0.02,
            format="%d%%",
            help="Expected cost savings from reduced errors"
        )

    # Calculate savings using session_state values and new parameters
    st.markdown("---")
    st.subheader("Savings Breakdown")
    
    # 1. Time Savings from Automated Reporting
    annual_reporting_cost = st.session_state["reporting_hours"] * hourly_rate * 12
    reporting_savings = annual_reporting_cost * automation_efficiency
    st.write("**1. Reporting Automation Savings**")
    st.write(f"- Annual Hours Saved: {st.session_state['reporting_hours'] * 12 * automation_efficiency:,.0f} hours")
    st.write(f"- Cost Savings: ${reporting_savings:,.2f}")
    
    # 2. Inventory Optimization (if applicable)
    if st.session_state["inventory_cost"] > 0:
        inventory_savings = st.session_state["inventory_cost"] * inventory_optimization
        st.write("**2. Inventory Optimization Savings**")
        st.write(f"- Cost Reduction: ${inventory_savings:,.2f}")
    else:
        inventory_savings = 0
    
    # 3. Enhanced Decision Making Impact
    decision_making_benefit = st.session_state["revenue"] * decision_improvement
    st.write("**3. Enhanced Decision Making Impact**")
    st.write(f"- Revenue Improvement: ${decision_making_benefit:,.2f}")
    
    # 4. Error Reduction Savings
    error_reduction_savings = st.session_state["revenue"] * error_reduction
    st.write("**4. Error Reduction Savings**")
    st.write(f"- Cost Avoidance: ${error_reduction_savings:,.2f}")

    # ROI Summary
    st.markdown("---")
    st.subheader("Total ROI Summary")
    
    first_year_cost = implementation_cost + annual_subscription
    total_annual_benefits = (
        reporting_savings +
        inventory_savings +
        decision_making_benefit +
        error_reduction_savings
    )
    
    # ROI Metrics
    roi_percentage = ((total_annual_benefits - first_year_cost) / first_year_cost) * 100 if first_year_cost > 0 else 0
    payback_months = (first_year_cost / total_annual_benefits) * 12 if total_annual_benefits > 0 else float('inf')
    
    # Display metrics in columns
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric("Total Annual Benefits", f"${total_annual_benefits:,.2f}")
    with metric_col2:
        st.metric("First Year ROI", f"{roi_percentage:.1f}%")
    with metric_col3:
        if payback_months == float('inf'):
            st.metric("Payback Period", "N/A")
        else:
            st.metric("Payback Period", f"{payback_months:.1f} months")
