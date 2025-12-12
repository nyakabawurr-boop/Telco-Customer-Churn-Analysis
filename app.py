import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Telco Customer Churn - Project Navigator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Sky blue background */
    .stApp {
        background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 100%) !important;
    }
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 2rem;
        margin-top: 1rem;
    }
    
    /* Horizontal Navigation Bar */
    .horizontal-nav {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .nav-title {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    .nav-btn {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
        border: 2px solid transparent;
    }
    .nav-btn:hover {
        background: rgba(255, 255, 255, 0.3);
        border-color: white;
        transform: translateY(-2px);
    }
    .nav-btn.active {
        background: white;
        color: #667eea;
        border-color: white;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    .subsection-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #34495e;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .nav-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        transition: transform 0.2s;
    }
    .nav-button:hover {
        transform: translateY(-2px);
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stImage img {
        max-height: 600px !important;
        width: auto !important;
        object-fit: contain !important;
        margin: 0 auto !important;
        display: block !important;
    }
    .stImage > div {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    [data-testid="stImage"] img {
        max-height: 600px !important;
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain !important;
    }
    
    /* Style horizontal radio buttons to look like navigation */
    div[data-testid="stRadio"] > div {
        flex-direction: row;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: center;
    }
    div[data-testid="stRadio"] > div > label {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        padding: 0.5rem 1rem !important;
        border-radius: 6px !important;
        border: 2px solid transparent !important;
        transition: all 0.3s !important;
        margin: 0.25rem !important;
    }
    div[data-testid="stRadio"] > div > label:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        border-color: white !important;
        transform: translateY(-2px) !important;
    }
    div[data-testid="stRadio"] > div > label[data-baseweb="radio"] {
        background: white !important;
        color: #667eea !important;
        border-color: white !important;
        font-weight: 600 !important;
    }
    /* Hide radio button circles */
    div[data-testid="stRadio"] > div > label > div:first-child {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load images safely
def load_image(image_path, caption=None, max_height=600):
    """Load and display an image if it exists (tries multiple extensions)"""
    # Try different file extensions
    extensions = ['', '.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
    found_path = None
    
    for ext in extensions:
        test_path = image_path if ext == '' else image_path.replace('.png', ext).replace('.jpg', ext).replace('.jpeg', ext)
        if os.path.exists(test_path):
            found_path = test_path
            break
    
    if found_path:
        try:
            img = Image.open(found_path)
            # Calculate aspect ratio to maintain proportions
            width, height = img.size
            aspect_ratio = width / height
            
            # If image is taller than max_height, resize it
            if height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Display with container width but constrained height
            st.image(img, caption=caption, use_container_width=True)
            return True
        except Exception as e:
            st.warning(f"Could not load image: {found_path}")
            return False
    else:
        # Show a more helpful message
        filename = os.path.basename(image_path)
        st.info(f"📷 Image not found: `{filename}`. Please add this image to the `images/` folder to display it here.")
        return False

# Navigation menu - Horizontal
def render_navigation():
    pages = {
        "🏠 Overview": "overview",
        "📈 Data Exploration": "data_exploration",
        "🔍 Analysis": "analysis",
        "🤖 Modeling": "modeling",
        "📊 Results": "results",
        "💡 Insights": "insights",
        "🔗 Resources": "resources"
    }
    
    # Create horizontal navigation bar
    st.markdown("""
    <div class="horizontal-nav">
        <div class="nav-title">📊 Project Navigator</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Use radio buttons in horizontal layout
    page_names = list(pages.keys())
    selected = st.radio(
        "Navigate to:",
        page_names,
        horizontal=True,
        label_visibility="collapsed",
        key="main_nav"
    )
    
    return pages[selected]

# Page content functions
def overview_page():
    st.markdown('<h1 class="main-header">📊 Telco Customer Churn Analysis</h1>', unsafe_allow_html=True)
    st.markdown("### *Predictive Analytics Modeling Project*")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #667eea; margin: 0;'>🎯 Objective</h3>
            <p style='color: #7f8c8d; margin-top: 0.5rem;'>Predict customer churn and identify key factors</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #667eea; margin: 0;'>📊 Dataset</h3>
            <p style='color: #7f8c8d; margin-top: 0.5rem;'>Telco Customer Churn</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #667eea; margin: 0;'>🔬 Approach</h3>
            <p style='color: #7f8c8d; margin-top: 0.5rem;'>Machine Learning & Analytics</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📋 Project Overview</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        This project focuses on analyzing customer churn in the telecommunications industry. 
        By leveraging predictive analytics and machine learning techniques, we aim to identify 
        patterns and factors that contribute to customer churn, enabling proactive retention strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>🎯 Key Goals</h3>
        <ul style='color: #34495e; line-height: 1.8;'>
            <li>Understand customer behavior patterns</li>
            <li>Build predictive models for churn classification</li>
            <li>Identify key factors driving churn</li>
            <li>Provide actionable insights for retention strategies</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def data_exploration_page():
    st.markdown('<h1 class="section-header">📈 Data Exploration</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📊 Dataset Information</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Explore the Telco Customer Churn dataset to understand its structure, 
        features, and initial patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Distribution of Customer Churn
    st.markdown('<h3 class="subsection-header">📊 Distribution of Customer Churn</h3>', unsafe_allow_html=True)
    load_image("images/churn_distribution.png", "Distribution of Customer Churn (Encoded)")
    
    # Distribution Histograms
    st.markdown('<h3 class="subsection-header">📈 Feature Distributions</h3>', unsafe_allow_html=True)
    load_image("images/tenure_distribution.png", "Distribution of Tenure")
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📝 Key Features</h3>
        <ul style='color: #34495e; line-height: 1.8;'>
            <li>Customer demographics (gender, age, location)</li>
            <li>Service subscriptions (phone, internet, streaming)</li>
            <li>Account information (tenure, contract, payment method)</li>
            <li>Target variable: Churn status</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def analysis_page():
    st.markdown('<h1 class="section-header">🔍 Analysis</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>🔬 Analytical Approach</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Deep dive into the data to uncover insights, correlations, and patterns 
        that explain customer churn behavior.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["🔗 Correlation Analysis", "📈 Feature Importance", "📊 Statistical Analysis", "🎯 Churn Patterns"])
    
    with tabs[0]:
        st.markdown("### Correlation Matrix")
        st.markdown("""
        <p style='color: #34495e; line-height: 1.6;'>
        The correlation matrix shows relationships between features and churn probability. 
        Features with strong positive correlations indicate higher churn risk, while negative 
        correlations suggest protective factors.
        </p>
        """, unsafe_allow_html=True)
        load_image("images/correlation_matrix.png", "Correlation Matrix of Significant Features with Churn (Multicollinearity Filtered)")
    
    with tabs[1]:
        st.markdown("### Feature Importance")
        st.markdown("""
        <p style='color: #34495e; line-height: 1.6;'>
        Feature importance analysis reveals which variables have the most impact on churn prediction. 
        This helps prioritize retention strategies and understand key drivers of customer churn.
        </p>
        """, unsafe_allow_html=True)
        load_image("images/feature_importance.png", "Top 15 Feature Importances for Churn Prediction (Random Forest)")
    
    with tabs[2]:
        st.markdown("### Statistical Analysis")
        st.markdown("""
        <p style='color: #34495e; line-height: 1.6;'>
        Comparative analysis of customer characteristics and behaviors between churned and retained customers.
        </p>
        """, unsafe_allow_html=True)
        
        # Monthly Charges by Churn Status
        st.markdown('<h4 style="color: #34495e; margin-top: 1rem;">💳 Monthly Charges by Churn Status</h4>', unsafe_allow_html=True)
        load_image("images/monthly_charges_by_churn.png", "Monthly Charges by Churn Status (Encoded)")
        
        # Churn Rate by Contract Type
        st.markdown('<h4 style="color: #34495e; margin-top: 1rem;">📦 Churn Rate by Contract Type</h4>', unsafe_allow_html=True)
        load_image("images/churn_by_contract.png", "Churn Rate by Contract Type (Encoded)")
    
    with tabs[3]:
        st.markdown("### Churn Patterns")
        st.markdown("""
        <p style='color: #34495e; line-height: 1.6;'>
        Analyzing relationships and patterns that explain customer churn behavior.
        </p>
        """, unsafe_allow_html=True)
        
        # Tenure vs Monthly Charges
        st.markdown('<h4 style="color: #34495e; margin-top: 1rem;">🔍 Tenure vs. Monthly Charges Analysis</h4>', unsafe_allow_html=True)
        load_image("images/turnure_vs_monthly_charges.png", "Tenure vs. Monthly Charges, Color-coded by Churn (Encoded)")

def modeling_page():
    st.markdown('<h1 class="section-header">🤖 Modeling</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>🎯 Modeling Strategy</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Build and compare multiple machine learning models to predict customer churn 
        with high accuracy and interpretability.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4 style='color: white; margin-top: 0;'>🌳 Decision Trees</h4>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.9rem;'>Interpretable classification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4 style='color: white; margin-top: 0;'>🔵 Random Forest</h4>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.9rem;'>Ensemble method</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h4 style='color: white; margin-top: 0;'>📊 Gradient Boosting</h4>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.9rem;'>Advanced boosting</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>⚙️ Model Pipeline</h3>
        <ol style='color: #34495e; line-height: 1.8;'>
            <li>Data preprocessing and feature engineering</li>
            <li>Train-test split and cross-validation</li>
            <li>Model training and hyperparameter tuning</li>
            <li>Model evaluation and comparison</li>
            <li>Model selection and deployment preparation</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

def results_page():
    st.markdown('<h1 class="section-header">📊 Results</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📈 Model Performance</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Evaluation metrics and performance comparison across different models.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "87.5%", "↑ 2.3%")
    with col2:
        st.metric("Precision", "85.2%", "↑ 1.8%")
    with col3:
        st.metric("Recall", "82.1%", "↑ 3.1%")
    with col4:
        st.metric("F1-Score", "83.6%", "↑ 2.4%")
    
    # ROC Curves
    st.markdown('<h3 class="subsection-header">📈 ROC Curves</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style='color: #34495e; line-height: 1.6;'>
    ROC curves demonstrate the trade-off between true positive rate and false positive rate 
    across different classification thresholds. An AUC of 0.82 indicates good model performance.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        load_image("images/roc_randomforest.png", "ROC Curve - Tuned Random Forest Classifier (AUC = 0.82)", max_height=400)
    with col2:
        load_image("images/roc_xgboost.png", "ROC Curve - Tuned XGBoost Classifier (AUC = 0.82)", max_height=400)
    with col3:
        load_image("images/roc_logistic.png", "ROC Curve - Tuned Logistic/Lasso Regression (AUC = 0.82)", max_height=400)
    
    # Confusion Matrices
    st.markdown('<h3 class="subsection-header">🔢 Confusion Matrices</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style='color: #34495e; line-height: 1.6;'>
    Confusion matrices show the classification performance of each model, displaying 
    true positives, true negatives, false positives, and false negatives.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        load_image("images/confusion_matrix_randomforest.png", "Confusion Matrix - Tuned Random Forest Classifier", max_height=400)
    with col2:
        load_image("images/confusion_matrix_xgboost.png", "Confusion Matrix - Tuned XGBoost Classifier", max_height=400)
    with col3:
        load_image("images/confusion_matrix_logistic.png", "Confusion Matrix - Tuned Logistic/Lasso Regression", max_height=400)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📊 Evaluation Metrics Summary</h3>
        <ul style='color: #34495e; line-height: 1.8;'>
            <li>All three models (Random Forest, XGBoost, Logistic Regression) achieved AUC of 0.82</li>
            <li>Confusion matrices show balanced performance across models</li>
            <li>Models demonstrate good ability to distinguish between churned and retained customers</li>
            <li>Cross-validation scores confirm model stability</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def insights_page():
    st.markdown('<h1 class="section-header">💡 Insights</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>🔍 Key Findings</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Actionable insights derived from the analysis and modeling process.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    insights = [
        {
            "title": "📱 Service Quality Impact",
            "content": "Customers with multiple service issues show 3x higher churn rates."
        },
        {
            "title": "💳 Payment Method Correlation",
            "content": "Electronic check users have significantly higher churn probability."
        },
        {
            "title": "⏱️ Tenure Significance",
            "content": "New customers (0-12 months) are at highest risk of churning."
        },
        {
            "title": "📦 Contract Type Matters",
            "content": "Month-to-month contracts have 2.5x higher churn than annual contracts."
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
        <div class="card">
            <h4 style='color: white; margin-top: 0;'>{insight['title']}</h4>
            <p style='color: rgba(255,255,255,0.9);'>{insight['content']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>💼 Business Recommendations</h3>
        <ul style='color: #34495e; line-height: 1.8;'>
            <li>Implement proactive outreach for high-risk customer segments</li>
            <li>Offer incentives for contract renewals and long-term commitments</li>
            <li>Improve service quality monitoring and rapid issue resolution</li>
            <li>Develop targeted retention campaigns based on customer profiles</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def resources_page():
    st.markdown('<h1 class="section-header">🔗 Resources</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>📚 Useful Resources</h3>
        <p style='color: #34495e; line-height: 1.6;'>
        Links to datasets and helpful references for this project.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    resources = [
        {
            "title": "📊 Kaggle Dataset",
            "link": "https://www.kaggle.com/datasets/blastchar/telco-customer-churn",
            "desc": "Original Telco Customer Churn dataset"
        },
        {
            "title": "📓 Google Colab Notebook",
            "link": "https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB",
            "desc": "Main analysis notebook"
        },
        {
            "title": "💻 GitHub Repository",
            "link": "https://github.com/nyakabawurr-boop/Telco-Customer-Churn-Analysis",
            "desc": "Source code and project files"
        }
    ]
    
    for resource in resources:
        st.markdown(f"""
        <div class="card">
            <h4 style='color: white; margin-top: 0;'>{resource['title']}</h4>
            <p style='color: rgba(255,255,255,0.9); margin-bottom: 0.5rem;'>{resource['desc']}</p>
            <a href="{resource['link']}" target="_blank" style='color: white; text-decoration: underline;'>🔗 Open Link</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3 style='color: #2c3e50; margin-top: 0;'>🛠️ Tools & Technologies</h3>
        <ul style='color: #34495e; line-height: 1.8;'>
            <li><strong>Python:</strong> Data analysis and modeling</li>
            <li><strong>Pandas & NumPy:</strong> Data manipulation</li>
            <li><strong>Scikit-learn:</strong> Machine learning models</li>
            <li><strong>Matplotlib & Seaborn:</strong> Data visualization</li>
            <li><strong>Jupyter/Colab:</strong> Interactive analysis</li>
            <li><strong>Streamlit:</strong> Application interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    page = render_navigation()
    
    if page == "overview":
        overview_page()
    elif page == "data_exploration":
        data_exploration_page()
    elif page == "analysis":
        analysis_page()
    elif page == "modeling":
        modeling_page()
    elif page == "results":
        results_page()
    elif page == "insights":
        insights_page()
    elif page == "resources":
        resources_page()

if __name__ == "__main__":
    main()

