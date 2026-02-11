## 2025-05-14 - [Streamlit Card Layout & Styling]
**Learning:** Manual HTML <div> tags split across st.markdown calls in Streamlit result in broken layouts as the browser/Streamlit closes tags prematurely. Using st.container(border=True) and targeting [data-testid="stVerticalBlockBorderWrapper"] with CSS is the robust way to create cards that correctly wrap widgets.
**Action:** Always prefer st.container(border=True) for grouping elements and use specific data-testid selectors for custom styling.

## 2025-05-14 - [Accessibility in Streamlit Results]
**Learning:** Dynamic results in Streamlit (like sentiment analysis) are not automatically announced by screen readers.
**Action:** Wrap result text in a div with role="status" and aria-live="polite" within st.markdown(..., unsafe_allow_html=True).
