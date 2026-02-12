## 2025-05-15 - Streamlit CSS Specificity and Brittle Selectors
**Learning:** Custom styles for semantic elements in Streamlit (like `h1`, `p`) often require `!important` to override default themes. While using `data-testid` is sometimes necessary for layout fixes (like `stVerticalBlockBorderWrapper`), it is considered brittle by some reviewers.
**Action:** Use `!important` when styling semantic elements in Streamlit. Use `st.container(border=True)` for grouping but be cautious with deep CSS overrides on internal Streamlit classes.

## 2025-05-15 - Repository Hygiene in Streamlit
**Learning:** Running Streamlit locally creates logs and NLTK downloads data. These should be cleaned up or gitignored to avoid polluting the PR.
**Action:** Add `streamlit.log`, `__pycache__/`, and `*.png` to `.gitignore`. Clean up temporary files before submission.
