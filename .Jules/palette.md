## 2026-02-18 - Improved Streamlit Dark Theme & Accessibility
**Learning:** Streamlit's default theme often overrides simple `body` CSS selectors. Using `[data-testid="stAppViewContainer"]` and `[data-testid="stVerticalBlockBorderWrapper"]` is essential for reliable theme enforcement. Additionally, manual HTML containers in Streamlit should be replaced with `st.container(border=True)` for better integration and cleaner code.
**Action:** Always target `data-testid` selectors for theme-level CSS in Streamlit and prefer native container components over raw HTML divs.
