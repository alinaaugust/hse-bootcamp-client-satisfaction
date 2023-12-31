# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJzHKdfoypEVkU8wUtNJvSHJLf66vECw
"""

import pandas as pd
import streamlit as st
from PIL import Image
from model import open_data, preprocess_data, split_data, load_model_and_predict


def process_main_page():
    show_main_page()
    process_side_bar_inputs()

def show_main_page():
    image = Image.open('data/satisfaction-cover.jpg')

    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Clients' Satisfaction",
        page_icon=image,

    )

    st.write(
        """
        # Определяем, останется ли клиент доволен полетом.
        """
    )

    st.image(image)

def write_user_data(df):
    st.write("## Ваши данные")
    st.write(df)


def write_prediction(prediction, prediction_probas):
    st.write("## Предсказание")
    st.write(prediction)

    st.write("## Вероятность предсказания")
    st.write(prediction_probas)


def process_side_bar_inputs():
    st.sidebar.header('Заданные пользователем параметры')
    user_input_df = sidebar_input_features()

    train_df = open_data()
    train_X_df, _ = split_data(train_df)
    full_X_df = pd.concat((user_input_df, train_X_df), axis=0)
    preprocessed_X_df = preprocess_data(full_X_df, test=False)

    user_X_df = preprocessed_X_df[:1]
    write_user_data(user_X_df)

    prediction, prediction_probas = load_model_and_predict(user_X_df)
    write_prediction(prediction, prediction_probas)


def sidebar_input_features():
    sex = st.sidebar.radio("Пол", ("Мужской", "Женский"))
    age = st.sidebar.slider(
        "Возраст",
        min_value=0, max_value=100, value=0, step=1)
    customer_type = st.sidebar.radio("Лояльность клиента", ("Нет", "Да"))
    travel_type = st.sidebar.radio("Тип поездки", ("Деловая", "Личная"))
    #sclass = st.sidebar.selectbox("Класс обслуживания", (
    "Бизнес", #"Эконом плюс", "Эконом"))
    dist = st.sidebar.number_input('Дальность перелета', 1, 10000)
    departure = st.sidebar.number_input('Задержка отправления', 0, 10000)
    arrival = st.sidebar.number_input('Дальность перелета', 0, 10000)
    wifi = st.sidebar.slider(
        "Интернет на борту",
        min_value=0, max_value=5, value=0, step=1)
    time_conv = st.sidebar.slider(
        "Удобство времени прилета/вылета",
        min_value=0, max_value=5, value=0, step=1)
    booking = st.sidebar.slider(
        "Удобство онлайн-бронирования",
        min_value=0, max_value=5, value=0, step=1)
    gate = st.sidebar.slider(
        "Расположение выхода на посадку",
        min_value=0, max_value=5, value=0, step=1)
    food = st.sidebar.slider(
        "Еда и напитки на борту",
        min_value=0, max_value=5, value=0, step=1)
    boarding = st.sidebar.slider(
        "Выбор места в самолете",
        min_value=0, max_value=5, value=0, step=1)
    seat = st.sidebar.slider(
        "Комфорт сиденья",
        min_value=0, max_value=5, value=0, step=1)
    entertainment = st.sidebar.slider(
        "Развлечения на борту",
        min_value=0, max_value=5, value=0, step=1)
    onboard = st.sidebar.slider(
        "Обслуживание на борту",
        min_value=0, max_value=5, value=0, step=1)
    leg = st.sidebar.slider(
        "Место в ногах",
        min_value=0, max_value=5, value=0, step=1)
    baggage = st.sidebar.slider(
        "Обращение с багажом",
        min_value=0, max_value=5, value=0, step=1)
    checkin = st.sidebar.slider(
        "Регистрация на рейс",
        min_value=0, max_value=5, value=0, step=1)
    inflight = st.sidebar.slider(
        "Обслуживание",
        min_value=0, max_value=5, value=0, step=1)
    cleanliness = st.sidebar.slider(
        "Чистота в самолете",
        min_value=0, max_value=5, value=0, step=1)

    translation = {
        "Мужской": "Male",
        "Женский": "Female",
        "Нет": "disloyal Customer",
        "Да": "Loyal Customer",
        "Деловая": "Business travel",
        "Личная": "Personal Travel",
        "Бизнес": "Business",
        "Эконом плюс": "Eco Plus",
        "Эконом": "Eco",
    }

    data = {
        "Customer Type": translation[customer_type],
        "Gender": translation[sex],
        "Age": age,
        "Type of Travel": translation[travel_type],
        #"Class": translation[sclass],
        "Common Delay": departure + arrival,
        "Flight Distance": dist,
        "Departure Delay in Minutes": departure,
        "Arrival Delay in Minutes": arrival,
        "Inflight wifi service": wifi,
        "Departure/Arrival time convenient": time_conv,
        "Ease of Online booking": booking,
        "Gate location": gate,
        "Food and drink": food,
        "Online boarding": boarding,
        "Seat comfort": seat,
        "Inflight entertainment": entertainment,
        "On-board service": onboard,
        "Leg room service": leg,
        "Baggage handling": baggage,
        "Checkin service": checkin,
        "Inflight service": inflight,
        "Cleanliness": cleanliness,
        "Marks sum": wifi + time_conv + booking + gate + food + boarding + seat + entertainment + onboard + leg + baggage + checkin + inflight + cleanliness,
    }

    df = pd.DataFrame(data, index=[0])

    return df


if __name__ == "__main__":
    process_main_page()
