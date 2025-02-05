# 🚀 Startup Predictor

## 📌 Overview
The **Startup Predictor** is a machine learning-powered web application built with Flask that predicts the funding stage of a startup based on financial and descriptive inputs. The model behind the app leverages **XGBoost, LightGBM, and a Stacking Classifier**, ensuring a high level of predictive accuracy. This project demonstrates expertise in **machine learning model comparison, deployment, and Flask-based web applications.**

## ✨ Features
- 🌟 **User-friendly Web Interface**: Built with Flask, allowing seamless user interaction.
- 📊 **Advanced Machine Learning**: Uses a comparative approach with XGBoost, LightGBM, and Stacking Classifier.
- 🏆 **Best Model Selection**: The most effective model, after evaluation, is saved as `model.pkl` for deployment.
- 🚀 **Real-time Predictions**: Users can input their startup details and receive instant funding stage predictions.
- 🖥 **Scalable and Lightweight**: Flask ensures quick responses and easy deployment.

## 🛠 Tech Stack
- **Backend**: Flask, Python
- **Machine Learning**: XGBoost, LightGBM, Stacking Classifier, Scikit-learn
- **Data Handling**: Pandas, NumPy
- **Model Deployment**: Pickle for model serialization

## 🎯 How It Works
1. Users enter key startup information (description, debt, equity, grants).
2. The input is processed and fed into the trained model.
3. The model predicts whether the startup is **Rejected, Early Stage, or Late Stage**.
4. The result is displayed instantly on the web interface.

## 🚀 Quick Start
### 🔧 Prerequisites
- Python 3.7+
- Flask
- Scikit-learn
- Pandas
- XGBoost
- LightGBM

### ▶️ Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/oms0401/startup-predictor.git
   cd startup-predictor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open the browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## 📌 Model Training Workflow
- **Data Preprocessing**: Cleaned and structured startup funding data.
- **Feature Engineering**: Created numerical representations of startup descriptions.
- **Model Comparison**: Trained XGBoost, LightGBM, and Stacking Classifier.
- **Best Model Selection**: Evaluated models based on accuracy and performance metrics.
- **Deployment**: Saved the best model as `model.pkl` and integrated it into the Flask app.

## 📈 Performance Metrics
The best-performing model was selected based on:
- **Accuracy Score**: High precision in predicting funding stages.
- **ROC-AUC**: Evaluated model discrimination ability.
- **Confusion Matrix**: Analyzed prediction errors.

## 🎯 Future Enhancements
- 📌 **Enhanced Feature Engineering**: Extracting more meaningful insights from startup descriptions.
- 📌 **Database Integration**: Storing past predictions for trend analysis.
- 📌 **Deployment on Cloud**: Hosting on AWS/GCP for scalability.
- 📌 **Improved UI/UX**: A more interactive frontend using React or Flask templates.

## 📬 Contact
For any inquiries, reach out via:
- 📧 Email: your-email@example.com
- 💼 LinkedIn: [Your Profile](www.linkedin.com/in/om-manoj-sharma-b87b22291)
- 🏆 GitHub: [Your Repository](https://github.com/oms0401/startup-predictor)

---


