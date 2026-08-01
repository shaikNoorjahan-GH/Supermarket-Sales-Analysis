import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🛒 Supermarket Sales Analysis Dashboard")

df = pd.read_csv("../data/SuperMarket Analysis.csv")

st.subheader("Dataset Preview")

st.dataframe(df.head())

total_revenue = df["Sales"].sum()

total_customers = len(df)

best_branch = df.groupby("Branch")["Sales"].sum().idxmax()

best_product = df.groupby("Product line")["gross income"].sum().idxmax()

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

highest_month = df.groupby("Month")["Sales"].sum().idxmax()

st.header("Dashboard Summary")

st.write("### Total Revenue")
st.write(total_revenue)

st.write("### Total Customers")
st.write(total_customers)

st.write("### Best Branch")
st.write(best_branch)

st.write("### Best Product")
st.write(best_product)

st.write("### Highest Revenue Month")
st.write(highest_month)

st.header("Sales by Branch")

branch_sales = df.groupby("Branch")["Sales"].sum()

fig, ax = plt.subplots(figsize=(6,4))

branch_sales.plot(kind="bar", ax=ax)

ax.set_title("Sales by Branch")
ax.set_xlabel("Branch")
ax.set_ylabel("Total Sales")

st.pyplot(fig)

st.header("Payment Methods")

payment_method = df["Payment"].value_counts()

fig, ax = plt.subplots(figsize=(6,6))

payment_method.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")
ax.set_title("Payment Methods")

st.pyplot(fig)

st.header("Monthly Sales Trend")

monthly_sales = df.groupby("Month")["Sales"].sum()

fig, ax = plt.subplots(figsize=(8,5))

monthly_sales.plot(
    kind="line",
    marker="o",
    ax=ax
)

ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")

st.pyplot(fig)

st.header("Customer Ratings")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(df["Rating"], bins=10)

ax.set_title("Customer Ratings Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")

st.pyplot(fig)

st.header("Product Line Profit")

product_profit = df.groupby("Product line")["gross income"].sum()

fig, ax = plt.subplots(figsize=(10,5))

product_profit.plot(kind="bar", ax=ax)

ax.set_title("Profit by Product Line")
ax.set_xlabel("Product Line")
ax.set_ylabel("Gross Income")

plt.xticks(rotation=45)

st.pyplot(fig)
