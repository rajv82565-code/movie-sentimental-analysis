## 2025-05-14 - [Streamlit Search Interaction]
**Learning:** In Streamlit, native text inputs do not trigger an action on "Enter" unless wrapped in an `st.form`. This is a common usability gap for users accustomed to standard web search behavior.
**Action:** Always wrap search inputs and their corresponding action buttons in `st.form(key='...', border=False)` and use `st.form_submit_button` to enable "Enter to submit" functionality.

## 2025-05-14 - [Repository Hygiene for Python]
**Learning:** Running Streamlit apps and Python scripts locally generates `__pycache__`, `.pyc` files, and often custom log files (e.g., `streamlit.log`). These artifacts clutter the repository and can cause environment conflicts.
**Action:** Before submitting, explicitly remove all build artifacts, cache directories, and temporary log/screenshot files created during development and verification.
