## 2025-05-22 - [Streamlit Theming and Layout]
**Learning:** Custom CSS targeting the `body` tag in Streamlit is often ineffective because Streamlit's internal DOM structure (specifically `stAppViewContainer`) overrides it. Additionally, manual HTML wrappers across multiple `st.markdown` calls break because Streamlit wraps each call in its own div.
**Action:** Use `[data-testid="stAppViewContainer"]` for background styling and `st.container(border=True)` combined with `[data-testid="stVerticalBlockBorderWrapper"]` for consistent card layouts that wrap native widgets.
