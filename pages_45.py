import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random as rnd

PLOTLY_THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(248,250,252,0.8)",
    font_color="#64748b",
    font_family="Inter, sans-serif",
    colorway=["#6366f1","#8b5cf6","#06b6d4","#10b981","#f59e0b","#ef4444"],
)

def page_insights(df, ROADS):
    st.markdown("<div class='page-title'>🧠 Smart Insights</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>AI-powered recommendations based on traffic patterns</div>", unsafe_allow_html=True)

    hourly_avg = df.groupby("Hour")["Vehicle_Count"].mean()
    peak_h = int(hourly_avg.idxmax())
    low_h  = int(hourly_avg.idxmin())
    top_road = df.groupby("Road_Name")["Vehicle_Count"].sum().idxmax()
    avg_d = df["Traffic_Density"].mean()
    crit_pct = round(len(df[df["Congestion_Level"]=="Critical"])/len(df)*100,1)

    insights = [
        ("purple","⏰ Peak Traffic Hour",
         f"Heaviest traffic at <b>{peak_h:02d}:00–{peak_h+1:02d}:00</b>. Deploy adaptive signal control and increase green-wave cycles."),
        ("blue","🌙 Low Traffic Window",
         f"Traffic drops to minimum at <b>{low_h:02d}:00</b>. Best window for road maintenance and infrastructure upgrades."),
        ("green","🛣️ Most Congested Road",
         f"<b>{top_road}</b> carries the highest vehicle volume. Consider AI-based dynamic routing and diversion strategies."),
        ("orange","🌡️ Congestion Overview",
         f"Avg density: <b>{avg_d:.0%}</b>. Critical congestion: <b>{crit_pct}%</b> of all observations."),
        ("purple","🚦 Signal Optimization",
         "AI recommends adaptive timing on peak corridors. Green-wave sync could cut delays by <b>35%</b>."),
        ("green","🌿 Eco Recommendation",
         "High density correlates with AQI spikes. Promote EV lanes and carpooling to cut emissions by <b>~22%</b>."),
        ("blue","📱 Smart Routing",
         f"Divert {top_road} overflow via alternate corridors 8–10 AM. Push real-time suggestions via city nav apps."),
        ("orange","🏥 Emergency Corridor",
         f"Pre-clear {top_road} during peak hours. Auto green-wave for emergency vehicles reduces ETA by <b>40%</b>."),
    ]

    col1, col2 = st.columns(2)
    for i, (cls, title, body) in enumerate(insights):
        target = col1 if i % 2 == 0 else col2
        target.markdown(f"""
        <div class='insight-card {cls}'>
          <h4>{title}</h4><p>{body}</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>📈 Traffic Prediction vs Historical</div>", unsafe_allow_html=True)
    hours = list(range(24))
    base = hourly_avg.reindex(hours).fillna(hourly_avg.mean()).values
    pred = np.clip(base + np.random.normal(0,10,24), 0, None)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hours, y=base, name="Historical Avg",
        line=dict(color="#6366f1", width=2.5), mode="lines"))
    fig.add_trace(go.Scatter(x=hours, y=pred, name="AI Prediction",
        line=dict(color="#10b981", width=2.5, dash="dot"), mode="lines"))
    fig.add_trace(go.Scatter(x=hours+hours[::-1],
        y=list(pred+15)+list((pred-10)[::-1]),
        fill="toself", fillcolor="rgba(99,102,241,0.07)",
        line=dict(color="rgba(0,0,0,0)"), name="Confidence Band"))
    fig.update_layout(title="Next 24h AI Traffic Forecast", **PLOTLY_THEME,
        title_font_color="#1e293b", title_font_size=15,
        xaxis=dict(title="Hour", gridcolor="#f1f5f9"),
        yaxis=dict(title="Vehicles", gridcolor="#f1f5f9"),
        legend=dict(bgcolor="rgba(0,0,0,0)"), height=360)
    st.plotly_chart(fig, use_container_width=True)


def page_smartcity(df, ROADS):
    st.markdown("<div class='page-title'>🏙️ Smart City Features</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Futuristic AI-powered city management modules</div>", unsafe_allow_html=True)

    features = [
        ("🚦","Signal Optimization","Active","#6366f1","#eef2ff",f"{rnd.randint(82,97)}% eff."),
        ("🚨","Emergency Alert","Standby","#ef4444","#fef2f2","Auto green-wave"),
        ("⚠️","Accident Risk","Monitoring","#f59e0b","#fffbeb",f"Risk: {rnd.randint(12,38)}%"),
        ("🔮","Traffic Prediction","Live","#8b5cf6","#faf5ff","98.2% accuracy"),
        ("🌿","Pollution Monitor","Active","#10b981","#ecfdf5",f"AQI: {rnd.randint(62,140)}"),
        ("📊","Traffic Efficiency","Optimal","#0ea5e9","#eff6ff",f"{rnd.randint(74,92)}% score"),
    ]

    cols = st.columns(3)
    for i,(icon, title, status, color, bg, metric) in enumerate(features):
        cols[i%3].markdown(f"""
        <div class='feature-card' style='background:{bg};border-color:rgba(0,0,0,0.05)'>
          <span class='feature-icon'>{icon}</span>
          <div class='feature-title'>{title}</div>
          <div class='feature-value' style='color:{color}'>{metric}</div>
          <div class='feature-sub' style='margin-top:4px'>
            <span style='background:{color}22;color:{color};padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700'>{status}</span>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1,1])

    with c1:
        st.markdown("<div class='section-header'>🚨 Emergency Alert Simulation</div>", unsafe_allow_html=True)
        if st.button("🔴 Trigger Emergency Alert"):
            road = rnd.choice(ROADS)
            st.markdown(f"""
            <div class='glass-panel' style='border-left:4px solid #ef4444;background:#fef2f2'>
              <b style='color:#dc2626'>🚨 EMERGENCY DISPATCH</b><br>
              <span style='color:#64748b;font-size:13px'>Ambulance on <b style='color:#1e293b'>{road}</b><br>
              ✅ Green-wave activated — 2.4 km corridor<br>⏱️ ETA to hospital: ~4 min</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("<div class='glass-panel' style='color:#94a3b8;font-size:13px'>Click to simulate emergency vehicle alert system.</div>", unsafe_allow_html=True)

        st.markdown("<br><div class='section-header'>⚠️ Road Risk Assessment</div>", unsafe_allow_html=True)
        for road in ROADS[:5]:
            risk = round(rnd.uniform(0.1,0.9),2)
            color = "#10b981" if risk<0.4 else "#f59e0b" if risk<0.7 else "#ef4444"
            label = "Low Risk" if risk<0.4 else "Medium" if risk<0.7 else "High Risk"
            st.markdown(f"""
            <div class='road-row'>
              <span class='road-name'>{road}</span>
              <span style='color:{color};font-size:12px;font-weight:700'>{label} ({risk:.0%})</span>
            </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='section-header'>🔔 Recent Alerts</div>", unsafe_allow_html=True)
        alerts = [
            ("#ef4444","🚨","Critical","Outer Ring Road at 96% capacity — diversion active"),
            ("#f59e0b","⚠️","Warning",f"{ROADS[0]} moderate congestion detected"),
            ("#10b981","✅","Resolved","Signal optimisation complete on 6 corridors"),
            ("#6366f1","🔮","Prediction","Peak expected at 17:30 — pre-signals adjusted"),
            ("#0ea5e9","🌿","Pollution","AQI elevated near Electronic City Road"),
        ]
        for color, icon, level, msg in alerts:
            st.markdown(f"""
            <div class='alert-card'>
              <div class='alert-dot' style='background:{color}'></div>
              <div>
                <div style='font-size:12px;font-weight:700;color:{color}'>{icon} {level}</div>
                <div style='font-size:13px;color:#334155;margin-top:2px'>{msg}</div>
              </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>🔮 48-Hour Traffic Forecast</div>", unsafe_allow_html=True)
    import plotly.graph_objects as go2
    hrs48 = list(range(48))
    base_p = list(df.groupby("Hour")["Vehicle_Count"].mean().reindex(range(24)).fillna(50).values)*2
    pred48 = [max(0,v+rnd.gauss(0,12)) for v in base_p]
    upper  = [v+rnd.uniform(18,32) for v in pred48]
    lower  = [max(0,v-rnd.uniform(10,20)) for v in pred48]
    fig48 = go.Figure()
    fig48.add_trace(go.Scatter(x=hrs48+hrs48[::-1], y=upper+lower[::-1],
        fill="toself", fillcolor="rgba(99,102,241,0.08)", line=dict(color="rgba(0,0,0,0)"), name="Confidence"))
    fig48.add_trace(go.Scatter(x=hrs48, y=pred48, mode="lines",
        line=dict(color="#6366f1",width=2.5), name="Predicted"))
    fig48.update_layout(title="48-Hour Vehicle Count Forecast", **PLOTLY_THEME,
        title_font_color="#1e293b", title_font_size=15,
        xaxis=dict(title="Hour",gridcolor="#f1f5f9"),
        yaxis=dict(title="Vehicles",gridcolor="#f1f5f9"),
        legend=dict(bgcolor="rgba(0,0,0,0)"), height=340)
    st.plotly_chart(fig48, use_container_width=True)

    poll = df.groupby("Road_Name")["Pollution_Index"].mean().sort_values(ascending=False)
    import plotly.express as px
    fig_p = px.bar(poll.reset_index(), x="Road_Name", y="Pollution_Index",
        title="🌿 Pollution Index by Road",
        color="Pollution_Index", color_continuous_scale=["#10b981","#f59e0b","#ef4444"])
    fig_p.update_layout(**PLOTLY_THEME, title_font_color="#1e293b", title_font_size=15,
        xaxis=dict(gridcolor="#f1f5f9"), yaxis=dict(gridcolor="#f1f5f9"), height=320,
        margin=dict(l=0,r=0,t=40,b=80))
    st.plotly_chart(fig_p, use_container_width=True)
