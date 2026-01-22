# Carrefour-Analysis

Sistema di Trasformazione Dati Acquisti in Gestione Personale  
(Purchase Data to Personnel Management Transformation System)

## Descrizione / Description

Questo sistema trasforma i dati di acquisto di Carrefour in informazioni utili per la gestione del personale, inclusi metriche di performance dei dipendenti e requisiti di personale basati sui pattern di acquisto.

This system transforms Carrefour purchase data into personnel management insights, including employee performance metrics and staffing requirements based on purchase patterns.

## Caratteristiche / Features

- **Analisi Performance Dipendenti** / Employee Performance Analysis
  - Transazioni totali per dipendente
  - Fatturato generato
  - Valore medio transazione
  - Transazioni per ora
  - Punteggio di efficienza (0-100)

- **Requisiti di Personale** / Staffing Requirements
  - Calcolo del personale necessario per reparto e ora
  - Previsioni basate su dati storici
  - Transazioni e fatturato attesi

- **Report Completi** / Comprehensive Reports
  - Formato testo per lettura rapida
  - Formato JSON per integrazioni
  - Sommario esecutivo

## Installazione / Installation

```bash
# Clone the repository
git clone https://github.com/fronzo556/Carrefour-Analysis.git
cd Carrefour-Analysis

# Install dependencies
pip install -r requirements.txt
```

## Utilizzo / Usage

### Esecuzione Base / Basic Execution

```bash
python main.py
```

Questo comando:
1. Carica i dati di acquisto da `sample_data/purchases.csv`
2. Analizza le performance dei dipendenti
3. Calcola i requisiti di personale
4. Genera e salva report in `output/`

### Formato Dati di Input / Input Data Format

Il file CSV di input deve contenere le seguenti colonne:
- `transaction_id`: ID univoco della transazione
- `timestamp`: Data e ora (formato ISO 8601)
- `cashier_id`: ID del cassiere/dipendente
- `department`: Reparto
- `product_category`: Categoria prodotto
- `amount`: Importo in euro
- `items_count`: Numero di articoli
- `customer_id`: ID cliente (opzionale)

### Esempio di Output / Output Example

Il sistema genera due tipi di report:

1. **Report Testuale** (`personnel_report_YYYYMMDD_HHMMSS.txt`)
   - Sommario esecutivo
   - Metriche performance dipendenti
   - Requisiti di personale

2. **Report JSON** (`personnel_report_YYYYMMDD_HHMMSS.json`)
   - Struttura dati completa
   - Ideale per integrazioni con altri sistemi

## Struttura del Progetto / Project Structure

```
Carrefour-Analysis/
├── main.py                    # Applicazione principale
├── purchase_models.py         # Modelli dati acquisti
├── personnel_models.py        # Modelli gestione personale
├── transformer.py             # Logica di trasformazione
├── data_loader.py            # Caricamento dati CSV
├── report_generator.py       # Generazione report
├── requirements.txt          # Dipendenze Python
├── sample_data/
│   └── purchases.csv         # Dati di esempio
├── output/                   # Report generati (auto-creata)
└── README.md                 # Questo file
```

## Componenti Principali / Main Components

### 1. Purchase Models (`purchase_models.py`)
Definisce la struttura dei dati di acquisto.

### 2. Personnel Models (`personnel_models.py`)
Definisce le strutture dati per:
- Performance dei dipendenti
- Requisiti di personale
- Report completi

### 3. Transformer (`transformer.py`)
Contiene la logica di trasformazione:
- Calcolo metriche performance
- Analisi pattern storici
- Generazione requisiti personale

### 4. Data Loader (`data_loader.py`)
Gestisce caricamento e salvataggio dati CSV.

### 5. Report Generator (`report_generator.py`)
Genera report in formato testo e JSON.

## Metriche Calcolate / Calculated Metrics

### Punteggio Efficienza / Efficiency Score
Il punteggio di efficienza (0-100) è calcolato basandosi su:
- Transazioni per ora (fino a 50 punti)
- Valore medio transazione (fino a 50 punti)

### Requisiti Personale / Staffing Requirements
Calcolati usando la formula:
- 1 dipendente ogni 20 transazioni previste per ora
- Minimo 1 dipendente per reparto/ora

## Personalizzazione / Customization

Per utilizzare i propri dati:

1. Preparare un file CSV con il formato specificato
2. Modificare il percorso in `main.py` oppure
3. Sostituire `sample_data/purchases.csv` con i propri dati

Per aggiungere dipendenti:
```python
transformer.register_employee('CASH005', 'Nome Cognome')
```

## Requisiti / Requirements

- Python 3.8+
- pandas >= 2.0.0
- numpy >= 1.24.0
- python-dateutil >= 2.8.0

## Licenza / License

Questo progetto è open source e disponibile per uso libero.

## Autore / Author

Carrefour Analysis System - 2026