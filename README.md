🧠 Heart Stroke Prediction App
An end-to-end machine learning project to predict stroke risk based on patient data.
Built with an XGBoost classifier (~98% ROC-AUC), and deployed as an interactive web app using Streamlit.

This project demonstrates the complete ML workflow — from data preprocessing to model deployment.

🚀 Demo
👉 Deployed App: [https://hmuissl9cvjhpfvyrndmnj.streamlit.app/e]
👉 GitHub Repo: [https://github.com/Abishekkk0109/Heart-Stroke-Prediction-]

🏆 Project Highlights
✅ Built an XGBoost model for stroke risk prediction
✅ Achieved ~98% ROC-AUC with cross-validation
✅ Designed an intuitive Streamlit app for healthcare users
✅ Interactive input fields with instant predictions
✅ Full ML lifecycle: data preprocessing → model training → deployment

📊 Features Used
Gender

Age

Hypertension status

Heart disease status

Ever married status

Work type

Residence type

Smoking status

Average glucose level

BMI

⚙️ Tech Stack
Language: Python

ML Algorithm: XGBoost Classifier

Libraries: Pandas, Numpy, Scikit-learn, XGBoost

App Deployment: Streamlit

🗂️ Project Structure
├── Heart_Stroke_Prediction.ipynb    # Jupyter notebook with EDA, preprocessing, model building
├── app_py.py                        # Streamlit app code
├── xgboost_stroke_model.pkl         # Trained XGBoost model
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
💻 How to Run Locally
1️⃣ Clone this repo:

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2️⃣ Install dependencies:

pip install -r requirements.txt
3️⃣ Run the Streamlit app:

streamlit run app_py.py
🚀 Model Performance
Model used: XGBoost Classifier

Cross-validated ROC-AUC: ~0.98

Optimized for both recall and precision

Pre-trained model saved and used in the Streamlit app

🌐 Deployment
Deployed using Streamlit Cloud

App is lightweight and fast — accessible to both technical and non-technical users

Designed to be used in clinical settings or educational demonstrations

🔮 Possible Future Improvements
Hyperparameter tuning for even better performance

Add more patient features (exercise, alcohol intake, family history, medications)

Include SHAP explainability in the app

Add user authentication

Improve front-end UI styling

📚 Acknowledgments
Public heart stroke dataset

Inspired by healthcare applications of ML

Libraries used: Pandas, Numpy, Scikit-learn, XGBoost, Streamlit

📄 License
This project is open-source. You are free to use, modify, and share it — educational or non-commercial use is highly encouraged!

