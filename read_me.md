# K-Nearest Neighbors

KNN (K-Nearest Neighbors) is a supervised learning algorithm used for both classification and regression problems.
It’s called a lazy learner because it doesn’t learn a model during training — instead, it stores all data and makes predictions by comparing new data to stored examples.

Basic Idea

1. When a new data point comes in:
2. Compute its distance from all other points.
3. Pick the K nearest neighbors.

- For classification:
→ Majority vote among neighbors.
- For regression:
→ Average of neighbors’ values.

### Problem Statement: Car Purchase Prediction using KNN
📖 Background

A car dealership company wants to better understand their customers to improve targeted marketing and sales.
They have collected data about customers — including Name, Age, Annual Income, and whether they purchased a car or not in the past year.

The company believes that customers with similar age and income profiles often exhibit similar purchasing behavior.

To leverage this insight, you are asked to develop a K-Nearest Neighbors (KNN) classification model that predicts whether a new customer is likely to purchase a car