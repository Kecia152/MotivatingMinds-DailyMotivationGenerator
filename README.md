# 💬 Motivating Minds – Daily Motivation Generator

An AI-powered, beautifully designed motivation generator that gives personalized quotes based on your current emotional state and preferred tone.
made by [IBM watsonx.ai](https://www.ibm.com/products/watsonx-ai), [Hugging Face Transformers](https://huggingface.co/transformers/), and [Streamlit](https://streamlit.io/)

---
## 🌐 Live Demo-project deployed with streamlit cloud
url - https://motivatingminds-dailymotivationgenerator-9htgh75pja4clpyoghm9b.streamlit.app/
---

## Features

* Personalized motivational quotes based on mood and tone
* Sentiment analysis 
* Clean and interactive Streamlit UI
* Quote history tracking
* Secure use of environment variables
---

## Project Structure

MotivatingMinds-DailyMotivationGenerator/
🔹 main.py               # Streamlit app code
🔹 requirements.txt      # Python dependencies
🔹 .env.example          # Sample environment variable keys
🔹 .gitignore            # Git ignore configuration
🔹 README.md             # Project documentation

---

## 💠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MotivatingMinds-DailyMotivationGenerator.git
cd MotivatingMinds-DailyMotivationGenerator
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example file and add your IBM Cloud credentials:

```bash
cp .env.example .env
```

Inside `.env`:

```
WATSON_API_KEY=your_ibm_api_key
WATSON_PROJECT_ID=your_watson_project_id
```

---

## 💻 Run Locally

```bash
streamlit run location of main.py
```

App will be available at `http://localhost:8501`

---

## ☁️ Deploy to Streamlit Cloud

1. Push your project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click New app
4. Select the repo and set `main.py` as the app file
5. Under **Secrets**, paste:

```toml
WATSON_API_KEY = "your_ibm_api_key"
WATSON_PROJECT_ID = "your_watson_project_id"
```

6. Click **Deploy**

project will be live

---

## 🧪 Example Prompts

| Mood                     | Tone          | Example Quote                                            |
| ------------------------ | ------------- | -------------------------------------------------------- |
| Anxious or overwhelmed   | Gentle        | "Even storms pass — give yourself the grace to breathe." |
| Low energy / demotivated | Confident     | "Today isn’t wasted — it’s preparing you for momentum."  |
| Distracted or unfocused  | Philosophical | "The mind wanders, but intention always knows the path." |

---

## 🙌 Acknowledgements

* [IBM watsonx.ai](https://www.ibm.com/products/watsonx-ai)
* [Hugging Face Transformers](https://huggingface.co/)
* [Streamlit](https://streamlit.io/)

* Made by [Kecia](https://github.com/Kecia152)

---

## 📓 License

This project is licensed under the MIT License.
