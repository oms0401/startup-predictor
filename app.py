import pickle
from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get form data
        about = request.form['about']
        debt = float(request.form['debt'])
        equity = float(request.form['equity'])
        grant = float(request.form['grant'])

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'about_processed': [about],
            'ARR_processed': ['Unknown'],  # Assuming ARR is unknown
            'equity_processed': [equity],
            'debt_processed': [debt],
            'grants_processed': [grant]
        })

        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction = ['Rejected', 'Early Stage', 'Late Stage'][prediction]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)