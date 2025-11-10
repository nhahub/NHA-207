import pandas as pd

# gender_distribution(employeeDF)
def gender_distribution(df, show_output=True):
    gender_dist = df['gender'].round(value_counts(normalize=True) * 100, 2)
    gender_dist = gender_dist.round(2)
    if show_output:
        print("\n Gender Distribution (%):")
        for key, val in gender_dist.items():
            print(f'{key} : {val} %')
    return gender_dist