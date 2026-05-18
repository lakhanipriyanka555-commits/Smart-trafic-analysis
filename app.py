import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import cv2, tempfile, os
import random as rnd
from datetime import datetime
from styles import get_css
from data_gen import generate_and_cache, ROADS
from pages_45 import page_insights, page_smartcity

st.set_page_config(page_title="Smart Traffic Analytics System", page_icon="🚦",
                   layout="wide", initial_sidebar_state="expanded")
st.markdown(get_css(), unsafe_allow_html=True)

PLOTLY_THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(248,250,252,0.8)",
    font_color="#64748b", font_family="Inter, sans-serif",
    colorway=["#6366f1","#8b5cf6","#06b6d4","#10b981","#f59e0b","#ef4444"],
)

@st.cache_data
def load_data():
    return generate_and_cache()

df_full = load_data()

# ── Sidebar ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sidebar-brand'>
      <div class='sidebar-logo'>🚦 SmartTraffic</div>
      <div class='sidebar-tagline'>AI Analytics Platform</div>
    </div>""", unsafe_allow_html=True)

    page = st.radio("", [
        "🏠  Overview",
        "📊  Traffic Analytics",
        "📹  Live Monitoring",
        "🧠  Smart Insights",
        "🏙️  Smart City",
    ], label_visibility="collapsed")

    st.markdown("<div class='filter-label'>Filters</div>", unsafe_allow_html=True)
    sel_roads   = st.multiselect("Roads", ROADS, default=ROADS)
    sel_density = st.multiselect("Congestion", ["Low","Moderate","High","Critical"],
                                  default=["Low","Moderate","High","Critical"])
    hour_range  = st.slider("Hour Range", 0, 23, (0, 23))

    st.markdown("<hr style='border-color:#e2e8f0;margin:16px 0'>", unsafe_allow_html=True)
    now = datetime.now()
    st.markdown(f"""
    <div style='text-align:center'>
      <div style='font-size:20px;font-weight:800;color:#1e293b'>{now.strftime('%H:%M')}</div>
      <div style='font-size:11px;color:#94a3b8'>{now.strftime('%A, %d %b %Y')}</div>
    </div>""", unsafe_allow_html=True)

# ── Filter ───────────────────────────────────────────────────────
df = df_full.copy()
if sel_roads:   df = df[df["Road_Name"].isin(sel_roads)]
if sel_density: df = df[df["Congestion_Level"].isin(sel_density)]
df = df[(df["Hour"] >= hour_range[0]) & (df["Hour"] <= hour_range[1])]

# ── Navbar ───────────────────────────────────────────────────────
now = datetime.now()
st.markdown(f"""
<div class='top-navbar'>
  <div class='navbar-brand'>Smart Traffic Analytics System</div>
  <div class='navbar-right'>
    <span class='navbar-weather'>🌤 28°C Bengaluru</span>
    <span class='navbar-time'>🕐 {now.strftime('%H:%M:%S')}</span>
    <span class='navbar-pill'>🟢 System Online</span>
    <span class='navbar-pill'>👤 Admin</span>
  </div>
