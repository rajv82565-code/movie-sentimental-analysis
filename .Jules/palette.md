## 2025-05-14 - Streamlit CSS Scoping and Contrast
**Learning:** Custom styled HTML elements within `st.markdown` (e.g., using `<h3>` or `<p>`) can lose theme-aware text coloring, leading to accessibility issues like unreadable text against dark backgrounds.
**Action:** Always wrap dynamic HTML content in a specific class (e.g., `.results-container`) and apply targeted CSS rules (e.g., `.results-container p { color: #ffffff !important; }`) to ensure contrast without affecting the rest of the app's components.
