## 2025-05-14 - Streamlit Layout and Accessibility
**Learning:** Manual HTML `<div>` wrappers in Streamlit often break because the library inserts its own divs between opening and closing tags. Additionally, standard CSS background rules (e.g., `body`) are often overridden by Streamlit's internal layout containers.
**Action:** Use `with st.container(border=True):` for grouping and target `data-testid="stAppViewContainer"` and `data-testid="stVerticalBlockBorderWrapper"` for robust theming and card styling. Always add `role="status"` and `aria-live="polite"` to dynamic result containers.