</div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════
# PAGE 1 — OVERVIEW
# ════════════════════════════════════════════════════════
if "Overview" in page:
    st.markdown("<div class='page-title'>Dashboard Overview</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Real-time traffic intelligence across all monitored corridors</div>", unsafe_allow_html=True)

    total_veh = int(df["Vehicle_Count"].sum())
    avg_cong  = round(df["Traffic_Density"].mean()*100, 1)
    peak_h    = int(df.groupby("Hour")["Vehicle_Count"].mean().idxmax())
    top_road  = df.groupby("Road_Name")["Vehicle_Count"].sum().idxmax()
    n_alerts  = int(len(df[df["Congestion_Level"]=="Critical"])//100)

    kpis = [
        ("","🚗","Total Vehicles",f"{total_veh:,}","↑ 12% vs last week","kpi-icon-purple","green"),
        ("green","🌡️","Avg Congestion",f"{avg_cong}%","↓ 3% improved","kpi-icon-green","blue"),
        ("blue","⏰","Peak Hour",f"{peak_h:02d}:00","Morning rush peak","kpi-icon-blue","orange"),
        ("orange","🛣️","Top Congested",top_road[:12]+"…" if len(top_road)>12 else top_road,"High density","kpi-icon-orange","red"),
        ("red","🔔","Active Alerts",str(n_alerts),"Needs attention","kpi-icon-red",""),
    ]
    cols = st.columns(5)
    for i,(cls,icon,label,val,delta,icls,_) in enumerate(kpis):
        cols[i].markdown(f"""
        <div class='kpi-card {cls}'>
          <div class='kpi-icon-wrap {icls}'>{icon}</div>
          <div class='kpi-label'>{label}</div>
          <div class='kpi-value'>{val}</div>
          <div class='kpi-trend-{"up" if "↑" in delta else "down" if "↓" in delta else "neu"}'>{delta}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c_left, c_right = st.columns([2,1])

    with c_left:
        st.markdown("<div class='section-header'>📈 24-Hour Traffic Trend</div>", unsafe_allow_html=True)
        hourly = df.groupby("Hour")["Vehicle_Count"].mean().reset_index()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hourly["Hour"], y=hourly["Vehicle_Count"],
            fill="tozeroy", mode="lines", line=dict(color="#6366f1",width=2.5),
            fillcolor="rgba(99,102,241,0.08)", name="Avg Vehicles"))
        fig.update_layout(title="Average Vehicle Count by Hour", **PLOTLY_THEME,
            title_font_color="#1e293b", title_font_size=15, height=320,
            xaxis=dict(title="Hour",gridcolor="#f1f5f9"),
            yaxis=dict(title="Vehicles",gridcolor="#f1f5f9"))
        st.plotly_chart(fig, use_container_width=True)

    with c_right:
        st.markdown("<div class='section-header'>🛣️ Road Status</div>", unsafe_allow_html=True)
        road_sum = df.groupby("Road_Name").agg(
            Density=("Traffic_Density","mean")).reset_index().sort_values("Density",ascending=False)
        for _,row in road_sum.iterrows():
            d = row["Density"]
            badge = "badge-smooth" if d<0.35 else "badge-moderate" if d<0.65 else "badge-heavy" if d<0.85 else "badge-critical"
            lbl   = "Smooth" if d<0.35 else "Moderate" if d<0.65 else "Heavy" if d<0.85 else "Critical"
            st.markdown(f"""
            <div class='road-row'>
              <span class='road-name'>{row['Road_Name']}</span>
              <span class='{badge}'>{lbl}</span>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>📊 Daily Volume & Density</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    daily = df.groupby("Date")["Vehicle_Count"].sum().reset_index()
    fig2 = px.area(daily, x="Date", y="Vehicle_Count", title="Daily Total Vehicles",
        color_discrete_sequence=["#8b5cf6"])
    fig2.update_traces(fillcolor="rgba(139,92,246,0.08)")
    fig2.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15, height=280,
        xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(gridcolor="#f1f5f9"))
    c1.plotly_chart(fig2, use_container_width=True)

    dow = df.groupby("Day_of_Week")["Vehicle_Count"].mean().reset_index()
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dow["Day_of_Week"] = pd.Categorical(dow["Day_of_Week"], categories=order, ordered=True)
    dow = dow.sort_values("Day_of_Week")
    fig3 = px.bar(dow, x="Day_of_Week", y="Vehicle_Count", title="Avg Vehicles by Day of Week",
        color="Vehicle_Count", color_continuous_scale=["#c7d2fe","#6366f1"])
    fig3.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15, height=280,
        xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(gridcolor="#f1f5f9"),
        coloraxis_showscale=False)
    c2.plotly_chart(fig3, use_container_width=True)

    csv = df.to_csv(index=False).encode()
    st.download_button("⬇️ Download Filtered Report (CSV)", csv, "traffic_report.csv","text/csv")


