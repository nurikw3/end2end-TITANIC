

# 🚢 End2End-Titanic

![Preview](preview.jpg)

**End2End-Titanic** — full **end-to-end machine learning project** predicting Titanic survival.
Includes **model training, API, frontend (Streamlit), saved model (`.pkl`)**, and **Docker support**.

---

## ✨ Features

* 🧩 **Complete ML pipeline**: preprocessing → model → inference.
* 📦 **Trained model** saved as `model.pkl`.
* 🌐 **REST API** for predictions with FastAPI.
* 🖥 **Interactive Streamlit frontend**.
* 🐳 **Dockerized** for easy deployment.
* 🔄 **Request counter & health check** for monitoring.

---

## ⚙️ Installation

```bash
git clone https://github.com/username/end2end-titanic.git
cd end2end-titanic
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1️⃣ Run API

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 4000
```

* **Health check:** `GET /health` → `{"status":"OK"}`
* **Request stats:** `GET /stats` → `{"request_count": 0}`
* **Predict survival:** `POST /predict_model` with JSON:

```json
{
  "Pclass": 3,
  "Sex": 1,
  "Age": 22,
  "Fare": 7.25
}
```

Response:

```json
{
  "prediction": "Not Survived"
}
```

---

### 2️⃣ Run Frontend (Streamlit)

```bash
streamlit run app.py
```

* Enter passenger features in the sidebar.
* Get **real-time survival predictions**.

---

### 3️⃣ Run with Docker

```bash
docker build -t end2end-titanic .
docker run -p 4000:4000 end2end-titanic
```

* API will be accessible at `http://localhost:4000`.
* Streamlit frontend can also be exposed via Docker if configured in the Dockerfile.

---

## 🗂 Project Structure

```
end2end-titanic/
│
├─ app.py               # Streamlit frontend
├─ api.py               # FastAPI backend
├─ model.pkl            # Trained ML model
├─ Dockerfile           # Docker configuration
├─ requirements.txt
├─ preview.jpg          # Project preview image
└─ README.md
```

## 💡 Notes

* 🔄 Full end-to-end pipeline from input → prediction.
* ⚡ API includes **health** and **request stats** endpoints.
* 🐳 Docker support allows **easy deployment** anywhere.
* 🖥 Streamlit frontend allows interactive testing without API calls.
