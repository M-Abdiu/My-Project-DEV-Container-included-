# Arbeitszeit-Auswertungs Programm


This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.


## 📝 Analysis

**Problem**
Das Problem ist, dass der Vorgesetzte ein File erhält in den alle Mitarbeiter ihre gestempelten Zeiten eintragen. Er möchte eine Übersicht haben über die jeweiligen Mitarbeiter, in der gezeigt ist: Mitarbeiter, Überstunden, Minusstunden, Pensum, Einhaltung der Rahmenbedinungen und dies nicht immer manuell berechnen müssen. 


**Scenario**
Der User will eine Übersicht über die Überstunden haben, indem er das File importiert. Schlussendlich soll er als Output eine Übersicht erhalten in der aufgeführt ist:
- Mitarbeiter
- Pensum
- Anzahl Überstunden
- Anzahl Minuststunden
- Vertragliche Rahmenbedingungen eingehalten

**User stories:**
1. Als User möchte ich, eine CSV oder Excel Datei einlesen können, in der die Mitarbeiter ihre Zeitstempelungen + Pensum aufgeführt haben. 
2. Als User möchte ich, eine Übersicht der Überstunden des Mitarbeiters erhalten. 
3. Als User möchte ich, eine Übersicht der Minusstunden des Mitarbeitrs erhalten.
4. Als User möchte ich, eine Angabe der Pensums des Mitarbeiters erhalten. 
5. Als User möchte ich, eine Angabe erhalten ob die, von der Organisation gegebenen, Rahmenbedingungen eingehalten wurden.  


**Use cases:**
- Input des Files mit allen Angaben der Mitarbeiter.
- Das Programm durchlaufen lassen und die Daten sollen validiert werden. 
- Output wird als Übersichts Datei ausgegeben.

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

Der User Startet das Programm. 
Das Programm interagiert mit dem User in dem der User die CSV oder Excel Datei in das Programm einliest.
 

---


### 2. Data Validation

Das Programm muss überprüfen ob die angegebenen Daten korrekt sind:
- Ist der Mitarbeiter ein Name. 
- Sind die Timestamps korrekte Zeiten. Im richtigen Format und möglich.  
- Ist das Pensum >0 und <100.


### 3. File Processing

Das Programm liest die Daten, in dem es das Input CSV oder Excel File verwendet. 
Das Programm gibt Daten aus, in dem es die berechneten Resultate (Mitarbeiter, Überstunden, Minusstunden, Pensum, Rahmenbedinungen) in einem Output file als Übersicht ausgibt. 

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # Main Programm
├── input.csv			# Input File, mit Mitarbeiter, Pensum, Timestamps
├── output.csv			# Output FIle, mit Mitarbeiter, Überstunden, Minusstunden, Pensum, Rahmenbedinungen
└── README.md           # Projektbeschrieb und Meilensteine
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

1. Öffnen des reposotory in **GitHub Codespaces**
2. Input File in das Reposotory einfügen. 
3. Öffnen des Terminals.
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- Openpyxl für excel verarbeitung


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       		| Contribution                                 	|
|------------		|----------------------------------------------	|
| Denis Silva		|												|
| Mehmedali Abdiu 	|									            |
| Antoine Vaillant  |												|


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
