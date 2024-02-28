import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import SVC

from imblearn.over_sampling import SMOTE
# Load your dataset
df = pd.read_csv('dataset_hate_speech.csv')

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df['tweet'], df['class'], test_size=0.2, random_state=42
)

#converting data to tf-idf vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vectorized = vectorizer.fit_transform(train_data)
X_test_vectorized = vectorizer.transform(test_data)

# Display class distribution before oversampling
print("Class distribution before oversampling:")
print(pd.Series(train_labels).value_counts())

# Apply SMOTE to oversample the minority class
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_vectorized, train_labels.ravel()) # type: ignore
print(pd.Series(y_train_resampled).value_counts()) # type: ignore
# Create a pipeline with TF-IDF vectorization and SVC
model = SVC()

# Train the model
model.fit(X_train_resampled, y_train_resampled) # type: ignore

# Make predictions on the test set
predictions = model.predict(X_train_resampled) # type: ignore

# Evaluate the model
accuracy = accuracy_score(y_train_resampled, predictions)
classification_report_output = classification_report(y_train_resampled, predictions)
confusion_mat = confusion_matrix(y_train_resampled, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report_output)
print("Confusion Matrix:")
print(confusion_mat)