# ════════════════════════════════════════════════════════
# PAGE 2 — TRAFFIC ANALYTICS
# ════════════════════════════════════════════════════════
elif "Analytics" in page:
    st.markdown("<div class='page-title'>Traffic Analytics</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Interactive visualisations across all traffic dimensions</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📈 Trends & Flow", "🗺️ Road Comparison", "🔬 Advanced Analysis"])

    with tab1:
        hourly = df.groupby("Hour")["Vehicle_Count"].mean().reset_index()
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=hourly["Hour"], y=hourly["Vehicle_Count"],
            mode="lines+markers", line=dict(color="#6366f1",width=2.5),
            marker=dict(size=6,color="#6366f1",line=dict(color="#fff",width=2)),
            name="Avg Count"))
        fig1.update_layout(title="Vehicle Count vs Time of Day", **PLOTLY_THEME,
            title_font_color="#1e293b", title_font_size=15,
            xaxis=dict(title="Hour",gridcolor="#f1f5f9"),
            yaxis=dict(title="Avg Vehicle Count",gridcolor="#f1f5f9"), height=360)
        st.plotly_chart(fig1, use_container_width=True)

        rd_hour = df.groupby(["Hour","Road_Name"])["Vehicle_Count"].mean().reset_index()
        fig2 = px.line(rd_hour, x="Hour", y="Vehicle_Count", color="Road_Name",
            title="Traffic Flow Trend by Road (Multi-Line)",
            color_discrete_sequence=["#6366f1","#8b5cf6","#06b6d4","#10b981","#f59e0b","#ef4444","#ec4899","#0ea5e9"])
        fig2.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15,
            xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(gridcolor="#f1f5f9"),
            legend=dict(bgcolor="rgba(0,0,0,0)"), height=360)
        st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        road_cong = df.groupby("Road_Name")["Traffic_Density"].mean().reset_index().sort_values("Traffic_Density",ascending=False)
        fig3 = px.bar(road_cong, x="Road_Name", y="Traffic_Density",
            title="Congestion Level by Road",
            color="Traffic_Density", color_continuous_scale=["#c7d2fe","#6366f1","#7c3aed","#ef4444"])
        fig3.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15,
            xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(title="Avg Density",gridcolor="#f1f5f9"),
            height=360, margin=dict(b=80))
        st.plotly_chart(fig3, use_container_width=True)

        c1,c2 = st.columns(2)
        dist = df["Congestion_Level"].value_counts().reset_index()
        dist.columns = ["Level","Count"]
        fig4 = px.pie(dist, names="Level", values="Count",
            title="Traffic Density Distribution", hole=0.5,
            color_discrete_map={"Low":"#10b981","Moderate":"#f59e0b","High":"#ef4444","Critical":"#8b5cf6"})
        fig4.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15, height=360)
        fig4.update_traces(textfont_size=12, marker=dict(line=dict(color="#fff",width=2)))
        c1.plotly_chart(fig4, use_container_width=True)

        spd = df.groupby("Road_Name")["Avg_Speed_kmh"].mean().reset_index().sort_values("Avg_Speed_kmh",ascending=False)
        fig5 = px.bar(spd, x="Road_Name", y="Avg_Speed_kmh",
            title="Average Speed by Road (km/h)",
            color="Avg_Speed_kmh", color_continuous_scale=["#ef4444","#f59e0b","#10b981"])
        fig5.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15,
            height=360, margin=dict(b=80), xaxis=dict(gridcolor="#f1f5f9"),
            yaxis=dict(gridcolor="#f1f5f9"))
        c2.plotly_chart(fig5, use_container_width=True)

    with tab3:
        fig6 = px.scatter(df.sample(min(2000,len(df))), x="Vehicle_Count", y="Traffic_Density",
            color="Congestion_Level", size="Pollution_Index", opacity=0.7,
            title="Vehicle Count vs Congestion Scatter",
            color_discrete_map={"Low":"#10b981","Moderate":"#f59e0b","High":"#ef4444","Critical":"#8b5cf6"})
        fig6.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15,
            xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(gridcolor="#f1f5f9"),
            legend=dict(bgcolor="rgba(0,0,0,0)"), height=380)
        st.plotly_chart(fig6, use_container_width=True)

        pivot = df.groupby(["Hour","Road_Name"])["Traffic_Density"].mean().reset_index()
        heat  = pivot.pivot(index="Road_Name", columns="Hour", values="Traffic_Density").fillna(0)
        fig7  = go.Figure(go.Heatmap(z=heat.values, x=heat.columns.tolist(), y=heat.index.tolist(),
            colorscale=[[0,"#f0f4ff"],[0.4,"#818cf8"],[0.7,"#f59e0b"],[1,"#ef4444"]],
            colorbar=dict(title="Density", tickfont=dict(color="#64748b"))))
        fig7.update_layout(title="Congestion Heatmap — Hour × Road", **PLOTLY_THEME,
            title_font_color="#1e293b", title_font_size=15, height=380)
        st.plotly_chart(fig7, use_container_width=True)

    csv = df.to_csv(index=False).encode()
    st.download_button("⬇️ Export Analytics Data", csv, "analytics.csv","text/csv")


