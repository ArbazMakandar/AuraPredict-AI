# AuraPredict AI - Next-Gen Student Performance Intelligence

## 🌌 Project Overview
AuraPredict is a premium, high-end machine learning dashboard designed to predict student academic performance with precision. Built for the future of education, it combines advanced analytics with a stunning futuristic UI.

## 🚀 Features
- **Quantum Prediction Engine**: Uses a pre-trained Random Forest Regressor to forecast academic outcomes.
- **Glassmorphism UI**: A sleek, translucent interface with backdrop-filter effects and premium dark mode.
- **Advanced Analytics**: Interactive Plotly charts including performance distribution, correlation scatter plots, and subject proficiency radar charts.
- **Real-time Feedback**: Dynamic prediction cards with status badges (Elite, Optimal, Critical) and AI-driven recommendations.
- **Responsive Layout**: Professional grid system optimized for high-resolution displays.

## 📊 Model & Data
- **Model**: `student_model.pkl` (Random Forest Regressor)
- **Dataset**: `Student_Performance.csv`
- **Predictors**: Study Hours, Attendance %, Math/Science/English Scores.
- **Target**: Overall Performance Score (%).

## 💎 Project Showcase
The interface is engineered with a **Glassmorphism** design language, featuring:
- **Neural Radar Maps**: Dynamic subject proficiency visualization.
- **Quantum Badging**: Pulsing status indicators for performance tiers.
- **Glass-Card Inputs**: Ultra-modern sliders and numerical inputs with backdrop-filter effects.

## 🛠 Tech Stack
- **Engine**: Python 3.x
- **UI Framework**: Streamlit
- **Visuals**: Plotly, Custom CSS (Glassmorphism)
- **Data Science**: Pandas, NumPy, Scikit-learn
- **Typography**: Outfit & Inter (Google Fonts)

## 🏁 Getting Started
1. **Prerequisite**: Ensure you have [Git LFS](https://git-lfs.github.com/) installed.
2. Clone the repository and fetch large files:
   ```bash
   git clone https://github.com/ArbazMakandar/AuraPredict-AI.git
   cd AuraPredict-AI
   git lfs pull
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---
*Powered by AuraPredict Engine • © 2026 EduFuture Labs*