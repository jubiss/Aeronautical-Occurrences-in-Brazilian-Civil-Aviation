import matplotlib.pyplot as plt
def plot_null_percentages(df, title=None):
    null_percentages = df.isnull().sum() / len(df) * 100
    null_percentages = null_percentages[null_percentages > 0]
    null_percentages.sort_values(inplace=True)
    plt.figure(figsize=(10, len(null_percentages) / 2))
    plt.barh(null_percentages.index, null_percentages.values)
    plt.xlabel("Percentage of null values")
    if title == None:
        plt.title("Percentage of null values by column")
    else:
        plt.title(title)
    plt.show()