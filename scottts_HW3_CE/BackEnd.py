
from FrontEnd import data, extract_user_data
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os

def train_all_user_models(data, model_dir="models"):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    for user_id in data.keys():
        print(f"Training model for user {user_id}")
        user_data = extract_user_data(user_id, data)
        if len(user_data) < 5:
            print(f"Skipping user {user_id} due to insufficient data.")
            continue

        unauth_data = []
        for other_id in data.keys():
            if other_id != user_id:
                unauth_data.extend(extract_user_data(other_id, data))

        if len(unauth_data) < 5:
            print(f"Skipping user {user_id} due to insufficient negative samples.")
            continue

        X = user_data + unauth_data
        y = [1] * len(user_data) + [0] * len(unauth_data)

        X = np.array(X)
        y = np.array(y)

        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(X_train, y_train)

        joblib.dump(model, os.path.join(model_dir, f"knn_model_{user_id}.pkl"))
        print(f"Model for user {user_id} trained and saved.")

if __name__ == "__main__":
    train_all_user_models(data)
