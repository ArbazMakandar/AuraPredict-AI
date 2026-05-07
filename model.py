import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("Student_Performance.csv")

# Show columns
print(data.columns)

# Features (input)
X = data[['study_hours',
          'attendance_percentage',
          'math_score',
          'science_score',
          'english_score']]

# Target (output)
y = data['overall_score']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Calculate error
error = mean_squared_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Squared Error:", error)

# Custom prediction
new_data = [[5, 90, 85, 80, 88]]

result = model.predict(new_data)

print("Predicted Overall Score:", result[0])