import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('world_smoking_history_1924_2023.csv')

st.write("## Ma'lumotlar to'plami haqida")
st.write("Ushbu loyiha 1924 yildan 2023 yilgacha bo'lgan so'nggi 100 yil ichida chekish bo'yicha global ma'lumotlarning keng qamrovli tahlilini taqdim etadi. Asosiy maqsad tarixiy tendentsiyalarni o'rganish, aholi salomatligiga ta'siri va yoshlarning chekish tendentsiyalariga alohida e'tibor berishdir. Ma'lumotlar to'plami chekish odatlari, aholi foizlari, tegishli o'limlar, sog'liqni saqlash xarajatlari, chekishga qarshi kampaniyalar, qonunchilik kuchi va boshqalar bilan bog'liq turli ko'rsatkichlarni o'z ichiga oladi.")
st.dataframe(df)

st.write("## Diagramma")
st.write("### Yillar bo'yicha dunyoda chekadiganlar soni")

tab1, tab2, tab3 = st.tabs(["Umumiy", "Jins bo'yicha", "Yoshlar"])

with tab1:
    fig, ax = plt.subplots()
    sns.lineplot(x='Year', y='Smoking_Population_Percentage', data=df, ax=ax)
    plt.xlabel('Yil')
    plt.ylabel('Chekadiganlar %')
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots()
    sns.lineplot(x='Year', y='Male_Smokers_Percentage', data=df, ax=ax, label='Erkak')
    sns.lineplot(x='Year', y='Female_Smokers_Percentage', data=df, ax=ax, label='Ayol')
    plt.xlabel('Yil')
    plt.ylabel('Chekadiganlar %')
    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots()
    sns.barplot(data=df, x='Year', y='Smoking_Population_Percentage', ax=ax, label='Umumiy', order=[i*10+1930 for i in range(10)])
    sns.barplot(data=df, x='Year', y='Youth_Smokers_Percentage', ax=ax, label='Yoshlar', order=[i*10+1930 for i in range(10)])
    plt.xlabel('Yil')
    plt.ylabel('Chekadiganlar %')
    st.pyplot(fig)

"""
Year,
Smoking Population Percentage,
Male Smokers Percentage,
Female Smokers Percentage,
Smoking Related Deaths,
Country,
City,
Age Limit,
Death History,
Average Cigarettes Per Day,
Healthcare Costs,
Anti Smoking Campaigns,
Legislation Strength,
Youth Smokers Percentage
"""