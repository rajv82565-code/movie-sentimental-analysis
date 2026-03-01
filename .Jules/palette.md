## 2025-05-15 - Streamlit Form for Enter-to-Submit
**Learning:** In Streamlit, standard text inputs do not trigger actions on 'Enter' unless they are part of an `st.form`. This breaks common user expectations for search interfaces.
**Action:** Wrap search inputs and their corresponding action buttons in `st.form(key="...", border=False)` to enable native Enter-to-submit behavior.

## 2025-05-15 - ARIA Roles in Streamlit
**Learning:** Streamlit's `st.markdown` with `unsafe_allow_html=True` allows for high-quality accessibility enhancements like `role="status"` and `aria-live="polite"`, which are crucial for dynamic results.
**Action:** Wrap dynamic result text in HTML elements with appropriate ARIA roles to ensure screen readers announce changes.
