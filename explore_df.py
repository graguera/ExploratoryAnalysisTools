import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact, ttest_ind
from statsmodels.stats.outliers_influence import variance_inflation_factor
from pandas.api.types import CategoricalDtype

def explore_df(df: pd.DataFrame, target: str, alpha=0.05) -> str:
    markdown_output = []
    n_rows, n_cols = df.shape
    markdown_output.append(f"# Exploratory Analysis\n\n{n_rows} rows x {n_cols} columns | target = `{target}`\n")

    markdown_output.append("## Target Variable Summary\n")
    target_counts = df[target].value_counts()
    target_pct = df[target].value_counts(normalize=True) * 100
    target_summary = pd.concat([target_counts.rename("count"), target_pct.rename("%")], axis=1).round(2)
    markdown_output.append(target_summary.to_markdown())

    test_results = []

    for col in df.columns:
        if col == target:
            continue

        markdown_output.append(f"\n---\n\n## Variable: `{col}`\n")
        dtype = df[col].dtype

        is_cat = (
            isinstance(dtype, CategoricalDtype)
            or pd.api.types.is_object_dtype(dtype)
            or pd.api.types.is_bool_dtype(dtype)
            or df[col].nunique() <= 10
        )

        if is_cat:
            series = df[col].astype(object)
            ct = pd.crosstab(series, df[target])
            stat, p, _, _ = chi2_contingency(ct.values, correction=True)
            markdown_output.append(f"Chi-square test: stat = {stat:.2f}, p-value = {p:.4f}")
        else:
            grp_vals = df[target].unique()
            if len(grp_vals) == 2:
                grp0 = df.loc[df[target] == grp_vals[0], col].dropna()
                grp1 = df.loc[df[target] == grp_vals[1], col].dropna()
                tstat, p = ttest_ind(grp0, grp1, equal_var=False)
                markdown_output.append(f"T-test: t = {tstat:.2f}, p-value = {p:.4f}")

    return "\n\n".join(markdown_output)
