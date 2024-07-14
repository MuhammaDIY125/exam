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



tab1, tab2, tab3, tab4 = st.tabs(["Umumiy", "Ayollar", "Erkaklar", "Ayollar va Erkaklar"])

def chiqar(y, tpl=('', '')):
    fig, ax = plt.subplots()
    sns.lineplot(x='Year', y=y[0], data=df, ax=ax, label=tpl[0])
    sns.lineplot(x='Year', y=y[-1], data=df, ax=ax, label=tpl[-1])
    plt.xlabel('Yil')
    plt.ylabel('Chekadiganlar %')
    st.pyplot(fig)

with tab1:
    chiqar(('Smoking_Population_Percentage',))
with tab2:
    chiqar(('Male_Smokers_Percentage',))
with tab3:
    chiqar(('Female_Smokers_Percentage',))
with tab4:
    chiqar(('Male_Smokers_Percentage','Female_Smokers_Percentage'), ('Erkak', 'Ayol'))

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