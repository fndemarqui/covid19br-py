import pandas as pd
import numpy as np

def add_epi_rates(data):
    """
    Computes epidemiological rates (incidence, lethality, and mortality)
    and adds them as new columns to a pandas DataFrame.

    Args:
        data (pd.DataFrame): A pandas DataFrame containing epidemiological data.
            It must have the columns 'accumCases', 'accumDeaths', and 'pop'.

    Returns:
        pd.DataFrame: The original DataFrame with the new rate columns added,
            or an empty DataFrame if the input is empty.
    """
    if not data.empty:
        # Avoids modifying the original DataFrame directly
        newdata = data.copy()
        newdata['incidence'] = 100000 * newdata['accumCases'] / newdata['pop']
        newdata['lethality'] = round(100 * newdata['accumDeaths'] / newdata['accumCases'], 2)
        newdata['lethality'] = newdata['lethality'].replace([np.inf, -np.inf], 0)
        newdata['lethality'] = newdata['lethality'].fillna(0)
        newdata['mortality'] = 100000 * newdata['accumDeaths'] / newdata['pop']
        return newdata
    else:
        print("No rates can be computed using the 0x0 tibble/data.frame provided.")
        return pd.DataFrame()
