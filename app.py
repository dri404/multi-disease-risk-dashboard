from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "⚠️ High Risk Detected"
        else:
            result = "✅ Low Risk"

        return render_template('index.html', prediction_text=result)

    except:
        return render_template('index.html', prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)
