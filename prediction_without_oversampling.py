import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
import joblib
# Load your dataset
df = pd.read_csv('dataset_hate_speech.csv')

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df['tweet'], df['class'], test_size=0.2, random_state=42
)


# Create a pipeline with TF-IDF vectorization and SVC
model = make_pipeline(TfidfVectorizer(), SVC())

# Train the model
model.fit(train_data, train_labels)

# Make predictions on the test set
predictions = model.predict(test_data)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
classification_report_output = classification_report(test_labels, predictions)
confusion_mat = confusion_matrix(test_labels, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report_output)
print("Confusion Matrix:")
print(confusion_mat)

# for heatmap 
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

joblib.dump(model,'hate_speech_model.joblib')