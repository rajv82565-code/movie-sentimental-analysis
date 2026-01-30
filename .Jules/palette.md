## 2026-01-30 - Streamlit Custom Layout Containers
**Learning:** In Streamlit, separate `st.markdown` calls with `unsafe_allow_html=True` cannot be used to open and close a single HTML tag (like a `div` wrapper) across widgets. Each call creates its own container, leading to broken HTML and "ghost" empty elements.
**Action:** Combine related custom HTML into a single `st.markdown` call, or use native `st.container` and target it via specific CSS if absolute wrapping of widgets is required. For simple headers, a single markdown block for the whole card is preferred.
