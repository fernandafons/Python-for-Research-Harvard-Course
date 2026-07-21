# Python for Research – Harvard Course (PH526x)

This repository is a personal collection of homework assignments and case studies completed while taking [Using Python for Research by Harvard](https://courses.edx.org/courses/course-v1:HarvardX+PH526x+1T2020/course/), a Harvard course offered through edX. It progresses from core Python syntax to applied statistical learning, covering libraries such as NumPy, pandas, matplotlib, SciPy, scikit-learn, NetworkX, and Bokeh.

## Repository Structure

### `Week2/`
- **HomeWork2.py** – Introductory Python exercises covering core language fundamentals.

### `Week3/` – Text, Sequence, and Classification Case Studies
- **CaseStudy1.py** – Implements a Caesar cipher, encoding and decoding text messages by shifting letters through the alphabet.
- **translation_jpo.py** – Translates a DNA nucleotide sequence into a chain of amino acids using a codon lookup table (`dna.txt`, `protein.txt`).
- **LanguageProcessing.py** / **CaseStudy2.py** – Analyze word frequency and vocabulary richness across classic books in several languages (from the `Books/` folder) and Shakespeare's *Hamlet* (`hamlets.csv`), plotting book length vs. unique word count (`lang_plot.pdf`).
- **Classification.py** / **CaseStudy3.py** – Builds a k-nearest neighbors classifier from scratch and compares it against scikit-learn's implementation, applied to a wine-quality dataset (`data.csv`) with PCA-based visualization.

### `Week4/` – Exploratory Data Analysis & Networks
- **CaseStudy1.py** – Clusters Scotch whiskies by flavor-profile correlations and renders interactive Bokeh visualizations (`whiskies.txt`, `regions.txt`).
- **birds.py** / **cs2.py** – Explores GPS-tracking data for migratory birds, grouping speed and altitude statistics by bird and date (`bird_tracking.csv`).
- **SocialNetwork.py** / **cs3.py** – Uses NetworkX to study social network homophily (shared traits like sex, caste, religion) in Indian village survey data, plus a basic karate-club graph example.

### `Week5/` – Statistical Learning
- **cs9.py** – Compares linear/logistic regression against random forest models for predicting movie revenue and profitability (`movies_clean.csv`).
- **cs9p2.py** – Empty placeholder file.
- **last.py** – Implements simple linear regression from scratch via least-squares error minimization on synthetic data.

### `2025/`
- **agent.py** – A small Flask web app providing a chat interface to OpenAI's GPT-4 API (styled with `static/styles.css`). Requires an `OPENAI_API_KEY` environment variable — **do not hardcode API keys in this file.**

### Other files
- **Certificate.png** – Course completion certificate.
- **myplot.png** – Sample plot output from one of the exercises.
- **venv/** – Local Python virtual environment (typically excluded from version control via `.gitignore`).

## Requirements

Most scripts rely on:
numpy, pandas, matplotlib, scipy, scikit-learn, networkx, bokeh

The `2025/agent.py` web app additionally requires:
flask, openai

and a valid `OPENAI_API_KEY` environment variable.

## Running the Scripts

Most case studies can be run directly, e.g.:
```bash
python3 Week3/CaseStudy1.py
```

For the GPT-4 chat agent:
```bash
export OPENAI_API_KEY=your_key_here
python3 2025/agent.py
```
Then open `http://localhost:5000` in your browser.

**Note:** Some scripts read datasets hosted on edX (`courses.edx.org`) directly via URL, while others expect local files (e.g., `whiskies.txt`, `dna.txt`, `protein.txt`, the `Books/` folder) to be present in the working directory.