## 2025-05-15 - Streamlit Widget Label Styling
**Learning:** Streamlit widget labels (like for `st.text_area`) are often rendered inside a `div` with `data-testid="stWidgetLabel"` containing a `p` tag. To make them readable on dark backgrounds, targeting `[data-testid="stWidgetLabel"] p` with `!important` is effective.
**Action:** Use `[data-testid="stWidgetLabel"] p { color: #hex !important; }` when customizing Streamlit themes via CSS injection.

## 2025-05-15 - Native Containers over HTML hacks
**Learning:** Splitting HTML tags across multiple `st.markdown` calls (e.g., opening a div in one and closing in another) causes the browser to auto-close them, breaking layout.
**Action:** Use `st.container(border=True)` and target `[data-testid="stVerticalBlockBorderWrapper"]` for card-like styling instead of manual HTML divs.
