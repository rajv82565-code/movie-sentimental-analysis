## 2025-05-14 - Accessible Dynamic Results in Streamlit
**Learning:** Manual HTML div wrappers for aria-live in Streamlit often break because the browser auto-closes the opening tag before Streamlit inserts subsequent elements into the DOM.
**Action:** Use a single st.markdown call to render the text with role="status" and aria-live="polite", or place it on specific text elements that are updated.

## 2025-05-14 - Streamlit Card Pattern
**Learning:** Using st.container(border=True) and targeting [data-testid="stVerticalBlockBorderWrapper"] is the most reliable way to create card-like groupings that respect the Streamlit layout engine.
**Action:** Avoid manual <div class='card'> wrappers and use native containers with CSS overrides instead.
