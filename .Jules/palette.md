## 2025-05-22 - Streamlit Accessibility and Diff Constraints
**Learning:** Adding ARIA labels and roles to Streamlit-generated HTML via `st.markdown` significantly improves screen reader support. However, structural refactors like wrapping logic in `st.form` or `st.container` cause large indentation changes that can easily exceed micro-UX line count limits (50 lines).
**Action:** Use surgical `st.markdown` replacements for accessibility and localized parameter updates (like `placeholder` or `help`) to keep diffs small and focused while still providing high-impact UX improvements.
