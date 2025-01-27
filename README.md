# 🚗 Moroccan Car Price Prediction 📈

## 📜 Project Overview
Moroccan Vehicle Price Prediction is a data-driven project designed to predict vehicle prices in the Moroccan market. The project analyzes data scraped from Avito, leveraging machine learning and a user-friendly web application to deliver accurate price predictions for a wide range of car models and brands.


## 🎯 Key Objectives

 1. **📥 Data Extraction & Parsing:**
   - Scrape car listings from Avito using Selenium.
   - Parse and clean the HTML data using BeautifulSoup to extract relevant features (Price, Fiscal Power, Model Year, Gearbox , etc.)

 2. **🏗 Data Preparation:**
   - Clean, analyze, and preprocess the extracted data using Pandas to ensure it is ready for machine learning.

 3. **🤖 Machine Learning Model:**
   - Train a predictive model using scikit-learn to estimate car prices based on user input features.

 4. **🌐 Streamlit Web Application:**
   - Develop an interactive user interface using Streamlit.
   - Allow users to input details of any car model and receive price predictions in real-time.


## ⚙ Tech Stack :

 - **Selenium** : For extracting data from the website.
 - **BeautifulSoup**: For parsing and extracting data from HTML.
 - **Pandas** : For data analysis and cleaning.
 - **Scikit-learn** : For creating the prediction model.
 - **Streamlit** : For building the web application and deploying the model.
 - **pickle** : For saving and loading the machine learning model.


## 🚀 Getting Started :

1. Clone this repository to your local machine.
2. Install dependencies mentioned in `the requirement.txt` file.
2. Run the web application in the terminal with the following command: `streamlit run app.py`.

   #### Running the application will:

   - Execute the scraping script to collect data.
   - save the data extracted on the `data.csv` file .
   - Clean and analyze the data using the `analyse.ipynb` Notebook.
   - Train and evaluate the prediction model.
   - Save and load the model with pickel .
   - Provide the prediction result through the web application.

---

 **Note :** This project is for educational and demonstration purposes. The results may vary depending on the quality and quantity of the extracted data.

---

## 👥 Contributors
 - Soukaina El Hadifi 

## 📧 Contact
For questions or suggestions, feel free to reach out:

 - Name: El Hadifi Soukaina
 - Email: elhadifi.soukaina@gmail.com