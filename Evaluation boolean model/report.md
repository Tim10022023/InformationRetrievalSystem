# Information Retrieval Evaluation: Precision & Recall Analysis

## Introduction

In this report, we evaluate an Information Retrieval (IR) system with a focus on Precision and Recall for different queries. The system is evaluated using boolean retrieval, where documents are either retrieved or not based on the query. We focus on assessing how well the system retrieves relevant documents (Precision) and how well it captures all relevant documents (Recall).

The following queries were used to evaluate the system:

- **Query 1:** "swim and water"
- **Query 2:** "dinner or eating"
- **Query 3:** "winter or snow"

The goal of this analysis is to measure the performance of the IR system using these queries and analyze the results in terms of Precision and Recall.

---

## Methodology

### Evaluation Metrics

- **Precision** is defined as the proportion of relevant documents retrieved compared to the total documents retrieved:
  
  \[
  Precision = \frac{\text{Number of relevant documents retrieved}}{\text{Total number of documents retrieved}}
  \]

- **Recall** is defined as the proportion of relevant documents retrieved compared to the total relevant documents available:

  \[
  Recall = \frac{\text{Number of relevant documents retrieved}}{\text{Total number of relevant documents}}
  \]

---

## Query 1: "swim and water"

### Documents Retrieved
The following documents were retrieved for the query "swim and water":

- **Found Documents:** 
  - `RubihornTrail_en.txt`
  - `KaiserEgg_en.txt`
  - `Murgsee_en.txt`
  - `Schafsiedel_en.txt`

### Relevant Documents
The expected relevant documents are:

- **Expected Relevant Documents:** 
  - `RubihornTrail_en.txt`
  - `Murgsee_en.txt`
  - `Schafsiedel_en.txt`

### Irrelevant Documents
The document `KaiserEgg_en.txt` is irrelevant because it includes a statement like: "So I wouldn't necessarily swim in this standing water."

### Missing Documents
The following documents were expected to be relevant but were not retrieved:

- **Missing Documents:**
  - `Gruensee_en.txt`: "Don't forget swimming trunks! Refreshing!"
  - `RoterGrat_en.txt`: "From glaciers spanning lake with swimming option."

---

### Precision & Recall for Query 1

- **Precision Calculation:**

  Precision = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total documents retrieved}} = \frac{3}{4} = 0.75\)

- **Recall Calculation:**

  Recall = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total relevant documents}} = \frac{3}{5} = 0.6\)

---

## Query 2: "dinner or eating"

### Documents Retrieved
The following documents were retrieved for the query "dinner or eating":

- **Found Documents:**
  - `ZugspitzeTrail2_en.txt`
  - `Gatterl_en.txt`
  - `Rossmad_en.txt`
  - `ZugspitzeTrail1_en.txt`

### Relevant Documents
All retrieved documents are relevant.

- **Expected Relevant Documents:**
  - `ZugspitzeTrail2_en.txt`
  - `Gatterl_en.txt`
  - `Rossmad_en.txt`
  - `ZugspitzeTrail1_en.txt`

### Irrelevant Documents
There are no irrelevant documents retrieved for this query.

### Missing Documents
The following documents were expected to be relevant but were not retrieved:

- **Missing Documents:**
  - `Mutoerl_en.txt`: "There was a very delicious kaaspress dumpling soup and then the dessert: very delicious blackberry cake."
  - `Wandflue_en.txt`: "On the terrace you can taste a warming soup, delicious Swiss cheese, or fresh rösti."

---

### Precision & Recall for Query 2

- **Precision Calculation:**

  Precision = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total documents retrieved}} = \frac{4}{4} = 1.0\)

- **Recall Calculation:**

  Recall = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total relevant documents}} = \frac{4}{6} = 0.67\)

---

## Query 3: "winter or snow"

### Documents Retrieved
The following documents were retrieved for the query "winter or snow":

- **Found Documents:** 
  - `Juifen_en.txt`
  - `Wandflue_en.txt`
  - `Pochtenfall_en.txt`
  - `Olpererhuette_en.txt`
  - `Schafsiedel_en.txt`
  - `Sonnjoch_en.txt`
  - `Hoellental_en.txt`
  - `ZugspitzeTrail1_en.txt`
  - `Aurlandsvangen_en.txt`
  - `Puehringerhuette_en.txt`
  - `Oeschinensee_en.txt`
  - `Sonntagshorn_en.txt`
  - `Lackenkogel_en.txt`
  - `Rinnenspitze_en.txt`
  - `Geissspitze_en.txt`

### Irrelevant Documents
The following documents were retrieved but are not relevant for this query:

- **Irrelevant Documents:**
  - `Pochtenfall_en.txt`: "The hut is closed in winter."
  - `Hoellental_en.txt`: "In the snow-free time, around mid-May to late October, the gorge is open 24 hours a day."
  - `Oeschinensee_en.txt`: "We still had snow and thereby there were two places where it was a little more dangerous."
  - `Lackenkogel_en.txt`: "Lackenkogel with the starting point Winterbauer."

### Missing Documents
The following documents were expected to be relevant but were not retrieved:

- **Missing Documents:**
  - `Tseuzier_en.txt`: "This artificial lake with a small island in the middle is in the center of the ski and tourist town of Crans-Montana."
  - `Cimetta_en.txt`: "Can be well connected with skis to the climb of the Madone and the departure to Mergoscia."

---

### Precision & Recall for Query 3

- **Precision Calculation:**

  Precision = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total documents retrieved}} = \frac{10}{15} = 0.67\)

- **Recall Calculation:**

  Recall = \(\frac{\text{Number of relevant documents retrieved}}{\text{Total relevant documents}} = \frac{10}{12} = 0.83\)

---

## Discussion

### Observations
- **Query 1 ("swim and water"):** The system retrieved 4 documents, 3 of which were relevant. Precision was 0.75, and Recall was 0.6. The system could be improved by retrieving the missing relevant documents.
  
- **Query 2 ("dinner or eating"):** All 4 retrieved documents were relevant, giving a Precision of 1.0, but Recall was 0.67 due to the missing relevant documents.

- **Query 3 ("winter or snow"):** Precision was 0.67 because some irrelevant documents were retrieved, but Recall was higher at 0.83 due to retrieving most of the relevant documents.

### Analysis
- **Precision:** The system is good at avoiding irrelevant documents, but some queries still result in irrelevant documents being retrieved.
  
- **Recall:** There is room for improvement in all queries, especially in ensuring that all relevant documents are retrieved. Query 3 performed well in terms of Recall, but the Precision was somewhat impacted by irrelevant results.

- **Boolean Retrieval:** The boolean retrieval model retrieves documents based on exact keyword matches, which may explain the missing relevant documents in all three queries. More advanced retrieval models, like ranking or probabilistic models, could improve both Precision and Recall.

---

## Conclusion

This experiment demonstrates the performance of the IR system using Boolean retrieval on three specific queries. While Precision was generally good, Recall could be improved, particularly in retrieving all relevant documents. Future work could explore different query formulations, retrieval models, and larger datasets to further optimize the system's performance.

---

## Source Code & Dataset

The code used for this experiment, as well as the dataset, can be found in the GitHub repository linked below:

- **[GitHub Repository Link]** (add your GitHub URL here)
