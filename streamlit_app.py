import streamlit as st
import cv2

# Charger l'image depuis l'utilisateur
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Lire l'image avec OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Détection de visages avec cascade classifier
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=(30, 30))

    # Dessiner les rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

    # Afficher l'image modifiée
    st.image(img, channels="BGR")

    # Enregistrer l'image avec les visages détectés
    if st.button("Enregistrer l'image"):
        cv2.imwrite("detected_faces.jpg", img)
        st.success("Image enregistrée avec succès.")

    # Ajouter un sélecteur de couleur pour les rectangles
    color = st.color_picker("Choisissez la couleur des rectangles", "#ff6347")  # Couleur par défaut : rouge clair

    # Ajouter un curseur pour ajuster minNeighbors
    min_neighbors = st.slider("Réglage du nombre minimum de voisins", 1, 10, 3)  # Valeurs possibles de 1 à 10, valeur par défaut : 3

    # Ajouter un curseur pour ajuster scaleFactor
    scale_factor = st.slider("Réglage du facteur d'échelle", 1.1, 2.0, 1.2)  # Valeurs possibles de 1.1 à 2.0, valeur par défaut : 1.2
