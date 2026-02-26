## 2026-02-26 - Native Streamlit Containers for Layout Stability
**Learning:** Manual HTML `div` wrappers in Streamlit often break when combined with multiple `st.*` calls due to how Streamlit inserts elements into the DOM. Using `st.container(border=True)` provides a stable native wrapper that can be reliably styled.
**Action:** Always prefer `st.container(border=True)` over manual HTML divs for card-like groupings. Target `[data-testid="stVerticalBlockBorderWrapper"]` in custom CSS to apply specific card styling (background, shadow, etc.) to these containers.
