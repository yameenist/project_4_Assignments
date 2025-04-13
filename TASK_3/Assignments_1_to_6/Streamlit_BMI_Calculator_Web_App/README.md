# ⚖️ BMI Calculator

This project is a simple BMI (Body Mass Index) calculator built using Streamlit. It allows users to input their weight and height to calculate their BMI and determine their weight classification.

## 🕹️ How It Works

1. The user enters their weight in kilograms.
2. The user enters their height in meters.
3. The program calculates the BMI using the formula:
   
   ```
   BMI = weight (kg) / (height (m) ^ 2)
   ```
   
4. The calculated BMI is displayed along with its classification:
   - **Underweight**: BMI < 18.5
   - **Normal weight**: BMI between 18.5 and 24.9
   - **Overweight**: BMI between 25 and 29.9
   - **Obesity**: BMI ≥ 30
5. The user can view a BMI classification chart for reference.
6. Users can re-enter values to perform multiple calculations.

## 📌 Example Output

```
⚖️ BMI Calculator
==================
Enter your weight (kg): 70
Enter your height (m): 1.75

Your BMI is **22.86**.
Classification: **Normal weight**.

BMI Classification Chart:
| BMI Range       | Classification  |
|-----------------|-----------------|
| < 18.5          | Underweight     |
| 18.5 - 24.9     | Normal weight   |
| 25 - 29.9       | Overweight      |
| ≥ 30            | Obesity         |
```

## 🛠️ Code Breakdown

- **User Input Handling:** Ensures users enter valid positive values for weight and height.
- **BMI Calculation:** Uses the standard BMI formula to compute the value.
- **Classification System:** Determines the weight category based on the BMI value.
- **Formatted Output:** Displays results clearly and provides a reference BMI chart.
- **Streamlit Integration:** Provides an interactive UI with buttons and input fields.

## Deployment Url : https://bmi-calculator-app-401.streamlit.app/

🎉 A great project to practice working with numerical calculations and user interaction in Python using Streamlit!

