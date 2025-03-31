# InformationRetrievalSystem for HIKING TRAILS
Natural Language Processing and Information Retrieval / 자연어처리 및 정보검색  

## **Description**  
This repository contains the **data collection** and **models** of an **Information Retrieval (IR) System**.  
The dataset consists of **hiking trail descriptions** from different countries, providing a real-world example of text-based search and retrieval.  

## **Search Models**  

### **1️⃣ Boolean Model**  
The **Boolean Model** allows searching with logical operators:  
- **AND** → Finds documents containing **all** specified words.  
- **OR** → Finds documents containing **at least one** of the specified words.  
- **NOT** → Excludes documents containing a specified word.  

✅ **Example Queries:**  
```
mountain AND lake  
forest OR river  
canyon AND waterfall NOT difficult  
```  
To use the Boolean Model, run:  
```sh
python boolean_model.py
```
Then enter a query using `AND`, `OR`, and `NOT` to filter the results.  

### **2️⃣ Vector Space Model (TF-IDF)**  
The **Vector Space Model** ranks documents based on their relevance to the query. It uses:  
- **TF-IDF (Term Frequency-Inverse Document Frequency)** to weight words by importance.  
- **Cosine Similarity** to compare the query with each document.  

✅ **Example Query:**  
```
best scenic trail with waterfall  
```  
➡️ The system returns **ranked** documents based on similarity scores.  

To use the Vector Space Model, run:  
```sh
python vector_space_model.py
```
Enter a query in **natural language**, and the system will return **ranked results**.  


This project demonstrates **two fundamental IR techniques** and allows users to search for hiking trails efficiently. 🚀  
