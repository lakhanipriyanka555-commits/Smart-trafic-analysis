# 🚦 Smart Traffic Analytics System

A professional AI-powered Smart Traffic Analytics dashboard built with **Streamlit**, **Pandas**, **Plotly**, and **OpenCV**.

---

## 🌟 Features

- **📊 Dashboard Overview** — KPI cards, 24-hour traffic trend, road status summary
- **📈 Traffic Analytics** — Interactive line, bar, pie, scatter, heatmap charts
- **📹 Live Monitoring** — Upload traffic video, detect vehicles with OpenCV MOG2
- **🧠 Smart Insights** — AI-style traffic recommendations and 24h prediction graph
- **🏙️ Smart City Features** — Emergency alerts, signal optimization, pollution index, accident risk, 48h forecast

## 🎨 Design

- Premium **light-theme** UI (Apple + Notion inspired)
- Glassmorphism cards with soft shadows
- Pastel gradient accents (indigo, violet, mint, sky)
- Smooth hover animations

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/lakhanipriyanka555-commits/Smart-trafic-analysis.git
cd Smart-trafic-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m streamlit run app.py
```

Open **https://smart-trafic-analysis-gf5eucytj9vmyg5utbehbn.streamlit.app/** in your browser.

---

## 📁 Project Structure

```
Smart-trafic-analysis/
│
├── app.py              # Main Streamlit application (Pages 1–3)
├── pages_45.py         # Smart Insights & Smart City pages
├── styles.py           # Premium light-theme CSS
├── data_gen.py         # Traffic dataset generator & loader
├── generate_data.py    # Standalone data generation script
├── requirements.txt    # Python dependencies
└── traffic_data.csv    # Auto-generated sample dataset
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Streamlit | Web framework & UI |
| Pandas | Data analysis |
| Plotly | Interactive charts |
| OpenCV | Vehicle detection |
| NumPy | Numerical processing |

---

## 📊 Dataset Columns

| Column | Description |
|--------|-------------|
| Time | Timestamp |
| Vehicle_Count | Number of vehicles |
| Traffic_Density | 0.0–1.0 density ratio |
| Congestion_Level | Low / Moderate / High / Critical |
| Road_Name | Road identifier |
| Avg_Speed_kmh | Average vehicle speed |
| Pollution_Index | Estimated AQI proxy |

---

## 👩‍💻 Author

**Priyanka Lakhani** — Smart City AI Analytics Project
