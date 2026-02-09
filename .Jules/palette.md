## 2025-05-15 - Streamlit UI Polish & Accessibility
**Learning:** Streamlit's default theme often overrides simple `body` CSS selectors. To effectively style the background and containers, use `[data-testid="stAppViewContainer"]` and `[data-testid="stVerticalBlockBorderWrapper"]` (for `st.container(border=True)`).
**Action:** Always target specific Streamlit data-testids for theme-consistent styling. Combine `st.spinner` with `aria-live="polite"` result containers for a smooth and accessible async-like experience even for fast local models.
