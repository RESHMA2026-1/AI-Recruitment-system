 ATS Scoring Engine

 Overview

The ATS Scoring Engine is designed to evaluate candidates based on multiple parameters and generate a final score.

It provides a **transparent and explainable scoring system** for recruitment.

---

 Objective

To build a candidate evaluation system that:

* Scores candidates using multiple parameters
* Uses a configurable weight system
* Generates explainable output

---

 ⚙️ Scoring Parameters

* **Skill Match** → Measures how well candidate skills match job requirements
* **Experience Relevance** → Checks relevance of past experience
* **Education Alignment** → Matches educational background
* **Semantic Similarity** → Identifies related skills (not exact match)

---

 🧠 Scoring Formula

Final Score is calculated as:

```
Final Score =
(Skill × Weight1) +
(Experience × Weight2) +
(Education × Weight3) +
(Semantic × Weight4)
```

---

## ⚖️ Weight Configuration

Weights are defined in `weights_config.py`:

```
weights = {
    "skill": 0.4,
    "experience": 0.3,
    "education": 0.1,
    "semantic": 0.2
}
```

Weights can be modified based on job role.

---

 📂 Project Structure

```
ats_scoring_engine/
│── ats_engine.py
│── weights_config.py
│── score_generator.py
│── test_engine.py
│── README.md
```

---

🔄 Workflow

1. Input candidate data
2. Extract parameter scores
3. Apply weighted formula
4. Generate final score
5. Provide explanation

---

 ▶️ How to Run

 Step 1: Activate environment

```
venv\Scripts\activate
```

 Step 2: Run the engine

```
python test_engine.py
```

---

 Output

* Final Score
* Parameter-wise breakdown
* Explainable result

---

 Example

**Input:**

```
Skill: 0.8
Experience: 0.7
Education: 0.9
Semantic: 0.75
```

**Output:**

```
Final Score: 0.78

Breakdown:
Skill: 0.8
Experience: 0.7
Education: 0.9
Semantic: 0.75
```

---

⚠️ Handling Missing Data

* Missing values are assigned default = 0
* Prevents system failure
* Ensures stable scoring

---

  Future Improvements

* Dynamic weights per job role
* Integration with resume parser
* Advanced semantic matching models

---

 👩‍💻 Author

Reshma Chandran
