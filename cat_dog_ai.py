import math

# Simple educational AI model
# Cat vs Dog Classification

training_data = [
    ([25, 4, 40], 0),
    ([23, 3, 38], 0),
    ([30, 5, 45], 0),
    ([60, 25, 90], 1),
    ([65, 30, 100], 1),
    ([55, 20, 85], 1)
]

weights = [0.0, 0.0, 0.0]
bias = 0.0
learning_rate = 0.001

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Train the model
for epoch in range(3000):
    for features, label in training_data:
        features = [x / 100 for x in features]

        z = sum(w * x for w, x in zip(weights, features)) + bias
        prediction = sigmoid(z)
        error = prediction - label

        for i in range(3):
            weights[i] -= learning_rate * error * features[i]

        bias -= learning_rate * error

# Make a prediction
def predict(height, weight, length):
    features = [height / 100, weight / 100, length / 100]
    z = sum(w * x for w, x in zip(weights, features)) + bias
    result = sigmoid(z)

    if result >= 0.5:
        return "Dog"
    else:
        return "Cat"

print("AI Cat vs Dog Classifier")
print("Prediction:", predict(60, 25, 90))
