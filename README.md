# 🚦 Malicious URL Detection API

A Python-based machine learning service for detecting malicious URLs, built with FastAPI and LightGBM, featuring advanced feature extraction.

## Features

- Robust ML pipeline with TF-IDF and engineered URL features
- Model trained on large-scale, real-world malicious URL datasets (not included for privacy/size)
- FastAPI-powered RESTful API for easy integration and rapid predictions
- Ready for deployment, extensible for batch processing or web frontend integration
- Achieves high test accuracy (>97%) on benchmark datasets

## Setup Instructions

1. **Clone the repository:**
```
git clone https://github.com/yourusername/malicious-url-detector.git
cd malicious-url-detector
```

2. **Create and activate virtual environment:**
```
python3 -m venv venv
source venv/bin/activate
```
3. **Install dependencies:**
```
pip install -r requirements.txt
```

4. **Add your dataset (not tracked in git):**
- Place your `malicious_urls.csv` in the project root (same as README location).

5. **Train the model:**
```
python -c "from app.model import train_and_save; train_and_save('malicious_urls.csv')"
```
6. **Start the API server:**

```
uvicorn app.main:app --reload --port 8000
```

7. **Test the API:**
- Use Swagger docs [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Or curl:
  ```
  curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"url":"http://example.com"}'
  ```
## 📸 Screenshots

This section showcases key stages and outputs of the Malicious URL Detection project with actual screenshots.

---

### Model Training Output

After running the training command:

python -c "from app.model import train_and_save; train_and_save('malicious_urls.csv')"

text

you'll see detailed logs and final metrics in your terminal, showcasing the training phase and the high model performance:

![Model training and evaluation metrics](screenshots/Model-metrics.jpg)

---

### FastAPI Server Running

Start your API server with:

uvicorn app.main:app --reload --port 5500

text

This screenshot displays the FastAPI server running locally, ready to accept inference/POST requests for URL classification:

![FastAPI server running and endpoint example](screenshots/predict-url.jpg)

---

### Example API Prediction via Swagger UI

You can test the API on the interactive Swagger (OpenAPI) docs interface, available at [http://127.0.0.1:5500/docs](http://127.0.0.1:5500/docs):

- Execute a POST request on `/predict` with a JSON body containing a URL.
- Observe the predicted label type ("benign", "phishing", etc.) in the server response section.

![Swagger UI prediction result](screenshots/result.jpg)

---

These screenshots demonstrate the practical completion and successful functioning of the training workflow, API serving, and live model predictions in this project.

## Notes

- **Dataset:** Due to size, the main malicious URL dataset should NOT be committed to git. Download and place locally.
- **Trained Model:** `app/model.pkl` is produced after training; this is ignored by git.
- **Customization:** Feature extraction and model parameters are easily tweakable in `model.py`.

## License

MIT (update as appropriate)

## Author

Nulin Jeriba, [nulinjeriba25@gmail.com]




