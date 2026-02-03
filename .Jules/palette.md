## 2025-02-03 - Initial Streamlit Accessibility and UX Audit
**Learning:** Streamlit apps often lack proper ARIA roles for dynamic content, and default CSS can lead to low contrast when using custom dark themes on white backgrounds.
**Action:** Use `[data-testid="stAppViewContainer"]` for consistent background styling and always include `role="status"` and `aria-live="polite"` for result containers.
