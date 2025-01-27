import streamlit as st
import pickle
import pandas as pd
from scrap import scrape_vehicle_data

st.title("Predict Vehicle Price")

vehicle_name = st.text_input("Enter Vehicle Name or Model", "")

st.header("Enter Vehicle Characteristics")

# User inputs for vehicle characteristics
puissance = st.number_input("Puissance fiscale", min_value=0, step=1)
AnneeModele = st.number_input("Annee Modele", min_value=1900, step=1)
Kilométrage_max = st.number_input("Kilométrage_max", min_value=0, step=1)

etat = st.radio("L'état de votre véhicule?", ["Correct", "Bon", "Très bon", "Excellent", "Neuf"])

carburant = st.radio("Diesel ou Essence?", ["Diesel", "Essence", "Electrique", "Hybride"])

boite = st.radio("Automatique ou Manuelle?", ["Automatique", "Manuelle"])

Main = st.radio("Première main?", ["oui", "non"])

# Button to trigger prediction
if st.button("Calculate"):
    # Process inputs for prediction
    Diesel =True if carburant == "Diesel" else False
    Essence =True if carburant == "Essence" else False
    Hybride =True if carburant == "Hybride" else False
    Electrique =True if carburant == "Electrique" else False
    Premiere_main = True if Main == "oui" else False
    
    Manuelle = True if boite == "Manuelle" else False 
    Automatique = True if boite == "Automatique" else False

    # Condition of the vehicle
    Bon = True if etat == "Bon" else False
    Correct = True if etat == "Correct" else False
    Excellent = True if etat == "Excellent" else False
    Tres_bon = True if etat == "Très bon" else False
    Neuf = True if etat == "Neuf" else False
    
    # Create URL-compatible vehicle name
    vehicle_name_url = vehicle_name.replace(" ", "-").lower()

    # Call the scraping function (this will scrape the website using the vehicle name)
    if vehicle_name:
        scrape_result = scrape_vehicle_data(vehicle_name_url)  # Perform the scraping

    # Create DataFrame for the model
    df = pd.DataFrame({
        'Puissance fiscale': [puissance],
        'AnneeModele': [AnneeModele],
        'Première main': [Premiere_main],
        'Manuelle': [Manuelle],
        'Automatique':[Automatique],
        'Bon': [Bon],
        'Neuf': [Neuf],
        'Correct': [Correct],
        'Excellent': [Excellent],
        'Très bon': [Tres_bon],
        'Diesel': [Diesel],
        'Essence' : [Essence],
        'Hybride' : [Hybride],
        'Electrique' : [Electrique],
        'Kilométrage_max': [Kilométrage_max]
    })

    notebook_path = "./analyse.ipynb"
    import papermill as pm
    pm.execute_notebook(notebook_path, notebook_path)

    with open('modele.pkl', 'rb') as file:
        model = pickle.load(file)

    # Predict the price
    df = df[model.feature_names_in_]
    result = model.best_estimator_.predict(df)
    result = round(float(result[0]), 2)  

    # Display the price prediction result
    st.success(f"Predicted Price: {result} DH")







