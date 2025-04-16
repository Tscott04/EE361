import firebase_admin
from firebase_admin import credentials, db
import numpy as np

cred = credentials.Certificate("firebase_service_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://touchalytics-97e7f-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')
data = ref.get()

def is_normal_vector(vector, mean, std, z_thresh=3):
    """Check if a vector is within z-score threshold for all values."""
    z_scores = np.abs((vector - mean) / std)
    return np.all(z_scores < z_thresh)

def extract_user_data(user_id, all_data):
    features = []
    user_swipes = all_data.get(str(user_id), {})

    raw_vectors = []

    # Step 1: Gather all swipe vectors first
    for swipe_id, swipe in user_swipes.items():
        if isinstance(swipe, dict):
            try:
                feature_vector = [
                    float(swipe['averageDirection']),
                    float(swipe['averageVelocity']),
                    float(swipe['directionEndToEnd']),
                    float(swipe['midStrokeArea']),
                    float(swipe['midStrokePressure']),
                    float(swipe['pairwiseVelocityPercentile']),
                    float(swipe['startX']),
                    float(swipe['startY']),
                    float(swipe['stopX']),
                    float(swipe['stopY']),
                    float(swipe['strokeDuration'])
                ]
                raw_vectors.append(feature_vector)
            except (KeyError, ValueError):
                continue

    # Step 2: Compute mean and std for z-score filtering
    if not raw_vectors:
        return []

    all_data_np = np.array(raw_vectors)
    mean = np.mean(all_data_np, axis=0)
    std = np.std(all_data_np, axis=0)

    # Step 3: Filter out abnormal data using z-score
    for vector in raw_vectors:
        vector_np = np.array(vector)
        if is_normal_vector(vector_np, mean, std):
            features.append(vector)

    return features