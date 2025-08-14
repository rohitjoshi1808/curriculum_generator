# 📚 AI-Powered Curriculum Generator

## 📖 Overview
The **Curriculum Generator** is a Streamlit-based web application that uses **AI** to automatically generate a detailed school curriculum.  
You simply select the **school standard** and enter the **subjects**, and the app will generate a structured syllabus instantly.

This tool can be useful for:
- **Teachers** who want quick syllabus outlines.
- **School administrators** for planning academic content.
- **Parents & students** for personalized learning plans.

---

## ✨ Features
- **AI Curriculum Creation**: Generates curriculum tailored to your selected standard and subjects.
- **Interactive UI**: Simple, clean interface with form-based input.
- **Customizable**: Supports different school standards and multiple subjects.
- **Instant Output**: Generates a complete syllabus in seconds.

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Streamlit** – Web UI
- **OpenAI API** – AI syllabus generation
- **python-dotenv** – Environment variable management

---

## ⚙️ Installation

```
1️⃣ Clone the repository
bash
git clone https://github.com/your-username/curriculum-generator.git
cd curriculum-generator
2️⃣ Create & activate virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
```

### 🔧 Setup
Get your OpenAI API key from OpenAI.

Create a .env file in the root directory:

env
Copy
Edit
OPENAI_API_KEY=your_api_key_here

### ▶️ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run main.py
Steps in the App:
Select the school standard from the dropdown (e.g., Standard 1).

Enter subjects separated by commas (e.g., Math, Science, English).

Click Submit.

View your AI-generated curriculum in the text area.

### ⚙️ Configuration
You can modify:

School standards list in main.py.

AI prompt in app.py to adjust curriculum style and details.

Model name in app.py (gpt-4 or gpt-3.5-turbo).

### 🏗 Architecture
```
bash
Copy
Edit
📂 curriculum-generator
│
├── app.py            # AI logic for generating curriculum
├── main.py           # Streamlit UI for user interaction
├── .env              # API key storage (ignored in Git)
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

### 🔒 Safety & Disclaimer
The AI-generated curriculum is for reference only — verify before using in academic settings.

Your API key must be kept private and should not be committed to GitHub.

Each generation uses OpenAI API credits.

### 🚀 Future Enhancements
✅ Export curriculum to PDF or Word.

✅ Add multi-language support.

✅ Allow custom academic year planning.

✅ Integration with school ERP systems.

