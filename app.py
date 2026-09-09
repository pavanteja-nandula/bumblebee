import os
import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Load your model (ensure hive_model.pkl is in the same folder)
MODEL_FILE = "hive_model.pkl"
model_data = joblib.load(MODEL_FILE)

model = model_data["model"]
scaler = model_data["scaler"]
features = model_data["features"]
data_ranges = model_data["data_ranges"]

# ... (include your helper functions like normalize, hive_stability, bee_activity, etc.) ...
# ... (include your predict_hive function) ...
# ... (include your gr.Blocks UI definition) ...

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
