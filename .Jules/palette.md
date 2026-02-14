## 2025-05-22 - Enhancing Streamlit Accessibility with ARIA roles
**Learning:** Screen readers may not automatically announce dynamic updates in Streamlit (like sentiment analysis results). Using `st.markdown` with `role="status"` and `aria-live="polite"` ensures these updates are communicated effectively to assistive technologies.
**Action:** Always wrap dynamic result displays in semantic HTML with appropriate ARIA roles when using Streamlit.
