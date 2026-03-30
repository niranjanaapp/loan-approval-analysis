import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/loan_data.csv")

df.columns = df.columns.str.strip()

print(df['loan_status'].value_counts())

df['loan_status'].value_counts().plot(kind='bar')
plt.title("Loan Approval Count")
plt.xlabel("Status")
plt.ylabel("Count")

plt.savefig("loan_status_chart.png")  # <-- add this line
plt.show()
