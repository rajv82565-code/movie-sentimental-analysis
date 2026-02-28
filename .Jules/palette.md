## 2025-02-28 - [Accessibility in Custom Streamlit UI]
**Learning:** When using `st.markdown` with `unsafe_allow_html=True` to create custom UI elements (like cards or status regions), standard Streamlit widgets inside them might not automatically inherit accessibility properties. Manual inclusion of `role="status"` and `aria-live` is necessary for dynamic result areas to be screen-reader accessible.
**Action:** Always wrap dynamic output sections in a `<div role="status" aria-live="polite">` when they are updated via user interaction in Streamlit.

## 2025-02-28 - [Repository Hygiene]
**Learning:** Streamlit and Python development often generate temporary artifacts like `__pycache__` and execution logs (e.g., `streamlit.log`). These must be explicitly excluded or removed before submission to maintain a clean repository.
**Action:** Verify and remove all build artifacts and log files before calling the submit tool.
