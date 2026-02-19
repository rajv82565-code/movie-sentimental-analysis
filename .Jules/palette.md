## 2025-05-14 - Streamlit Native Container Styling
**Learning:** Manual HTML `div` wrappers in Streamlit often break due to its internal DOM insertion logic. Using `st.container(border=True)` and targeting `[data-testid="stVerticalBlockBorderWrapper"]` for custom styles (like background and padding) provides a more robust and native-feeling card component.
**Action:** Use `st.container(border=True)` for grouping elements and style via `data-testid` selectors instead of manual HTML `div` blocks.
