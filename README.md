My First AI Project: Cat vs Dog Classification

Final project for the Building AI course

Summary

This project demonstrates binary classification using a simple logistic regression model. It uses a small synthetic dataset with three numerical features (height, weight, and length) to distinguish between cats and dogs. It is an educational project, not an image recognition system.

Background

Cats and dogs are among the most common household pets. Distinguishing between these two animals provides a simple example of a binary classification problem in artificial intelligence.

The purpose of this project is to demonstrate how a basic AI model can learn from numerical data and make predictions.

The main motivations for this project are:

* Learning the basic concepts of artificial intelligence.
* Understanding binary classification.
* Exploring how numerical features can be used for predictions.
* Practicing Python programming and machine learning.
* Understanding how a simple logistic regression model works.

How is it used?

This project is designed as an educational demonstration for beginners who want to understand basic machine learning concepts.

To run the program:

1. Install Python 3 on your computer.
2. Download or clone this GitHub repository.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

python cat_dog_ai.py

The program trains a simple logistic regression model using a small synthetic dataset. It then makes a prediction using three numerical inputs: height, weight, and length.

The example prediction is:

AI Cat vs Dog Classifier
Prediction: Dog

The intended users are students, beginners, and people interested in learning about artificial intelligence and machine learning.

This program does not recognize cats or dogs from photographs. It only uses numerical data.

Data sources and AI methods

The project uses a small synthetic dataset created manually for educational purposes.

The dataset contains six training examples, each with three numerical features:

* Height
* Weight
* Length

The target labels represent two classes:

* 0 = Cat
* 1 = Dog

The machine learning method used is logistic regression, a supervised learning algorithm for binary classification.

The model uses:

* A sigmoid function to calculate prediction probabilities.
* Three numerical weights and one bias.
* A learning rate of 0.001.
* 3000 training epochs.
* Stochastic gradient descent to update the model parameters.

The program is implemented in Python and uses the built-in math library.

No external datasets or animal images are used.

Challenges

This project is a basic educational example and has several limitations:

* The dataset contains only six training examples.
* The data is synthetic and does not represent all cats and dogs.
* Only three numerical features are used.
* The model has not been evaluated on a separate test dataset.
* The model cannot recognize animals from images.
* The predictions should not be considered reliable for real-world animal classification.

An important ethical consideration is that AI systems depend on the quality and representativeness of their training data. Predictions from a very small dataset may be inaccurate or misleading.

What next?

There are several ways to improve and expand this project in the future:

* Collect a larger and more realistic dataset.
* Add more useful numerical features.
* Divide the dataset into training and testing sets.
* Evaluate the model using accuracy and other performance measures.
* Improve the training process and model performance.
* Explore image classification using a suitable image dataset and a more advanced machine learning model.

Further knowledge of Python, machine learning, data preparation, and model evaluation would help develop this project.

Acknowledgments

This project was created as a final project for the Building AI course by MinnaLearn and the University of Helsinki.

The project was inspired by the educational materials and exercises provided in the Building AI course.

The Python code and synthetic training dataset were created for this educational project. No external images or datasets were used.
