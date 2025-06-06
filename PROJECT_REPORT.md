
# 🧠 Heart Stroke Prediction Project Report

## 📌 Project Overview

The goal of this project was to develop an end-to-end **Machine Learning (ML) pipeline** to predict the risk of heart stroke based on a patient's demographic and health-related information.

This involved:
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Model deployment as an interactive web app using **Streamlit**

## 🎯 Objectives

✅ Build an ML model to predict **stroke risk**  
✅ Achieve **high accuracy and ROC-AUC**  
✅ Deploy the model for easy access via **Streamlit web app**  
✅ Provide **instant feedback** to healthcare professionals and users

## 🗃️ Dataset

The project used a **public heart stroke dataset**.  
The dataset included the following features:

- Gender
- Age
- Hypertension status
- Heart disease status
- Ever married
- Work type
- Residence type
- Smoking status
- Average glucose level
- BMI

**Target variable**: `stroke` (binary: 0 = no stroke, 1 = stroke)

## 🔍 Exploratory Data Analysis (EDA)

- Missing values were identified and handled.
- Class imbalance was observed — only a small % of patients had strokes.
- Various visualizations were used to explore the relationships between features and stroke risk.

## 🛠️ Data Preprocessing

- Categorical variables were **one-hot encoded**:
    - Gender
    - Ever married
    - Work type
    - Residence type
    - Smoking status
- Numerical variables were **scaled** where appropriate.
- Final feature vector prepared for model training.

## 🤖 Model Building

**Algorithm used**: **XGBoost Classifier**

- Chosen for its its excellent performance on classification tasks.
- Handles imbalance, feature importance, and nonlinear relationships well.

**Training & Validation**:
- **Cross-validation** used to ensure robustness.
- Performance metrics computed on validation set.

## 📈 Model Performance

**Metrics**:

- **Accuracy**: ~98%  
- **ROC-AUC Score**: ~0.98  
- High precision and recall were achieved.
- The model demonstrated strong generalization on unseen data.

*Interpretation*: The model can reliably distinguish between high-risk and low-risk stroke patients.

## 🚀 Deployment

The trained model was deployed using a **Streamlit** web app:

- User-friendly UI
- Allows users to enter patient details via dropdowns and sliders
- Predicts the stroke risk and displays:
    - Classification result (High risk / Low risk)
    - Probability score

## 📊 Streamlit App Features

- Gender selection  
- Age slider  
- Hypertension and heart disease selectors  
- Ever married status  
- Work type selection  
- Residence type selection  
- Smoking status selection  
- Average glucose level slider  
- BMI slider  

**Prediction output**:
- Classification (High risk / Low risk)
- Probability score

## 📌 Final Project Architecture

```
Heart_Stroke_Prediction.ipynb  -->  model training and saving (.pkl)
                    |
                    V
        xgboost_stroke_model.pkl
                    |
                    V
              Streamlit app
             (app_py.py file)
                    |
                    V
            Deployed Web App
```

## 🔮 Possible Future Improvements

- Further hyperparameter optimization (GridSearchCV)
- Add model explainability (SHAP values)
- Address class imbalance using advanced techniques (SMOTE, Focal Loss)
- More advanced UI features (user authentication, saving results)
- Responsive design for mobile use

## 🎓 Summary

✅ Successfully built an end-to-end ML pipeline for stroke prediction  
✅ Achieved **high model performance** (~98% accuracy, ROC-AUC ~98%)  
✅ Deployed the model as an **interactive web app**  
✅ Demonstrated full ML lifecycle from EDA to Deployment

## Skills Demonstrated

- Python programming  
- Data preprocessing and feature engineering  
- Model building with **XGBoost**  
- Evaluation with cross-validation and ROC-AUC  
- Deployment using **Streamlit**  
- End-to-end ML pipeline development  
- Healthcare application of ML  

## Conclusion

This project serves as a proof-of-concept for using **Machine Learning** to assist healthcare professionals in identifying patients at risk of stroke.  
The deployed app provides an easy-to-use interface and enables practical application of the model's predictions.
