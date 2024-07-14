import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('world_smoking_history_1924_2023.csv')


st.write("## Ma'lumotlar to'plami haqida")
st.write("Ushbu loyiha 1924 yildan 2023 yilgacha bo'lgan so'nggi 100 yil ichida chekish bo'yicha global ma'lumotlarning keng qamrovli tahlilini taqdim etadi. Asosiy maqsad tarixiy tendentsiyalarni o'rganish, aholi salomatligiga ta'siri va yoshlarning chekish tendentsiyalariga alohida e'tibor berishdir. Ma'lumotlar to'plami chekish odatlari, aholi foizlari, tegishli o'limlar, sog'liqni saqlash xarajatlari, chekishga qarshi kampaniyalar, qonunchilik kuchi va boshqalar bilan bog'liq turli ko'rsatkichlarni o'z ichiga oladi.")
st.dataframe(df)


st.write("## Kirish")
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
Bu grafiklar orqali ko'rishimiz mumkin ki 1924 yildan 1954 yilgacha chegadifanlar soni tinmasdan oshgan va 1954 yili rekord darajadagi 55% ga teng bo'lgan. Bundan tashqari agar chekuvchilarni jins bo'yisha ajratsak erkak kishilar ayollardan har doim ko'proq bo'lganligini kuzatishimiz mumkin. Yoshlar ham nisbatan 1954 yilgacha ko'pchiligi chekarkan.

Katta o'zgarishlar 1955 yildan boshlangan. Chekuvchilar asta sekin kamayishgan. Bu tendentsiya 2008-yilgacha davom etgan va shundan keyin minimal 1% darajasida qolgan.

Biz bunaqa uzgarishlarga nima olib kelganligi o'rganib chiqishni uzimizga maqsad qildik.
"""


df = df.drop('Youth_Smokers_Percentage', axis=1).drop('Male_Smokers_Percentage', axis=1).drop('Female_Smokers_Percentage', axis=1).drop('Age_Limit', axis=1)
# Chekuvchilarni erkaklar bilan ayollar va yoshlarni ma'limotlarini ko'rib chiqdik, shuning uchun endi oddiy chekuvchilarni ma'lumotini ishlatsak bo'ladi. Yosh limiti esa xech narsaga ta'sir qilmaydi.

df_numeric = df.select_dtypes([int, float]).columns.tolist()[1:]
# Barcha (yil va tepada olib tashlaganlarimizdan tashqari) numerik columnlarni yig'voldik.

lst = [ "Chekuvchi aholi ulushi",
        "Chekish bilan bog'liq o'limlar",
        "O'lim tarixi",
        "Kuniga o'rtacha sigaret",
        "Sog'liqni saqlash xarajatlari",
        "Chekishga qarshi kampaniyalar",
        "Qonunchilik kuchi"]
# Tepadagi columnlar tarjimasi

df2 = df

for i in df_numeric:
    df2[i] = (df[i] - df[i].min()) / (df[i].max() - df[i].min())
# Scale

st.write("## Nisbatlari")

column = st.radio(
    label = "Qiziqtirgan parametrni tanlang",
    options = lst,
    index=None,
)

if st.button("Nisbatlarni ko'rsat"):
    st.write(f"### {column}")
    a = df_numeric[lst.index(column)]
    for i in df_numeric:
        if i == a:
            continue
        fig, ax = plt.subplots()
        sns.lineplot(x='Year', y=a, data=df2, ax=ax, label=column)
        sns.lineplot(x='Year', y=i, data=df2, ax=ax, label=lst[df_numeric.index(i)])
        plt.xlabel('Yil')
        plt.ylabel('')
        st.pyplot(fig)
else:
    pass

"## Hulosa"

"Ko'rib chiqilgan diogrammalardan ko'rishimiz mumkin ki chekuvchilar kamayishiga aniq bir sabab bo'lmagan ekan. Yagona yetarlik darajada ta'sir qilgan narsa bu qonunchilik kuchi. Demak chekivchilar % deyarlik tashqi ta'sirsiz uzi kamaygan deyishimiz mumkin."