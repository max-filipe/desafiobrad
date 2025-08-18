
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def main():
    #dados
    df_nps = pd.read_csv("database/customer_nps.csv")
    df_original = pd.read_csv("database/customer_original.csv")
    df_social = pd.read_csv("database/customer_social.csv")

    #visualizar
    df_nps.head()
    df_original.head()
    df_social.head()

    #informarcoes gerais
    average_nps = df_nps['NPS'].mean()
    print(f"The average NPS is: {average_nps:.2f}")

    #tratamento dados
    df_social.info()
    df_original["cpf"] = df_original['cpf'].apply(lambda x:x.replace('.','').replace('-',''))
    df_original["cpf"]=df_original["cpf"].astype(int)
    df_original.info()
    df=pd.merge(df_original,df_nps,on="cpf",how="left")
    df=pd.merge(df,df_social,on="cpf",how="left")
    colunas=["PhoneService","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","PaperlessBilling","Churn","Partner","Dependents"]
    df.head()

    #analise de dados
    churn_by_payment = df_original[df_original['Churn'] == 'Yes']['PaymentMethod'].value_counts()
    most_churn_payment_method = churn_by_payment.idxmax()
    highest_churn_count = churn_by_payment.max()
    print("Number of churned customers by Payment Method:")
    # display(churn_by_payment)
    print(f"\nThe payment method with the most churn is: {most_churn_payment_method} with {highest_churn_count} churned customers.")
    colunas_categoricas = ["InternetService", "Contract", "PaymentMethod", "gender"]
    df[colunas_categoricas] = df[colunas_categoricas].apply(lambda col: col.astype('category').cat.codes)
    df.drop("cpf",axis=1,inplace=True)
    df.head()
    corrnps = df.corr(numeric_only=True)["NPS"].sort_values(ascending=False)
    corrchurn = df.corr(numeric_only=True)["Churn"].sort_values(ascending=False)
    corrgeral = df.corr(numeric_only=True)
    not_churned_customers = merged_df[merged_df['Churn'] == 'No']
    max_tenure_no_churn = not_churned_customers['tenure'].max()
    print(f"The maximum tenure for customers with Churn = No is: {max_tenure_no_churn}")
    average_tenure_by_churn = merged_df.groupby('Churn')['tenure'].mean()
    print("Average Tenure by Churn Status:")
    # display(average_tenure_by_churn)
    not_churned_customers = merged_df[merged_df['Churn'] == 'No']
    monthly_charges_no_churn_desc = not_churned_customers['MonthlyCharges'].describe()
    print("Descriptive Statistics for Monthly Charges of Non-Churned Customers:")
    # display(monthly_charges_no_churn_desc)
    churn_by_contract = pd.crosstab(merged_df['Contract'], merged_df['Churn'])
    print("Churn counts by Contract type:")
    # display(churn_by_contract)
    churn_by_techsupport = pd.crosstab(merged_df['TechSupport'], merged_df['Churn'])
    print("Churn counts by TechSupport:")
    # display(churn_by_techsupport)
    churn_by_onlinebackup = pd.crosstab(merged_df['OnlineBackup'], merged_df['Churn'])
    print("Churn counts by OnlineBackup:")
    # display(churn_by_onlinebackup)

    #graficos
    sns.heatmap(corrnps.to_frame(),annot=True,fmt=".2f",cmap="Blues")
    sns.heatmap(corrchurn.to_frame(),annot=True,fmt=".2f",cmap="YlGnBu")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=churn_by_payment.index, y=churn_by_payment.values, hue=churn_by_payment.index, palette='viridis', legend=False)
    plt.title('Number of Churned Customers by Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of Churned Customers')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    for container in ax.containers:
        ax.bar_label(container)
    plt.figure(figsize=(8, 5))
    sns.histplot(data=not_churned_customers, x='MonthlyCharges', kde=True)
    plt.title('Distribution of Monthly Charges for Non-Churned Customers')
    plt.xlabel('Monthly Charges')
    plt.ylabel('Frequency')
    plt.show()
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=merged_df, x='Churn', y='MonthlyCharges')
    plt.title('Distribution of Monthly Charges by Churn Status')
    plt.xlabel('Churn')
    plt.ylabel('Monthly Charges')
    plt.show()
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=merged_df, x='Churn', y='tenure')
    plt.title('Distribution of Tenure by Churn Status')
    plt.xlabel('Churn')
    plt.ylabel('Tenure')
    plt.show()
    churn_by_contract.plot(kind='bar', stacked=True, figsize=(8, 6))
    plt.title('Churn by Contract Type')
    plt.xlabel('Contract Type')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.show()
    churn_by_techsupport.plot(kind='bar', stacked=True, figsize=(8, 6))
    plt.title('Churn by Tech Support')
    plt.xlabel('Tech Support')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.show()
    churn_by_onlinebackup.plot(kind='bar', stacked=True, figsize=(8, 6))
    plt.title('Churn by Online Backup')
    plt.xlabel('Online Backup')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Churn')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
