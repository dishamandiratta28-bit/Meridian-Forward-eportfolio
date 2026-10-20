import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Learning Team 11 | HCM AS2",
    page_icon="◌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Editorial visual system ----------
BG = "#F4F0E6"
PAPER = "#FBF9F3"
INK = "#243D30"
GREEN = "#6D8A70"
SAGE = "#D8E2D2"
CLAY = "#C98268"
BLUE = "#BFD4D4"
MUTED = "#72796F"
LINE = "#D7D6CA"

st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
      :root {{ --bg:{BG}; --paper:{PAPER}; --ink:{INK}; --green:{GREEN}; }}
      .stApp {{ background:var(--bg); color:var(--ink); }}
      [data-testid="stHeader"] {{ background:rgba(244,240,230,0.9); }}
      [data-testid="stSidebar"] {{ background:var(--paper); }}
      html, body, [class*="css"] {{ font-family:'DM Sans',sans-serif; }}
      h1,h2,h3 {{ font-family:'Playfair Display',serif !important; color:var(--ink) !important; }}
      .eyebrow {{ text-transform:uppercase; letter-spacing:.17em; font-size:.72rem; color:{MUTED}; font-weight:700; }}
      .hero {{ background:{PAPER}; border:1px solid {LINE}; border-radius:22px; padding:34px 36px; }}
      .hero-title {{ font-family:'Playfair Display',serif; font-size:clamp(2.5rem,5vw,5rem); line-height:1.02; letter-spacing:-.04em; color:{INK}; }}
      .hero-sub {{ font-size:.86rem; letter-spacing:.06em; color:{MUTED}; margin-top:16px; }}
      .metric {{ background:{PAPER}; border:1px solid {LINE}; padding:20px 22px; border-radius:18px; min-height:126px; }}
      .metric-label {{ color:{MUTED}; text-transform:uppercase; letter-spacing:.12em; font-size:.68rem; }}
      .metric-value {{ color:{INK}; font-family:'Playfair Display',serif; font-size:2.25rem; margin-top:5px; }}
      .metric-note {{ color:{MUTED}; font-size:.76rem; margin-top:2px; }}
      .section-no {{ font-family:'Playfair Display',serif; font-size:3.2rem; color:{GREEN}; line-height:1; }}
      .small-note {{ font-size:.76rem; color:{MUTED}; }}
      .stage-card {{ background:{PAPER}; border:1px solid {LINE}; border-radius:16px; padding:18px 16px; min-height:116px; }}
      .stage-num {{ font-size:.7rem; letter-spacing:.12em; color:{MUTED}; }}
      .stage-name {{ font-family:'Playfair Display',serif; color:{INK}; font-size:1.28rem; margin-top:8px; }}
      .stage-status {{ font-size:.7rem; margin-top:8px; color:{GREEN}; }}
      div[data-testid="stTabs"] button {{ font-weight:600; color:{INK}; }}
      div[data-testid="stTabs"] button[aria-selected="true"] {{ border-bottom-color:{GREEN}; color:{INK}; }}
      .stButton > button {{ border-radius:999px; border:1px solid {LINE}; background:{PAPER}; color:{INK}; }}
      .stButton > button:hover {{ border-color:{GREEN}; color:{INK}; }}
      hr {{ border-color:{LINE}; }}
      footer {{ visibility:hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

def base_fig(fig, height=340):
    fig.update_layout(
        height=height,
        paper_bgcolor=PAPER,
        plot_bgcolor=PAPER,
        font=dict(family="DM Sans", color=INK, size=12),
        margin=dict(l=12, r=12, t=24, b=12),
        showlegend=False,
    )
    fig.update_xaxes(showgrid=False, zeroline=False, showline=False, tickfont=dict(color=MUTED))
    fig.update_yaxes(showgrid=True, gridcolor="#E8E5DB", zeroline=False, showline=False, tickfont=dict(color=MUTED))
    return fig

# ---------- Top navigation ----------
st.markdown(
    f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:4px 0 22px 0">
      <div class="eyebrow">LEARNING TEAM 11 &nbsp; / &nbsp; HCM AS2</div>
      <div style="font-size:.75rem;color:{MUTED};letter-spacing:.08em">MERIDIAN FORWARD</div>
    </div>""",
    unsafe_allow_html=True,
)

pages = ["The journey", "What we did", "How we did it", "Outcome", "Team progress", "Contributions", "Evidence appendix"]
selected = st.radio("Navigate", pages, horizontal=True, label_visibility="collapsed")

# ---------- Hero ----------
if selected == "The journey":
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">A visual case study · AS2</div>
          <div class="hero-title">From workforce<br>gaps to decisions.</div>
          <div class="hero-sub">DISCOVER &nbsp; → &nbsp; ANALYSE &nbsp; → &nbsp; DESIGN &nbsp; → &nbsp; REFLECT</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    m1, m2, m3, m4 = st.columns(4)
    for col, label, value, note in [
        (m1, "BASELINE GAP", "544 h", "role shortages"),
        (m2, "SPARE CAPACITY", "172 h", "identified in baseline"),
        (m3, "NET DEFICIT", "372 h", "after spare capacity"),
        (m4, "PILOT WINDOW", "4 weeks", "case constraint"),
    ]:
        with col:
            st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-note">{note}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="eyebrow">THE PROGRESSION</div>', unsafe_allow_html=True)
    cols = st.columns([1, .18, 1, .18, 1, .18, 1])
    stages = [
        ("01", "Discover", "What is the problem?", SAGE),
        ("02", "Analyse", "What does the evidence say?", "#E8DCC8"),
        ("03", "Design", "Which option could work?", BLUE),
        ("04", "Reflect", "What changed / remains?", "#E9D9D0"),
    ]
    for i, (num, name, sub, tint) in enumerate(stages):
        with cols[i * 2]:
            st.markdown(f'<div class="stage-card" style="background:{tint}"><div class="stage-num">{num}</div><div class="stage-name">{name}</div><div class="small-note">{sub}</div></div>', unsafe_allow_html=True)
        if i < 3:
            with cols[i * 2 + 1]:
                st.markdown(f'<div style="padding-top:42px;text-align:center;color:{GREEN};font-size:1.4rem">→</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="eyebrow">THREE LENSES</div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a:
        st.markdown("### 01")
        st.markdown("**WHAT**")
        st.caption("Deliverables · work completed · evidence")
    with b:
        st.markdown("### 02")
        st.markdown("**HOW**")
        st.caption("Methods · calculations · decision logic")
    with c:
        st.markdown("### 03")
        st.markdown("**OUTCOME**")
        st.caption("Recommendation · conditions · learning")

elif selected == "What we did":
    st.markdown('<div class="eyebrow">01 / WHAT WE DID</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.3rem">The work, in three parts.</div>', unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    deliverables = [
        (c1, "01", "Business alignment", "01 / ALIGN", SAGE, "Business need and SHRBP alignment"),
        (c2, "02", "Workforce planning", "02 / DESIGN", "#E8DCC8", "Capacity, shortages, and role-level gaps"),
        (c3, "03", "Attraction & onboarding", "03 / ENABLE", BLUE, "Conditional vendor scenario and readiness"),
    ]
    for col, num, title, tag, tint, caption in deliverables:
        with col:
            st.markdown(f'<div class="stage-card" style="background:{tint};min-height:180px"><div class="eyebrow">{tag}</div><div class="section-no">{num}</div><div class="stage-name">{title}</div><div class="small-note">{caption}</div></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("#### Workforce capacity map")
    role_df = pd.DataFrame({
        "Role": ["Data preparation", "Quality assurance", "Legacy systems"],
        "Shortage (h)": [352, 96, 96],
    })
    fig = px.bar(role_df, x="Shortage (h)", y="Role", orientation="h", text="Shortage (h)",
                 color_discrete_sequence=[GREEN])
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_layout(yaxis=dict(autorange="reversed"), xaxis_title="Hours", yaxis_title="")
    st.plotly_chart(base_fig(fig, 310), use_container_width=True)
    st.caption("Baseline role shortages total 544 hours. Spare capacity is 172 hours; net deficit is 372 hours.")

elif selected == "How we did it":
    st.markdown('<div class="eyebrow">02 / HOW WE DID IT</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.3rem">Evidence → choices → checks.</div>', unsafe_allow_html=True)
    st.write("")
    flow = st.columns(5)
    flow_items = [
        ("01", "Map roles", SAGE),
        ("02", "Quantify gaps", "#E8DCC8"),
        ("03", "Compare options", BLUE),
        ("04", "Cost scenario", "#E9D9D0"),
        ("05", "Check gates", SAGE),
    ]
    for col, (num, label, tint) in zip(flow, flow_items):
        with col:
            st.markdown(f'<div class="stage-card" style="background:{tint};text-align:center"><div class="stage-num">{num}</div><div class="stage-name" style="font-size:1.05rem">{label}</div></div>', unsafe_allow_html=True)
    st.write("")
    left, right = st.columns([1.15, 1])
    with left:
        st.markdown("#### Role gap → proposed vendor coverage")
        data = pd.DataFrame({
            "Role": ["Data preparation", "Quality assurance", "Legacy systems"],
            "Baseline gap": [352, 96, 96],
            "Residual gap": [80, 72, 64],
        })
        fig = go.Figure()
        fig.add_trace(go.Bar(y=data["Role"], x=data["Baseline gap"], name="Baseline gap", orientation="h",
                             marker_color="#C7D3C3"))
        fig.add_trace(go.Bar(y=data["Role"], x=data["Residual gap"], name="Residual gap", orientation="h",
                             marker_color=CLAY))
        fig.update_layout(barmode="overlay", xaxis_title="Hours", yaxis_title="", showlegend=True,
                          legend=dict(orientation="h", y=1.12, x=0))
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(base_fig(fig, 320), use_container_width=True)
    with right:
        st.markdown("#### Decision gates")
        gate_data = pd.DataFrame({
            "Gate": ["Authorized access", "Workload cover", "Decision authority"],
            "Ready": [0, 0, 0],
        })
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=gate_data["Gate"], y=[1, 1, 1],
            marker_color=["#D8D6CB"] * 3,
            text=["PENDING", "PENDING", "PENDING"],
            textposition="inside",
            insidetextanchor="middle",
        ))
        fig.update_layout(yaxis=dict(visible=False, range=[0, 1.2]), xaxis_title="", yaxis_title="")
        st.plotly_chart(base_fig(fig, 320), use_container_width=True)
        st.caption("No pilot hours should be counted as ready until the required gates are cleared.")
    st.write("")
    st.markdown("#### Cost comparison")
    cost_cols = st.columns(3)
    for col, label, value, tint in [
        (cost_cols[0], "BASELINE VENDOR COST", "₹6.40L", "#E9D9D0"),
        (cost_cols[1], "BUDGET CAP", "₹6.00L", "#E8DCC8"),
        (cost_cols[2], "CONDITIONAL SCENARIO", "₹3.76L", SAGE),
    ]:
        with col:
            st.markdown(f'<div class="metric" style="background:{tint}"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

elif selected == "Outcome":
    st.markdown('<div class="eyebrow">03 / OUTCOME</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.3rem">A recommendation, with conditions.</div>', unsafe_allow_html=True)
    st.write("")
    l, r = st.columns([1, 1])
    with l:
        st.markdown("#### Cost against cap")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=["Baseline", "Cap", "Proposed*"],
            y=[6.40, 6.00, 3.76],
            marker_color=["#C98268", "#B9B6A8", GREEN],
            text=["₹6.40L", "₹6.00L", "₹3.76L"],
            textposition="outside",
        ))
        fig.update_layout(yaxis_title="₹ lakh", yaxis=dict(range=[0, 7.2]), xaxis_title="")
        st.plotly_chart(base_fig(fig, 350), use_container_width=True)
        st.caption("*Conditional redesigned scenario; not approved.")
    with r:
        st.markdown("#### Residual gaps in the proposed scenario")
        residual = pd.DataFrame({
            "Role": ["Data preparation", "Quality assurance", "Legacy systems"],
            "Hours": [80, 72, 64],
        })
        fig = px.pie(residual, values="Hours", names="Role", hole=.58,
                     color_discrete_sequence=[GREEN, "#B9CBB5", CLAY])
        fig.update_traces(textposition="outside", textinfo="label+value")
        fig.update_layout(showlegend=False)
        st.plotly_chart(base_fig(fig, 350), use_container_width=True)
        st.caption("216 hours remain unresolved until readiness gates are cleared.")
    st.markdown("#### What remains")
    stages = st.columns(4)
    remaining = [
        ("01", "Access", "Confirm"),
        ("02", "Cover", "Arrange"),
        ("03", "Authority", "Approve"),
        ("04", "Pilot", "Then start"),
    ]
    for col, (n, label, status) in zip(stages, remaining):
        with col:
            st.markdown(f'<div class="stage-card"><div class="stage-num">{n}</div><div class="stage-name">{label}</div><div class="stage-status">○ {status}</div></div>', unsafe_allow_html=True)

elif selected == "Team progress":
    st.markdown('<div class="eyebrow">04 / TEAM PROGRESS</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.3rem">The learning record.</div>', unsafe_allow_html=True)
    st.caption("Update milestones with real progress. Do not mark work complete without evidence.")
    st.write("")
    default = pd.DataFrame([
        {"Milestone": "Understand the case", "Status": "Completed", "Evidence / artifact": "AS2 presentation", "Learning / change": ""},
        {"Milestone": "Workforce gap analysis", "Status": "Completed", "Evidence / artifact": "Role-hour calculations", "Learning / change": ""},
        {"Milestone": "Build conditional scenario", "Status": "Completed", "Evidence / artifact": "Cost and residual-gap analysis", "Learning / change": ""},
        {"Milestone": "Corporate mentor feedback", "Status": "In progress", "Evidence / artifact": "", "Learning / change": ""},
        {"Milestone": "Final validation and reflection", "Status": "Not started", "Evidence / artifact": "", "Learning / change": ""},
    ])
    if "milestones" not in st.session_state:
        st.session_state.milestones = default.copy()
    edited = st.data_editor(
        st.session_state.milestones,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        column_config={
            "Status": st.column_config.SelectboxColumn(
                "Status", options=["Not started", "In progress", "Completed"], required=True
            ),
            "Milestone": st.column_config.TextColumn("Milestone", required=True),
            "Evidence / artifact": st.column_config.TextColumn("Evidence / artifact"),
            "Learning / change": st.column_config.TextColumn("Learning / change"),
        },
        key="milestone_editor",
    )
    st.session_state.milestones = edited
    st.write("")
    total = max(len(edited), 1)
    completed = int((edited["Status"] == "Completed").sum()) if len(edited) else 0
    in_progress = int((edited["Status"] == "In progress").sum()) if len(edited) else 0
    not_started = int((edited["Status"] == "Not started").sum()) if len(edited) else 0
    p1, p2, p3 = st.columns(3)
    for col, label, value, color in [
        (p1, "COMPLETED", completed, GREEN),
        (p2, "IN PROGRESS", in_progress, CLAY),
        (p3, "NOT STARTED", not_started, MUTED),
    ]:
        with col:
            st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)
    st.progress(completed / total)
    st.caption("Progress is based on the milestone statuses you set. This prototype keeps edits for the current session.")

elif selected == "Contributions":
    st.markdown('<div class="eyebrow">05 / CONTRIBUTIONS & ACCOUNTABILITY</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.1rem">Five people. A visible work trail.</div>', unsafe_allow_html=True)
    st.caption("Based on the team's account. Dates and artifacts must be verified; none are invented.")
    members = {
        "Disha Mandiratta": ["Created AS1 presentation", "Created AS2 presentation", "Created AS3 presentation and later rectified it", "Developed the Streamlit ePortfolio"],
        "Karan Siwas": ["Made relevant changes and redesigned AS1 and AS2 presentations", "Worked on AS3 and incorporated relevant changes", "Created decentralisation diagram and workflow chart"],
        "Divyanshu Gupta": ["Checked presentation content"],
        "Mahak Sahu": ["Checked presentation content"],
        "Tamanna Joshi": ["Checked presentation content"],
    }
    for name, tasks in members.items():
        with st.container(border=True):
            st.markdown(f"### {name}")
            for task in tasks: st.markdown(f"- {task}")
    st.markdown("#### Dated contribution log")
    st.info("Replace ‘Date to be confirmed’ with a date only when supported by file history, messages, or meeting records.")
    rows = [
        ["Date to be confirmed", "Disha Mandiratta", "AS1 presentation", "Created presentation", "Add file/version link"],
        ["Date to be confirmed", "Disha Mandiratta", "AS2 presentation", "Created presentation", "Add file/version link"],
        ["Date to be confirmed", "Karan Siwas", "AS1 / AS2 presentations", "Relevant changes and redesign", "Add revised file link"],
        ["Date to be confirmed", "Disha Mandiratta", "AS3 presentation", "Created and later rectified presentation", "Add file/version link"],
        ["Date to be confirmed", "Karan Siwas", "AS3 presentation", "Made relevant changes", "Add revised file link"],
        ["Date to be confirmed", "Karan Siwas", "Decentralisation / workflow", "Created diagram and workflow chart", "Add diagram link"],
        ["Date to be confirmed", "Disha Mandiratta", "Streamlit ePortfolio", "Developed portfolio", "Add repository/app link"],
        ["Date to be confirmed", "Divyanshu Gupta", "Presentations", "Checked content", "Add evidence if available"],
        ["Date to be confirmed", "Mahak Sahu", "Presentations", "Checked content", "Add evidence if available"],
        ["Date to be confirmed", "Tamanna Joshi", "Presentations", "Checked content", "Add evidence if available"],
    ]
    df = pd.DataFrame(rows, columns=["Date", "Member", "Deliverable", "Action", "Evidence / link"])
    if "contribution_log" not in st.session_state: st.session_state.contribution_log = df
    st.session_state.contribution_log = st.data_editor(st.session_state.contribution_log, use_container_width=True, hide_index=True, num_rows="dynamic", key="contrib_editor")
    st.download_button("Download contribution log CSV", st.session_state.contribution_log.to_csv(index=False).encode(), "team_contribution_log.csv", "text/csv")
    st.markdown("#### Learning and revisions")
    st.caption("Record real feedback, what changed, why, date, and supporting evidence. Do not invent learning outcomes.")
    rev = pd.DataFrame([["Date to be confirmed", "To be added", "To be completed by team", "Reasoned response / learning", "Add evidence link"]], columns=["Date", "Trigger / feedback", "What changed", "Reason / learning", "Evidence link"])
    if "revision_log" not in st.session_state: st.session_state.revision_log = rev
    st.session_state.revision_log = st.data_editor(st.session_state.revision_log, use_container_width=True, hide_index=True, num_rows="dynamic", key="revision_editor")
    st.download_button("Download revision log CSV", st.session_state.revision_log.to_csv(index=False).encode(), "learning_revision_log.csv", "text/csv")
    st.markdown("#### Corporate mentor engagement")
    st.warning("Status: NOT YET RECORDED. Do not imply contact, guidance, or approval until it actually occurs.")
    mentor = pd.DataFrame([["Faculty-approved question", "Enter exact approved question"], ["Mentor name", "Rashi Varshney — confirm intended mentor"], ["Engagement status", "Not yet recorded; confirm current status"], ["Contact date", "Pending"], ["Guidance received", "Pending — do not invent"], ["Team response and rationale", "Pending until guidance is received"], ["Revision / follow-up date", "Pending"]], columns=["Field", "Record"])
    st.dataframe(mentor, use_container_width=True, hide_index=True)

elif selected == "Evidence appendix":
    st.markdown('<div class="eyebrow">06 / EVIDENCE APPENDIX</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title" style="font-size:3.1rem">Show the working.</div>', unsafe_allow_html=True)
    st.caption("Figures currently used in the portfolio. Attach the controlling workbook and source-page references before final submission.")
    st.markdown("#### Calculation trail")
    calc = pd.DataFrame([
        ["Data preparation shortage", "Case input", 352, "Attach workbook reference"],
        ["Quality assurance shortage", "Case input", 96, "Attach workbook reference"],
        ["Legacy systems shortage", "Case input", 96, "Attach workbook reference"],
        ["Total baseline shortage", "352 + 96 + 96", 544, "Calculated"],
        ["Spare capacity", "Case input", 172, "Attach workbook reference"],
        ["Net deficit", "544 − 172", 372, "Calculated"],
        ["Conditional data preparation residual", "Scenario value", 80, "Not approved; gates pending"],
        ["Conditional QA residual", "Scenario value", 72, "Not approved; gates pending"],
        ["Conditional legacy residual", "Scenario value", 64, "Not approved; gates pending"],
        ["Total conditional residual", "80 + 72 + 64", 216, "Not ready capacity"],
    ], columns=["Item", "Calculation / input", "Hours", "Status"])
    st.dataframe(calc, use_container_width=True, hide_index=True)
    st.markdown("#### Conditional vendor costs")
    costs = pd.DataFrame([
        ["Data preparation", 1, 160, 550, "1 × 160 × 550", 88000],
        ["Quality assurance", 1, 160, 800, "1 × 160 × 800", 128000],
        ["Legacy systems", 1, 160, 1000, "1 × 160 × 1,000", 160000],
    ], columns=["Role", "Workers", "Hours per worker", "Rate/hour (₹)", "Calculation", "Cost (₹)"])
    st.dataframe(costs, use_container_width=True, hide_index=True)
    a, b, c = st.columns(3)
    a.metric("Conditional total", "₹3,76,000")
    b.metric("Budget cap", "₹6,00,000")
    c.metric("Headroom under cap", "₹2,24,000")
    st.caption("Baseline vendor cost is ₹6,40,000: ₹40,000 above the cap. The ₹3.76 lakh scenario is conditional, not approved.")
    st.markdown("#### Readiness gates")
    st.dataframe(pd.DataFrame([["Authorised access", "Not confirmed", "Do not count capacity as ready"], ["Workload / legacy cover", "Not confirmed", "Do not count capacity as ready"], ["Decision authority and supervision", "Not confirmed", "Do not count capacity as ready"]], columns=["Gate", "Status", "Effect"]), use_container_width=True, hide_index=True)
    st.markdown("#### Assumption and source register")
    assumptions = pd.DataFrame([
        ["A01", "One vendor worker per role; 160 hours each", "Basis of cost scenario", "Case calculations; attach workbook", "Scenario assumption, not approval"],
        ["A02", "102.4 effective hours per worker in residual-gap scenario", "Used for conditional capacity scenario", "AS2 case working; attach workbook", "Scenario assumption"],
        ["A03", "All three readiness gates must clear", "Prevents counting unready hours", "Case notes P063, P168, P183–P184, P188", "Gates not confirmed"],
        ["A04", "Permanent hires add zero pilot hours due to 8-week lead time vs 4-week pilot", "Hiring supports later supply", "Case planning constraint; attach source page", "Case constraint"],
        ["A05", "Selection tests / weighted criteria are proposals, not existing policy", "Approving owner required", "Q6.01; Q6.05 teaching illustration", "Proposed; approval required"],
        ["A06", "Salary, fee and induction cash costs not supplied", "Do not fabricate costs", "Q6.04", "Not supplied"],
        ["A07", "600-position request not accepted as submitted", "Separate long-term plan from pilot", "P044, P051, Q5.01", "Case limitation"],
    ], columns=["ID", "Assumption / limitation", "Impact / rationale", "Source reference", "Status"])
    st.dataframe(assumptions, use_container_width=True, hide_index=True)
    st.caption("Starter register based on available case notes; not the complete A01–A19 register. Add remaining entries from the controlling workbook; do not guess.")
    st.markdown("#### Proposed role specifications")
    st.dataframe(pd.DataFrame([["Data preparation", "Anomalous customer-data pack and validation explanation", "Proposal only; approving owner required"], ["Quality assurance", "Validation task and judgement questions", "Proposal only; approving owner required"], ["Legacy systems", "Teach-back of contract exception / legacy process", "Proposal only; approving owner required"]], columns=["Role", "Proposed work sample", "Status"]), use_container_width=True, hide_index=True)
    st.markdown("#### Supporting sources to attach")
    st.write("Add the controlling AS2 case workbook, source-page references, final AS1/AS2/AS3 presentations, decentralisation diagram, workflow chart, and dated review evidence to this repository or link an approved accessible location.")
    st.warning("Mentor contact and guidance are not recorded yet. Keep this pending until actual engagement occurs.")


st.write("")
st.markdown(
    f"""<div style="border-top:1px solid {LINE};padding-top:16px;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap">
    <span class="eyebrow">LEARNING TEAM 11</span>
    <span style="font-size:.72rem;color:{MUTED}">MERIDIAN FORWARD · HCM AS2</span>
    </div>""",
    unsafe_allow_html=True,
)
