## 2025-05-22 - Streamlit Theme Injection
**Learning:** Standard CSS `body` selectors are often overridden or ignored in Streamlit due to its nested iframe/container architecture.
**Action:** Always target `[data-testid="stAppViewContainer"]` for background styles and `[data-testid="stHeader"]` for header transparency to ensure theme consistency.

## 2025-05-22 - Accessible Dynamic Results
**Learning:** Streamlit `st.markdown` updates are not always announced by screen readers if they are nested in custom HTML.
**Action:** Explicitly include `role="status"` and `aria-live="polite"` in the root element of any dynamic result markdown.
