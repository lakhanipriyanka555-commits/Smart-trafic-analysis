def get_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* ══════════════════════════════════════════
   GLOBAL RESET & BASE
══════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: #1e293b;
    background: #f8fafc;
}

.stApp {
    background: linear-gradient(160deg, #f0f4ff 0%, #fafbff 40%, #f5f0ff 100%);
    min-height: 100vh;
}

/* ══════════════════════════════════════════
   SIDEBAR
══════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f8f9ff 100%) !important;
    border-right: 1px solid rgba(148,163,184,0.15) !important;
    box-shadow: 4px 0 24px rgba(99,102,241,0.06) !important;
}

[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

[data-testid="stSidebar"] .stRadio > div {
    gap: 4px;
    display: flex;
    flex-direction: column;
}
[data-testid="stSidebar"] .stRadio label {
    color: #64748b !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 10px 14px !important;
    border-radius: 10px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    color: #6366f1 !important;
    background: linear-gradient(135deg, #eef2ff, #f5f3ff) !important;
}
[data-testid="stSidebar"] .stRadio [aria-checked="true"] + label,
[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
    color: #6366f1 !important;
    background: linear-gradient(135deg, #eef2ff, #f5f3ff) !important;
    font-weight: 600 !important;
}

/* ══════════════════════════════════════════
   TOP NAVBAR
══════════════════════════════════════════ */
.top-navbar {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(226,232,240,0.8);
    border-radius: 0 0 20px 20px;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px rgba(99,102,241,0.06);
    animation: slideDown 0.4s ease;
}
.navbar-brand {
    font-size: 20px;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}
.navbar-right { display: flex; align-items: center; gap: 16px; }
.navbar-pill {
    background: linear-gradient(135deg, #f0f4ff, #f5f3ff);
    border: 1px solid rgba(99,102,241,0.15);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: #6366f1;
    font-weight: 600;
}
.navbar-weather {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    border: 1px solid rgba(16,185,129,0.2);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: #059669;
    font-weight: 600;
}
.navbar-time {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
    border: 1px solid rgba(249,115,22,0.2);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: #ea580c;
    font-weight: 600;
}

/* ══════════════════════════════════════════
   SECTION HEADERS
══════════════════════════════════════════ */
.section-header {
    font-size: 18px;
    font-weight: 700;
    color: #1e293b;
    letter-spacing: -0.3px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(99,102,241,0.2), transparent);
    margin-left: 12px;
}
.page-title {
    font-size: 26px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.8px;
    margin-bottom: 4px;
}
.page-subtitle {
    font-size: 14px;
    color: #94a3b8;
    margin-bottom: 24px;
    font-weight: 400;
}

/* ══════════════════════════════════════════
   KPI CARDS
══════════════════════════════════════════ */
.kpi-card {
    background: #ffffff;
    border: 1px solid rgba(226,232,240,0.8);
    border-radius: 20px;
    padding: 22px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 16px rgba(99,102,241,0.06);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    animation: fadeInUp 0.5s ease both;
}
.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 32px rgba(99,102,241,0.14);
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--card-accent, linear-gradient(90deg,#6366f1,#8b5cf6));
    border-radius: 20px 20px 0 0;
}
.kpi-card.green::before  { background: linear-gradient(90deg,#10b981,#34d399); }
.kpi-card.blue::before   { background: linear-gradient(90deg,#0ea5e9,#38bdf8); }
.kpi-card.orange::before { background: linear-gradient(90deg,#f59e0b,#fbbf24); }
.kpi-card.red::before    { background: linear-gradient(90deg,#ef4444,#f87171); }

.kpi-icon-wrap {
    width: 44px; height: 44px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    margin-bottom: 14px;
}
.kpi-icon-purple { background: linear-gradient(135deg,#eef2ff,#ede9fe); }
.kpi-icon-green  { background: linear-gradient(135deg,#ecfdf5,#d1fae5); }
.kpi-icon-blue   { background: linear-gradient(135deg,#eff6ff,#dbeafe); }
.kpi-icon-orange { background: linear-gradient(135deg,#fff7ed,#ffedd5); }
.kpi-icon-red    { background: linear-gradient(135deg,#fef2f2,#fee2e2); }

.kpi-value {
    font-size: 28px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 4px;
}
.kpi-label {
    font-size: 12px;
    color: #94a3b8;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 10px;
}
.kpi-trend-up   { font-size: 12px; color: #10b981; font-weight: 600; }
.kpi-trend-down { font-size: 12px; color: #ef4444; font-weight: 600; }
.kpi-trend-neu  { font-size: 12px; color: #64748b; font-weight: 600; }

/* ══════════════════════════════════════════
   GLASS PANEL / CHART CARDS
══════════════════════════════════════════ */
.glass-card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(226,232,240,0.7);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04), 0 8px 32px rgba(99,102,241,0.06);
    margin-bottom: 20px;
    transition: box-shadow 0.2s ease;
}
.glass-card:hover { box-shadow: 0 8px 40px rgba(99,102,241,0.12); }

.glass-panel {
    background: rgba(255,255,255,0.7);
    border: 1px solid rgba(226,232,240,0.6);
    border-radius: 16px;
    padding: 18px 20px;
    backdrop-filter: blur(12px);
    margin-bottom: 14px;
}

/* ══════════════════════════════════════════
   STATUS BADGES
══════════════════════════════════════════ */
.badge-smooth   { background:#ecfdf5; color:#059669; border:1.5px solid #6ee7b7; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:700; letter-spacing:0.4px; }
.badge-moderate { background:#fffbeb; color:#d97706; border:1.5px solid #fcd34d; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:700; letter-spacing:0.4px; }
.badge-heavy    { background:#fef2f2; color:#dc2626; border:1.5px solid #fca5a5; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:700; letter-spacing:0.4px; }
.badge-critical { background:#faf5ff; color:#7c3aed; border:1.5px solid #c4b5fd; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:700; letter-spacing:0.4px; }
.badge-live     { background:linear-gradient(135deg,#ef4444,#f87171); color:#fff; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:700; animation: pulseLive 1.5s infinite; letter-spacing:0.5px; }

/* ══════════════════════════════════════════
   INSIGHT CARDS
══════════════════════════════════════════ */
.insight-card {
    background: linear-gradient(135deg, #f8faff 0%, #faf5ff 100%);
    border: 1px solid rgba(99,102,241,0.12);
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 12px;
    border-left: 4px solid;
    transition: transform 0.2s ease;
}
.insight-card:hover { transform: translateX(4px); }
.insight-card.purple { border-left-color: #8b5cf6; }
.insight-card.blue   { border-left-color: #0ea5e9; }
.insight-card.green  { border-left-color: #10b981; }
.insight-card.orange { border-left-color: #f59e0b; }
.insight-card h4 { color: #1e293b; margin: 0 0 6px 0; font-size: 14px; font-weight: 700; }
.insight-card p  { color: #64748b; margin: 0; font-size: 13px; line-height: 1.6; }

/* ══════════════════════════════════════════
   ALERT / NOTIFICATION CARDS
══════════════════════════════════════════ */
.alert-card {
    background: #fff;
    border: 1px solid rgba(226,232,240,0.8);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: box-shadow 0.2s ease;
}
.alert-card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.alert-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    margin-top: 4px;
    flex-shrink: 0;
}

/* ══════════════════════════════════════════
   SMART CITY FEATURE CARDS
══════════════════════════════════════════ */
.feature-card {
    background: #fff;
    border: 1px solid rgba(226,232,240,0.8);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    text-align: center;
}
.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(99,102,241,0.12);
}
.feature-icon {
    font-size: 28px;
    margin-bottom: 10px;
    display: block;
}
.feature-title { font-size: 13px; font-weight: 700; color: #1e293b; margin-bottom: 6px; }
.feature-value { font-size: 20px; font-weight: 800; color: #6366f1; letter-spacing: -0.5px; }
.feature-sub   { font-size: 11px; color: #94a3b8; font-weight: 500; }

/* ══════════════════════════════════════════
   ROAD STATUS ROWS
══════════════════════════════════════════ */
.road-row {
    background: #fff;
    border: 1px solid rgba(226,232,240,0.7);
    border-radius: 12px;
    padding: 12px 16px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: background 0.2s;
}
.road-row:hover { background: #f8faff; }
.road-name { font-size: 13px; font-weight: 600; color: #334155; }

/* ══════════════════════════════════════════
   SIDEBAR BRAND
══════════════════════════════════════════ */
.sidebar-brand {
    padding: 20px 16px 16px;
    border-bottom: 1px solid rgba(226,232,240,0.6);
    margin-bottom: 12px;
}
.sidebar-logo {
    font-size: 22px;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}
.sidebar-tagline { font-size: 11px; color: #94a3b8; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 2px; }

/* ══════════════════════════════════════════
   FILTERS SECTION IN SIDEBAR
══════════════════════════════════════════ */
.filter-label {
    font-size: 10px;
    font-weight: 700;
    color: #cbd5e1;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin: 16px 0 8px;
}

/* ══════════════════════════════════════════
   STREAMLIT COMPONENT OVERRIDES
══════════════════════════════════════════ */
/* Tabs */
[data-testid="stTabs"] [role="tab"] {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #64748b !important;
    border-radius: 10px 10px 0 0 !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: #6366f1 !important;
    border-bottom: 2px solid #6366f1 !important;
}

/* Select / Multiselect */
[data-testid="stSelectbox"] > div > div,
[data-testid="stMultiSelect"] > div > div {
    background: #fff !important;
    border-color: rgba(148,163,184,0.3) !important;
    border-radius: 12px !important;
    color: #334155 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
}

/* Slider */
[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
}

/* Progress bars */
.stProgress > div > div { background: linear-gradient(90deg,#6366f1,#8b5cf6) !important; border-radius: 6px !important; }
.stProgress > div { background: #e2e8f0 !important; border-radius: 6px !important; }

/* Metric */
[data-testid="stMetric"] {
    background: #fff;
    border-radius: 14px;
    padding: 14px;
    border: 1px solid rgba(226,232,240,0.8);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
[data-testid="stMetricLabel"] { color: #94a3b8 !important; font-size: 12px !important; font-weight: 500 !important; }
[data-testid="stMetricValue"] { color: #0f172a !important; font-weight: 800 !important; letter-spacing: -0.5px !important; }

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 22px !important;
    box-shadow: 0 4px 16px rgba(99,102,241,0.3) !important;
    transition: all 0.25s ease !important;
}
.stDownloadButton > button:hover {
    box-shadow: 0 8px 28px rgba(99,102,241,0.45) !important;
    transform: translateY(-2px) !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #f8faff !important;
    border: 2px dashed rgba(99,102,241,0.3) !important;
    border-radius: 16px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(99,102,241,0.25) !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(99,102,241,0.4) !important;
}

/* Info / Success boxes */
[data-testid="stInfo"]    { background: #eff6ff; border-left-color: #3b82f6; border-radius: 12px; }
[data-testid="stSuccess"] { background: #ecfdf5; border-left-color: #10b981; border-radius: 12px; }
[data-testid="stWarning"] { background: #fffbeb; border-left-color: #f59e0b; border-radius: 12px; }
[data-testid="stError"]   { background: #fef2f2; border-left-color: #ef4444; border-radius: 12px; }

/* Hide Streamlit default menu/footer */
#MainMenu, footer, header { visibility: hidden; }

/* ══════════════════════════════════════════
   ANIMATIONS
══════════════════════════════════════════ */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-8px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulseLive {
    0%, 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.4); }
    50%       { box-shadow: 0 0 0 6px rgba(239,68,68,0); }
}
@keyframes spin {
    to { transform: rotate(360deg); }
}
</style>
"""
