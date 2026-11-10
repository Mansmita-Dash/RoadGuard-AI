# RoadGuard AI 🚧
### Intelligent Road Damage Progression Predictor Using Fuzzy Logic

## 📌 About the Project

RoadGuard AI is a web-based prototype designed to assess road damage risk using Soft Computing techniques, particularly Fuzzy Logic.

The system evaluates different road-related factors and generates a risk score, risk category, and maintenance recommendation.

## 🎯 Objectives

- Assess road damage risk based on multiple parameters.
- Apply Fuzzy Logic to handle uncertain road conditions.
- Identify roads that may require preventive maintenance.
- Provide recommendations to support road maintenance planning.

## ⚙️ Input Parameters

The system considers:

- Road Age
- Current Road Condition
- Rainfall Intensity
- Traffic Density
- Drainage Condition
- Heavy Vehicle Frequency

## 🧠 Technology Used

- Python
- Flask
- Fuzzy Logic
- Scikit-Fuzzy
- HTML
- CSS
- JavaScript

## 🔍 Methodology

The system uses a rule-based Fuzzy Logic model.

1. Collect road-related input parameters.
2. Convert categorical inputs into numerical values.
3. Apply fuzzy membership functions.
4. Evaluate fuzzy IF-THEN rules.
5. Calculate a final risk score using fuzzy inference.
6. Classify the result as Low, Medium, or High risk.
7. Generate a maintenance recommendation.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Mansmita-Dash/RoadGuard-AI.git
```

### 2. Open the project folder

```bash
cd RoadGuard-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows)

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install flask numpy scikit-fuzzy networkx
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

```text
http://127.0.0.1:5000/
```

## 📊 Expected Output

The system displays:

- Road assessment details
- Fuzzy risk score
- Risk category
- Suggested maintenance action

## ⚠️ Project Limitations

RoadGuard AI is an experimental academic prototype. Its fuzzy rules and membership functions are based on illustrative assumptions and have not been calibrated or validated using real-world road deterioration datasets.

Therefore, its output represents an indicative risk assessment, not a scientifically validated prediction of future road damage.

## 👩‍💻 Developed By

**Mansmita Dash**

B.Tech – Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning  
Veer Surendra Sai University of Technology (VSSUT)