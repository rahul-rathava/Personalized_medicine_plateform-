# requirements.txt

# Rasa dependencies (fixed version as per compatibility)
rasa==2.8.17
rasa-sdk==2.8.2

# Flask for backend API
flask==2.0.3

# Other required libraries
requests==2.31.0

# HTML template rendering
jinja2==3.0.3

# Optional (in case needed for VCF parsing or other extensions)
pandas==1.3.5

# --------------------------------------------------

# README.md

# Personalized Medicine Platform (Genomics Chatbot)

## 🚀 Project Overview
This project is a prototype of a **personalized medicine assistant**. It accepts **genomic files** (like `.vcf`) and provides:

- Nucleotide counts
- Variant analysis
- Disease risk insights
- Drug response predictions
- Personalized treatment recommendations
- Biomarker discovery
- Clinical data handling (via JSON)

It is integrated with a **Rasa chatbot** and a **Flask-based backend** for genomic data analysis.

---

## 📚 How It Works
1. **User chats** with the Rasa bot (e.g., "I want to analyze my genome")
2. Bot triggers `action_analyze_genome`
3. Bot sends the `sample_genome.vcf` file to the Flask server
4. Flask processes the file and returns:
   - Nucleotide stats
   - Variants detected
   - Risk insights
   - Drug responses
   - Treatment suggestions
   - Biomarkers and clinical notes
5. Bot responds with summarized results.

---

## 🚪 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚧 Run Instructions

### 1. Start Flask Backend (in `app/` folder):
```bash
cd app
python app.py
```

### 2. Start Rasa Action Server (in `rasa_bot/` folder):
```bash
cd ../rasa_bot
rasa run actions
```

### 3. Start Rasa Chatbot:
```bash
rasa shell
```

---

## 📂 Folder Structure
```
personalized_medicine_platform/
├── app/
│   ├── app.py
│   ├── sample_genome.vcf
│   └── templates/
│       └── index.html
├── rasa_bot/
│   ├── actions/
│   │   └── actions.py
│   ├── domain.yml
│   ├── data/
│   └── models/
├── requirements.txt
└── README.md
```

---

## 📊 Input/Output
### ✅ Inputs:
- `.vcf`, `.bam`, or `.fastq` files
- Clinical data (JSON)
- Natural language queries ("Analyze genome")

### 🔢 Outputs:
- Genomic variant summary
- Disease/treatment recommendations
- Pharmacogenomics insights
- Biomarker hints

---

## 🚫 Notes
- The HTML frontend does **not reflect chatbot analysis** (used for manual file uploads only).
- No live chat UI is included (not required by challenge).
- All results are generated from a test `.vcf` file inside `/app/` folder.

---

## 📍 Author
Rahul San

---

## ✅ Status
☑ Final version completed.
Ready for evaluation or demonstration.

---

## 📅 License
MIT License (open for educational/academic use).

