import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Load the model
model = joblib.load('fraud_detection.pkl')

# Page configuration
st.set_page_config(
    page_title="Enterprise Fraud Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main Container */
        .main {
            background-color: #f8fafc;
        }
        
        /* Dashboard Header */
        .dashboard-header {
            background: white;
            padding: 1.5rem 2rem;
            border-bottom: 1px solid #e2e8f0;
            margin: -6rem -4rem 2rem -4rem;
        }
        
        .company-header {
            color: #1a365d;
            font-size: 0.875rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        .dashboard-title {
            color: #1a202c;
            font-size: 1.875rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }
        
        /* Cards */
        .stat-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .card-metric {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2d3748;
        }
        
        .card-label {
            font-size: 0.875rem;
            color: #718096;
            margin-top: 0.5rem;
        }
        
        /* Form Elements */
        .stSelectbox {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
        }
        
        .stSlider {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        
        /* Custom Button */
        .custom-button {
            background: #3182ce;
            padding: 0.75rem 1.5rem;
            color: white;
            border-radius: 6px;
            font-weight: 500;
            border: none;
            transition: all 0.2s;
        }
        
        .custom-button:hover {
            background: #2c5282;
        }
        
        /* Results Section */
        .results-container {
            padding: 2rem;
            border-radius: 8px;
            margin-top: 2rem;
        }
        
        /* Tooltips */
        .tooltip {
            position: relative;
            display: inline-block;
            border-bottom: 1px dotted #718096;
            cursor: help;
        }
        
        /* Analytics Section */
        .analytics-container {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            border: 1px solid #e2e8f0;
            margin-top: 2rem;
        }
        
        /* Status Indicators */
        .status-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 0.5rem;
        }
        
        .status-active {
            background-color: #48bb78;
        }
        
        .status-warning {
            background-color: #ecc94b;
        }
        
        .status-critical {
            background-color: #f56565;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for system status and metrics
with st.sidebar:
    st.markdown("### System Status")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card"><span class="status-indicator status-active"></span>Model Status: Active</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><span class="status-indicator status-active"></span>API Status: Online</div>', unsafe_allow_html=True)
    
    st.markdown("### System Metrics")
    st.markdown(""" 
        <div class="stat-card">
            <div class="card-metric">99.98%</div>
            <div class="card-label">Model Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(""" 
        <div class="stat-card">
            <div class="card-metric">45ms</div>
            <div class="card-label">Average Response Time</div>
        </div>
    """, unsafe_allow_html=True)

# Main dashboard header
st.markdown("""
    <div class="dashboard-header">
        <div class="company-header">Enterprise Security Suite</div>
        <h1 class="dashboard-title">Fraud Detection Dashboard</h1>
    </div>
""", unsafe_allow_html=True)

# Transaction Section
st.markdown("## Transaction Details")
amount = st.number_input("Transaction Amount ($)", value=100.0, step=10.0)
transaction_type = st.selectbox("Transaction Type", ["Online Purchase", "ATM Withdrawal", "Wire Transfer"])

# Add explanations for fields
st.markdown("### Need help?")
st.info("**Transaction Amount:** The dollar amount of the transaction.\n\n"
        "**Transaction Type:** The method used to complete the transaction.")



# Main content area with tabs
tab1, tab2 = st.tabs(["Transaction Analysis", "Analytics Dashboard"])

with tab1:
    # Create three columns for better layout
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("### Transaction Details")
        amount = st.number_input(
            "Transaction Amount ($)",
            min_value=0.0,
            max_value=1000000.0,
            value=1000.0,
            step=100.0,
            format="%.2f"
        )
        
        transaction_type = st.selectbox(
            "Transaction Type",
            ["Online Purchase", "In-Store Purchase", "ATM Withdrawal", "Wire Transfer"]
        )

    with col2:
        st.markdown("### Card Information")
        card_type = st.selectbox(
            "Card Type",
            ["Corporate Card", "Premium Credit", "Standard Credit", "Debit Card"]
        )
        
        merchant_category = st.selectbox(
            "Merchant Category",
            ["Retail", "Travel", "Entertainment", "Services", "Other"]
        )

    with col3:
        st.markdown("### Location Data")
        country = st.selectbox(
            "Transaction Country",
            ["United States", "United Kingdom", "Canada", "Australia", "Other"]
        )
        
        is_international = st.checkbox("International Transaction")

    # Advanced Features Section
    st.markdown("### Advanced Analysis Features")
    col4, col5 = st.columns([1, 1])
    
    with col4:
        transaction_velocity = st.slider(
            "Transaction Velocity (24h)",
            min_value=0,
            max_value=100,
            value=25,
            help="Number of transactions made by the user in the last 24 hours"
        )
        
        device_risk_score = st.slider(
            "Device Risk Score",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            help="Risk score calculated based on the device used."
        )

    with col5:
        historical_fraud_rate = st.slider(
            "Historical Fraud Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=1.5,
            help="Percentage of fraudulent transactions in the past"
        )
        
        customer_risk_level = st.select_slider(
            "Customer Risk Level",
            options=["Low", "Medium", "High"],
            value="Medium"
        )

    # Analysis Button
    if st.button("Run Fraud Analysis", type="primary"):
        with st.spinner('Processing transaction...'):
            # Simulate processing time
            import time
            time.sleep(1)
            
            # Mock risk score calculation (replace with actual model prediction)
            risk_score = np.random.random()
            
            # Display results in a professional format
            st.markdown("### Analysis Results")
            col6, col7, col8 = st.columns(3)
            
            with col6:
                st.markdown(f"""
                    <div class="stat-card">
                        <div class="card-metric">{risk_score:.2%}</div>
                        <div class="card-label">Risk Score</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col7:
                recommendation = "Approve" if risk_score < 0.7 else "Review" if risk_score < 0.9 else "Decline"
                color = "#48bb78" if recommendation == "Approve" else "#ecc94b" if recommendation == "Review" else "#f56565"
                st.markdown(f"""
                    <div class="stat-card">
                        <div class="card-metric" style="color: {color}">{recommendation}</div>
                        <div class="card-label">Recommendation</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col8:
                confidence = np.random.uniform(85, 99)
                st.markdown(f"""
                    <div class="stat-card">
                        <div class="card-metric">{confidence:.1f}%</div>
                        <div class="card-label">Confidence Level</div>
                    </div>
                """, unsafe_allow_html=True)

with tab2:
    # Analytics Dashboard
    st.markdown("### Fraud Detection Analytics")
    # Create sample data for visualization
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    fraud_rates = np.random.uniform(0.5, 2.5, size=len(dates))

    # Plot fraud rates over time
    fig = px.line(
        x=dates,
        y=fraud_rates,
        title='Fraud Rate Trend (Last 30 Days)',
        labels={'x': 'Date', 'y': 'Fraud Rate (%)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=40, r=40, b=40, l=40),
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Key metrics
    col9, col10, col11 = st.columns(3)
    
    with col9:
        st.markdown("""
            <div class="stat-card">
                <div class="card-metric">$123,456</div>
                <div class="card-label">Prevented Fraud (MTD)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col10:
        st.markdown("""
            <div class="stat-card">
                <div class="card-metric">1.2%</div>
                <div class="card-label">False Positive Rate</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col11:
        st.markdown("""
            <div class="stat-card">
                <div class="card-metric">99.3%</div>
                <div class="card-label">Detection Rate</div>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #718096; font-size: 0.875rem;">
        Enterprise Fraud Detection System v2.0 • Last Updated: December 2024
    </div>
""", unsafe_allow_html=True)
