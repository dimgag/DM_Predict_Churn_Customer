import pandas as pd
import numpy as np
from sklearn.feature_selection import f_classif
from scipy import stats


def anova_test(data, target, p_value_threshold=0.05):
    """
    Perform ANOVA test for numerical features.

    H0: There is no significant difference between the means of the groups.
    H1: There is a significant difference between the means of the groups.

    Returns a DataFrame containing the results of the ANOVA test.
    The DataFrame is sorted by F-Score in descending order, indicating the strength of association.
    H0: Reject H0 if p-value < p_value_threshold, Fail to reject H0 if p-value > p_value_threshold.

    Parameters:
    :param data: pandas DataFrame containing numerical features.
    :param target: pandas Series containing the target variable.
    :param p_value_threshold: significance level (default=0.05).

    Returns:
    :return: pandas DataFrame with ANOVA test results.
    """

    X_train_num = data.select_dtypes(include=np.number)
    y_train = target

    f_stat, p_values = f_classif(X_train_num, y_train)

    ANOVA_F_table = pd.DataFrame(data = {'Numerical_Feature': X_train_num.columns.values, 'F-Score': f_stat, 'p values': p_values.round(decimals=10)})
    ANOVA_F_table.sort_values(by = ['F-Score'], ascending = False, ignore_index = True, inplace = True)
    ANOVA_F_table['H0'] = ANOVA_F_table['p values'].apply(lambda x: 'Reject H0' if x < p_value_threshold else 'Fail to reject H0')

    return ANOVA_F_table



def chi2_test(data, target, categorical_cols, p_value_threshold=0.05):
    """
    Chi-square test of independence for categorical features.

    H0: There is no association between the variables
    H1: There is an association between the variables
    
    Returns a DataFrame containing the results of the chi-square test of independence. 
    The DataFrame is sorted by p-value in ascending order, indicating the strength of association. 
    chi2_check: Reject H0 if p-value < p_value_threshold, Fail to reject H0 if p-value > p_value_threshold.

    Args:
    :param data: DataFrame
    :param target: Series
    :param categorical_cols: list of categorical columns
    :param p_value_threshold: significance level (default=0.05)

    Returns:
    :return: DataFrame
    """
    chi2_check = []
    p_value = []
    dof = []

    for i in categorical_cols:
        chi2, p, d, _ = stats.chi2_contingency(pd.crosstab(data[i], target))
        if p < p_value_threshold:
            chi2_check.append('Reject H0')
        else:
            chi2_check.append('Fail to reject H0')
        p_value.append(p)
        dof.append(d)

    chi_square_test = pd.DataFrame({'Categorical Variable': categorical_cols, 'Chi2-Test': chi2_check, 'P-Value': p_value, 'Degree of Freedom': dof})
    chi_square_test.sort_values(by='P-Value', ascending=True, inplace=True)
    chi_square_test.reset_index(drop=True, inplace=True)
    return chi_square_test




def t_test(data, target, alternative='two-sided', p_value_threshold=0.05):
    """
    Independent samples t-test for numerical features.
    H0: There is no significant difference between the means of the two groups.
    H1: There is a significant difference between the means of the two groups.
    Returns a DataFrame containing the results of the t-test.
    The DataFrame is sorted by t-statistic in descending order, indicating the strength of association.
    H0: Reject H0 if p-value < p_value_threshold, Fail to reject H0 if p-value > p_value_threshold.

    Parameters:
    :param data: pandas DataFrame containing numerical features.
    :param target: pandas Series containing the binary target variable.
    :param alternative: {'two-sided', 'less', 'greater'}, the alternative hypothesis for the test (default='two-sided').
    :param p_value_threshold: significance level (default=0.05).

    Returns:
    :return: pandas DataFrame with t-test results.
    """
    group1 = data[target == 0]
    group2 = data[target == 1]

    t_stat, p_value = stats.ttest_ind(group1, group2, alternative=alternative)

    t_test_results = pd.DataFrame(data={'Numerical_Feature': data.columns.values, 't-Statistic': t_stat, 'p values': p_value.round(decimals=10)})
    t_test_results.sort_values(by=['t-Statistic'], ascending=False, ignore_index=True, inplace=True)
    t_test_results['H0'] = t_test_results['p values'].apply(lambda x: 'Reject H0' if x < p_value_threshold else 'Fail to reject H0')

    return t_test_results
