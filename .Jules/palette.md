## 2025-05-14 - Streamlit CSS Contrast Management
**Learning:** Streamlit widgets like buttons do not automatically inherit high-contrast styles from parent containers when custom dark backgrounds are applied to the app view container. This can lead to unreadable text if not explicitly styled.
**Action:** Always target `[data-testid="stButton"] button` explicitly to set both `background-color` and `color` when overriding the global theme.
