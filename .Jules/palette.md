## 2026-02-15 - Streamlit CSS Specificity and Widget Labels
**Learning:** Streamlit's default theme often overrides simple CSS selectors. Specifically, widget labels (like those for `st.text_area`) require targeting `[data-testid="stWidgetLabel"] p` with `!important` to ensure accessible contrast on custom backgrounds.
**Action:** Always verify text contrast of all UI elements after applying a custom theme, and use data-testid selectors for reliable styling.
