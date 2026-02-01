## 2025-02-01 - Streamlit UI Polish and Accessibility
**Learning:** Streamlit apps often require specific CSS targeting (e.g., `[data-testid="stAppViewContainer"]`) and `!important` flags to correctly override default themes. Combining nested HTML into a single `st.markdown` call prevents layout issues from Streamlit's internal wrappers.
**Action:** Use consolidated `st.markdown` calls for complex HTML structures and always include ARIA roles (`role="status"`, `aria-live="polite"`) for dynamic results.