# ════════════════════════════════════════════════════════
# PAGE 3 — LIVE MONITORING
# ════════════════════════════════════════════════════════
elif "Monitoring" in page:
    st.markdown("<div class='page-title'>Live Traffic Monitoring</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>OpenCV-powered AI vehicle detection from uploaded traffic video</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='glass-panel'>
      <b style='color:#6366f1'>🎯 How it works:</b>
      <span style='color:#64748b;font-size:13px'> Upload a traffic video → MOG2 background subtraction detects moving vehicles →
      Bounding boxes drawn → Live count & traffic status updated per frame.</span>
    </div>""", unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload Traffic Video (MP4 / AVI / MOV)", type=["mp4","avi","mov"])
    frame_ph = st.empty()
    stat_ph  = st.empty()

    if uploaded:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded.read()); tfile.flush()
        cap  = cv2.VideoCapture(tfile.name)
        fgbg = cv2.createBackgroundSubtractorMOG2(history=200,varThreshold=50,detectShadows=False)
        kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        total_f = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps     = cap.get(cv2.CAP_PROP_FPS) or 25
        skip    = max(1,int(fps//5))
        counts  = []; idx = 0
        stop    = st.button("⏹ Stop")
        while cap.isOpened() and not stop:
            ret,frame = cap.read()
            if not ret: break
            idx += 1
            if idx % skip != 0: continue
            frame = cv2.resize(frame,(720,405))
            mask  = fgbg.apply(frame)
            mask  = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kern)
            mask  = cv2.dilate(mask,kern,iterations=2)
            cnts,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            n = 0
            for c in cnts:
                if 800 < cv2.contourArea(c) < 50000:
                    x,y,w,h = cv2.boundingRect(c)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(99,102,241),2); n+=1
            counts.append(n)
            d = min(1.0,n/40)
            status = "Smooth" if d<0.35 else "Moderate" if d<0.65 else "Heavy"
            color_cv = (16,185,129) if status=="Smooth" else (245,158,11) if status=="Moderate" else (239,68,68)
            cv2.putText(frame,f"Vehicles: {n}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,color_cv,2)
            cv2.putText(frame,f"Status: {status}",(10,65),cv2.FONT_HERSHEY_SIMPLEX,0.8,color_cv,2)
            badge = f"badge-{status.lower()}"
            frame_ph.image(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB),channels="RGB",
                           caption=f"Frame {idx} | Detected: {n} vehicles")
            stat_ph.markdown(f"""
            <div class='glass-panel'>
              🚗 <b>Vehicles:</b> {n} &nbsp;|&nbsp; 📊 <b>Density:</b> {d:.0%} &nbsp;|&nbsp;
              <span class='{badge}'>● {status}</span> &nbsp;|&nbsp;
              <b>Progress:</b> {min(100,int(idx/max(total_f,1)*100))}%
            </div>""", unsafe_allow_html=True)
        cap.release(); os.unlink(tfile.name)
        if counts:
            st.success(f"✅ Done. Avg vehicles/frame: {np.mean(counts):.1f} | Peak: {max(counts)}")
            tdf = pd.DataFrame({"Frame":range(len(counts)),"Vehicles":counts})
            fig = px.line(tdf,x="Frame",y="Vehicles",title="Vehicle Count Over Frames",
                color_discrete_sequence=["#6366f1"])
            fig.update_layout(**PLOTLY_THEME,title_font_color="#1e293b",height=320,
                xaxis=dict(gridcolor="#f1f5f9"),yaxis=dict(gridcolor="#f1f5f9"))
            st.plotly_chart(fig,use_container_width=True)
    else:
        st.info("📌 Upload a traffic video to begin AI vehicle detection.")
        if st.button("▶ Run Demo Simulation"):
            demo = [int(np.random.randint(3,38)) for _ in range(60)]
            tdf  = pd.DataFrame({"Frame":range(60),"Vehicles":demo})
            fig  = px.line(tdf,x="Frame",y="Vehicles",title="Demo Simulated Vehicle Detection",
                color_discrete_sequence=["#8b5cf6"])
            fig.update_layout(**PLOTLY_THEME,title_font_color="#1e293b",height=340,
                xaxis=dict(gridcolor="#f1f5f9"),yaxis=dict(gridcolor="#f1f5f9"))
            st.plotly_chart(fig,use_container_width=True)


# ════════════════════════════════════════════════════════
# PAGE 4 — SMART INSIGHTS
# ════════════════════════════════════════════════════════
elif "Insights" in page:
    page_insights(df, ROADS)

# ════════════════════════════════════════════════════════
# PAGE 5 — SMART CITY
# ════════════════════════════════════════════════════════
elif "Smart City" in page:
    page_smartcity(df, ROADS)
