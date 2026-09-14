import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

st.title("Data Analysis")

data = pd.read_csv(r"clean.csv")

st.subheader("Dataset")
st.dataframe(data, use_container_width=True)

st.subheader("Statistics")
st.dataframe(data.describe())

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Analysis")

# Age Distribution
fig, ax = plt.subplots()

sns.histplot(data=data, x="Age", ax=ax)

ax.set_title("Age Distribution")
ax.set_xlabel("Age")
ax.set_ylabel("Count")

st.pyplot(fig)


# Annual Income Boxplot
fig, ax = plt.subplots()

sns.boxplot(x=data["Annual_Income"], ax=ax)

ax.set_title("Annual Income")
ax.set_xlabel("Annual Income")

st.pyplot(fig)


# Purchase Car
st.subheader("Car Purchase")

st.write(data["Purchase_Car"].value_counts())
