# 🧠 NewsSenseAI: Multilingual News Summarizer & Sentiment Analyzer

**NewsSenseAI** is an intelligent web application that performs end-to-end **natural language processing (NLP)** on news articles in multiple languages. It extracts content from public URLs, detects the language, generates concise summaries, performs sentiment analysis, and identifies named entities. The system also supports PDF export with multilingual font compatibility.

---

## 🔍 Key Features

- 🌐 **Multilingual Support**  
  Supports English, Hindi, Marathi, and French using spaCy and Stanza pipelines.

- 📰 **URL-Based News Extraction**  
  Fetches article text from any valid online news article URL.

- ✍️ **Text Summarization**  
  Condenses long-form news into short, coherent summaries.

- 😊 **Sentiment Analysis**  
  Identifies emotional tone (positive, neutral, negative) of the article.

- 🔍 **Named Entity Recognition (NER)**  
  Detects and classifies entities like persons, organizations, locations, and dates.

- 📄 **PDF Export**  
  Generates downloadable PDFs with localized fonts (NotoSans), preserving multilingual text integrity.

---

## ⚙️ Tech Stack

| Layer        | Technology                                |
|--------------|-------------------------------------------|
| Backend      | Python (Flask)                            |
| NLP Engines  | spaCy, Stanza                             |
| Frontend     | HTML, Bootstrap, JavaScript               |
| PDF Export   | jsPDF with NotoSans for Unicode support   |
| Deployment   | (optional) Render / Hugging Face / Heroku |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/devang404/NewsSenseAI.git
cd NewsSenseAI
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLP Models

```bash
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm

# In Python shell or in code
import stanza
stanza.download('hi')
stanza.download('mr')
```

### 5. Run the Application

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

---

## 📸 Screenshots

> _You can upload UI screenshots here once deployed to show functionality._

---

## 🧩 Folder Structure

```
NewsSenseAI/
│
├── app.py                   # Flask application
├── requirements.txt         # Python dependencies
├── static/fonts/            # NotoSans for PDF generation
├── templates/index.html     # Main HTML UI
├── nlp/                     # Summarizer & Sentiment logic
├── scraper/                 # URL-based article fetcher
├── utils/                   # Language detection, helpers
└── README.md
```

---

## 📌 Future Enhancements

- [ ] Deploy to Hugging Face or Render
- [ ] Add bias detection module
- [ ] Enable map visualization for GPE entities (Google Maps)
- [ ] Compare sentiment across multiple URLs visually
- [ ] Add charts and NER highlighting in article text

---

## 👨‍💻 Author

**Devang Nadkarni**  
B.Tech. Artificial Intelligence & Data Science (SPPU)  
📬 [LinkedIn](https://www.linkedin.com/in/devang404)  
📁 [GitHub](https://github.com/devang404)

---

## 📄 License

MIT License — feel free to use and improve.