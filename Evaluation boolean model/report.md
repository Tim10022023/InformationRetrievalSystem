# Information Retrieval Evaluation: Precision & Recall Analysis

## Introduction

In this report, we evaluate an Information Retrieval (IR) system with a focus on Precision and Recall for different queries. The system is evaluated using boolean retrieval, where documents are either retrieved or not based on the query. We focus on assessing how well the system retrieves relevant documents (Precision) and how well it captures all relevant documents (Recall).

The following queries were used to evaluate the system:

- **Query 1:** "swim and water"
- **Query 2:** "dinner or eating"

The goal of this analysis is to measure the performance of the IR system using these queries, and analyze the results in terms of Precision and Recall.

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

## Discussion

### Observations
- **Query 1 ("swim and water"):** The system retrieved 4 documents, of which 3 were relevant. This resulted in a Precision of 0.75 and a Recall of 0.6. While the Precision is decent, Recall could be improved by retrieving the missing relevant documents (`Gruensee_en.txt` and `RoterGrat_en.txt`).
  
- **Query 2 ("dinner or eating"):** The system retrieved 4 documents, all of which were relevant. This resulted in a perfect Precision of 1.0, but the Recall was slightly less than ideal (0.67) due to the missing relevant documents (`Mutoerl_en.txt` and `Wandflue_en.txt`).

### Analysis
- **Precision:** The system seems to do well in terms of Precision, especially in Query 2, where it retrieved only relevant documents. However, it still misses out on some relevant documents, which affects Recall.
  
- **Recall:** Both queries show that there is room for improvement in Recall. Specifically, Query 1 missed out on relevant documents, and Query 2 didn't retrieve all relevant documents either.

- **Boolean Retrieval:** Since the IR system is working on a boolean basis, its ability to retrieve relevant documents is limited by the presence or absence of query terms. More advanced retrieval models like ranking or probabilistic retrieval could potentially improve both Precision and Recall.

---

## Conclusion

This experiment has shown how well the IR system performs with Boolean retrieval for two specific queries. The results demonstrate the strengths and weaknesses of the system, particularly in terms of Precision and Recall. There are clear areas for improvement, especially in terms of ensuring that all relevant documents are retrieved. Future work could involve experimenting with different query formulations, retrieval models, and larger datasets.

---

## Source Code & Dataset

The code used for this experiment, as well as the dataset, can be found in the GitHub repository linked below:

- **[GitHub Repository Link]** (add your GitHub URL here)
