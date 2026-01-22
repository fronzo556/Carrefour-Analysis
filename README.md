### Panoramica del Progetto
Questo progetto applica tecniche avanzate di **Data Science** e **Machine Learning** ai dati di vendita di un supermercato globale.
L'obiettivo è trasformare i dati transazionali grezzi (scontrini) in un **Sistema di Supporto Decisionale** che permetta al management di ottimizzare la gestione del personale e prevedere i flussi in cassa.

Il progetto risponde a due domande chiave:
1.  **Chi sono i clienti?** (Segmentazione tramite Clustering)
2.  **Quanto venderemo in futuro?** (Previsione tramite Random Forest)

---

#  Obiettivi Strategici
* **Analisi Temporale:** Individuare i picchi di traffico (Giorno/Ora) per ottimizzare i turni.
* **Customer Profiling:** Raggruppare i clienti in cluster comportamentali per strategie mirate.
* **Sales Forecasting:** Prevedere il fatturato giornaliero apprendendo la stagionalità complessa.

---

###  Pipeline del Progetto

#### 1️ Data Engineering & Feature Extraction
Trasformazione del dataset grezzo per estrarre informazioni strategiche.
* **Cleaning:** Standardizzazione dei dati e gestione dei valori nulli.
* **Time-Series Engineering:** Estrazione di feature temporali (`Giorno_Settimana`, `Mese`, `Trend`) fondamentali per intercettare le abitudini di acquisto cicliche.

#### 2️ Exploratory Data Analysis (EDA)
Visualizzazione dei pattern nascosti nei dati.
* **Heatmaps:** Mappatura dell'intensità del traffico per identificare le ore di punta (Codice Rosso).
* **Analisi Distribuzionale:** Studio della spesa media e dei metodi di pagamento preferiti.

#### 3️ Unsupervised Learning: Clustering (K-Means)
Utilizzo dell'algoritmo **K-Means** per segmentare la clientela in 3 gruppi distinti.
* **Risultato:** Identificazione dei **Centroidi** (i clienti "tipo") per distinguere i clienti VIP da quelli a rischio abbandono.

#### 4️ Supervised Learning: Forecasting (Random Forest)
Implementazione di un modello **Random Forest Regressor** (100 stimatori) per la previsione delle vendite.
* **Perché Random Forest?** A differenza della regressione lineare, questo modello cattura le non-linearità e la stagionalità (es. picchi del weekend e trend mensili).
* **Metriche:** Il modello è stato validato tramite R2 Score, MAE e Matrice di Confusione.

---

###  Risultati e Metriche

Il modello è stato valutato non solo scientificamente, ma anche per la sua utilità operativa:

| Metrica | Risultato | Significato Business |
| :--- | :--- | :--- |
| **R2 Score** | **> 0.85** | Il modello spiega fedelmente l'andamento del mercato. |
| **MAE** | **Basso** | L'errore medio in Euro è contenuto. |
| **Confusion Matrix** | **Alta Precisione** | Il modello distingue correttamente i giorni "Ottimi" da quelli "Sottotono". |

** Insight Operativo:**
L'analisi della **Matrice di Confusione** conferma che il modello è affidabile per il *decision making*: se l'AI prevede un giorno "Ottimo", il manager può convocare staff extra con la sicurezza di non sprecare budget.

---

###  Stack Tecnologico

* **Linguaggio:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Visualizzazione:** Seaborn, Matplotlib
* **Machine Learning:** Scikit-Learn (RandomForest, KMeans, Metrics)

---

###  Come Eseguire il Progetto
1.  Installare le dipendenze:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
2.  Posizionare il file `supermarket_sales.csv` nella cartella principale.
3.  Eseguire il Notebook Jupyter sequenzialmente.

---

