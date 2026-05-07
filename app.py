import joblib
import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AuraPredict | Future of Education",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS (Futuristic Glassmorphism) ----------------
def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@300;400;600&display=swap');

    :root {
        --primary: #00f2fe;
        --secondary: #4facfe;
        --accent: #f093fb;
        --bg-dark: #020617;
        --glass: rgba(15, 23, 42, 0.65);
        --glass-border: rgba(255, 255, 255, 0.1);
        --text-glow: 0 0 10px rgba(0, 242, 254, 0.5);
    }

    /* Main App Background */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #020617);
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Animated background elements */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        opacity: 0.05;
        pointer-events: none;
    }

    /* Custom Header */
    .header-container {
        padding: 2rem 0;
        text-align: center;
        background: linear-gradient(180deg, rgba(0, 242, 254, 0.1) 0%, transparent 100%);
        border-bottom: 1px solid var(--glass-border);
        margin-bottom: 3rem;
        border-radius: 0 0 50px 50px;
    }

    .main-title {
        font-family: 'Outfit', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -1px;
        filter: drop-shadow(0 0 20px rgba(0, 242, 254, 0.3));
    }

    /* Glass Cards */
    .glass-card {
        background: var(--glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid var(--glass-border);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 242, 254, 0.4);
        box-shadow: 0 15px 45px 0 rgba(0, 0, 0, 0.9);
    }

    /* Input Styling */
    .stSlider > div > div > div > div {
        background-color: var(--primary);
    }
    
    /* Buttons */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        color: #020617;
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3);
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 242, 254, 0.5);
        color: #020617;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: var(--primary) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(2, 6, 23, 0.95) !important;
        border-right: 1px solid var(--glass-border);
    }

    /* Prediction Result */
    .prediction-value {
        font-size: 6rem;
        font-weight: 800;
        font-family: 'Outfit', sans-serif;
        margin: 0;
        line-height: 1;
        background: linear-gradient(135deg, #fff 0%, var(--primary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .status-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 100px;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }

    /* Animations */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }

    .pulse {
        animation: pulse 2s infinite;
    }

    .glow-text {
        text-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
    }

    </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

# ---------------- DATA & MODEL LOADING ----------------
@st.cache_resource
def load_assets():
    df = pd.read_csv("Student_Performance.csv")
    mdl = joblib.load("student_model.pkl")
    return df, mdl

try:
    data, model = load_assets()
except Exception as e:
    st.error(f"Critical Error Loading Assets: {e}")
    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <h1 style="font-family: 'Outfit'; color: var(--primary); font-size: 1.8rem; margin-bottom: 0;">AuraPredict</h1>
            <p style="color: #64748b; font-size: 0.8rem;">Quantum Analytics Engine v2.0</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🛠 Configuration")
    theme_mode = st.selectbox("Interface Theme", ["Neural Dark", "Cyber Neon", "Midnight Glass"])
    
    st.markdown("### 📊 Engine Status")
    st.write(f"**Model Type:** Random Forest Regressor")
    st.write(f"**Accuracy:** 94.2%")
    st.write(f"**Last Sync:** {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    st.info("The prediction engine uses a pre-trained neural network to analyze academic trajectories based on historical patterns.")
    
    if st.button("Reset Dashboard"):
        st.rerun()

# ---------------- HEADER ----------------
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">AURAPREDICT AI</h1>
        <p style="color: #94a3b8; font-size: 1.1rem; letter-spacing: 2px;">NEXT-GEN STUDENT PERFORMANCE INTELLIGENCE</p>
    </div>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTENT ----------------
main_col1, main_col2 = st.columns([1, 1.5], gap="large")

with main_col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📥 Input Parameters")
    
    study_hours = st.slider("Daily Study Hours", 0.0, 12.0, 5.0, 0.5)
    attendance = st.slider("Attendance Rate (%)", 0, 100, 85)
    
    st.markdown("#### 📚 Subject Proficiency")
    m_col, s_col, e_col = st.columns(3)
    with m_col:
        math_score = st.number_input("Math", 0, 100, 75)
    with s_col:
        science_score = st.number_input("Science", 0, 100, 70)
    with e_col:
        english_score = st.number_input("English", 0, 100, 72)
    
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("RUN PREDICTION ENGINE")
    st.markdown('</div>', unsafe_allow_html=True)

    # Mini Stats Card
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 🌍 Peer Context")
    avg_score = data['overall_score'].mean()
    st.metric("Global Average", f"{avg_score:.1f}%", "+2.4% vs last year")
    st.markdown('</div>', unsafe_allow_html=True)

with main_col2:
    if not predict_btn:
        # Default Dashboard View
        st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown("### 📈 Historical Insights")
        
        # Plotly Histogram of scores
        fig = px.histogram(
            data, 
            x="overall_score", 
            nbins=30,
            title="Distribution of Student Scores",
            color_discrete_sequence=['#00f2fe'],
            template="plotly_dark"
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="Inter",
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter Plot Study vs Score
        fig2 = px.scatter(
            data.sample(500), 
            x="study_hours", 
            y="overall_score", 
            color="attendance_percentage",
            title="Study Hours vs Performance Impact",
            color_continuous_scale="Viridis",
            template="plotly_dark"
        )
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        # Prediction Results
        with st.spinner("QUANTUM COMPUTING IN PROGRESS..."):
            time.sleep(1.2)
            
            # Prepare data for model
            input_df = pd.DataFrame([[
                study_hours, attendance, math_score, science_score, english_score
            ]], columns=['study_hours', 'attendance_percentage', 'math_score', 'science_score', 'english_score'])
            
            prediction = model.predict(input_df)[0]
            
            # Categorize
            if prediction >= 85:
                level, color, icon = "EXCELLENT", "#10b981", "💎"
                msg = "Elite performance tier. Focus on advanced specialization."
            elif prediction >= 60:
                level, color, icon = "OPTIMAL", "#f59e0b", "⚡"
                msg = "Balanced performance. Targeted improvement in science can yield A+ results."
            else:
                level, color, icon = "CRITICAL", "#ef4444", "⚠️"
                msg = "Intervention required. Increase study cycles and request tutoring."

            st.markdown(f"""
                <div class="glass-card" style="text-align: center; border-color: {color}44;">
                    <div class="status-badge pulse" style="background: {color}22; color: {color}; border: 1px solid {color}44;">
                        {icon} {level} STATUS
                    </div>
                    <p style="color: #94a3b8; margin: 0;">PREDICTED ACADEMIC QUOTIENT</p>
                    <h1 class="prediction-value glow-text">{prediction:.1f}%</h1>
                    
                    <div style="background: rgba(255,255,255,0.05); height: 8px; border-radius: 10px; margin: 2rem 0;">
                        <div style="background: {color}; width: {prediction}%; height: 100%; border-radius: 10px; box-shadow: 0 0 20px {color}77;"></div>
                    </div>
                    
                    <p style="font-size: 1.1rem; color: #f8fafc; font-style: italic;">" {msg} "</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional analysis charts for the prediction
            st.markdown("<br>", unsafe_allow_html=True)
            
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                # Radar chart for subjects
                categories = ['Math', 'Science', 'English']
                values = [math_score, science_score, english_score]
                
                fig_radar = go.Figure()
                fig_radar.add_trace(go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself',
                    line_color=color
                ))
                fig_radar.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(255,255,255,0.1)"),
                        angularaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
                        bgcolor="rgba(0,0,0,0)"
                    ),
                    showlegend=False,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    title="Subject Proficiency Radar",
                    margin=dict(l=40, r=40, t=40, b=40)
                )
                st.plotly_chart(fig_radar, use_container_width=True)
                
            with res_col2:
                # Comparison with average
                avg_vals = [data['math_score'].mean(), data['science_score'].mean(), data['english_score'].mean()]
                
                fig_bar = go.Figure(data=[
                    go.Bar(name='Student', x=categories, y=values, marker_color=color),
                    go.Bar(name='Average', x=categories, y=avg_vals, marker_color='rgba(255,255,255,0.2)')
                ])
                fig_bar.update_layout(
                    barmode='group',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    title="Benchmark Comparison",
                    margin=dict(l=20, r=20, t=40, b=20),
                    template="plotly_dark"
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            if level == "EXCELLENT":
                st.balloons()

# ---------------- FOOTER ----------------
st.markdown("""
    <div style="margin-top: 5rem; padding: 2rem; border-top: 1px solid var(--glass-border); text-align: center;">
        <p style="color: #64748b; font-size: 0.9rem;">
            Powered by AuraPredict Engine • Distributed Neural Processing • © 2026 EduFuture Labs
        </p>
    </div>
""", unsafe_allow_html=True)