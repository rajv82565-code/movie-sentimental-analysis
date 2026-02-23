## 2026-02-23 - Streamlit HTML Injection and Layout Risks
**Learning:** Using st.markdown with unsafe_allow_html=True to wrap other Streamlit components in manual div tags results in fragmented, invalid HTML because each Streamlit call creates its own container. Additionally, embedding user input directly into these blocks creates XSS vulnerabilities.
**Action:** Use st.container(border=True) for grouping and html.escape() for any user content in unsafe_allow_html blocks. Prefer CSS targeting [data-testid="stVerticalBlockBorderWrapper"] for styling containers.
