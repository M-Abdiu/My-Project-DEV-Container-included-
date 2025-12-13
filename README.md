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

Das Problem ist, dass der Vorgesetzte ein File erhält in dem alle Mitarbeiter ihre gestempelten Zeiten eintragen. Er muss immer manuell berechnen, wie lange die Mitarbeiter gearbeitet haben und schauen, ob sie die vertraglichen Rahmenbedingungen nicht verletzt haben. Er möchte eine Übersicht haben über die jeweiligen Mitarbeiter, in der gezeigt ist: Mitarbeiter, Pensum, Ist-Zeit, Zoll-Zeit, Differenz-Stunden, Einhaltung der Rahmenbedinungen und Falls verletzt, Welche Rahmenbedingung verletzt wurde und dies nicht immer manuell berechnen müssen. 


**Scenario**
Der User will eine Übersicht über die Überstunden haben, indem ein File importiert, welches die wöchentliche Stemplungen der Mitarbeiter beinhaltet. Schlussendlich soll er als Output eine Übersicht erhalten in der aufgeführt ist:
- Nachname, Vorname, Pensum
- Effektivstunden
- Soll-Stunden
- Differenz-zeit
- Pausen-Stunden
- Vertragsbedingungen eingehalten?
- Begründung der Vertrags-Verletzung


**User stories:**
1. Als User möchte ich, eine CSV-Datei einlesen können, in der die Mitarbeiter ihre Zeitstempelungen für diese Woche + ihr Pensum aufgeführt haben.
2. Als User möchte ich, eine Übersicht der Überstunden jedes einzelnen Mitarbeiters erhalten.
3. Als User möchte ich, eine Übersicht der Minusstunden jedes einzelnen Mitarbeiters erhalten.
4. Als User möchte ich, eine Angabe des Pensums des Mitarbeiters erhalten.
5. Als User möchte ich, die Arbeitszeiteinhaltung an dem Pensum angepasst des Mitarbeiters erhalten. (Max 48h = 100%)
6. Als User möchte ich, eine Angabe erhalten ob die vertraglichen Rahmenbedingungen eingehalten wurden.
7. Als User möchte ich, eine Angabe kriegen wenn eine Rahmenbedingung nicht eingehalten wurde und eine Begründung, welche nicht eingehalten wurde.

**Use cases:**
- Input des Files mit allen Angaben der Mitarbeiter eingeben.
- Das Programm durchlaufen lassen und die Daten sollen validiert werden. 
- Output wird als Übersichtsausgabe in der Konsole ausgegeben.

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

Der User Startet das Programm. 
Das Programm interagiert mit dem User in dem der User die CSV-File in das Programm einliest.
 

---


### 2. Data Validation

Das Programm muss überprüfen ob die angegebenen Daten korrekt sind:
- Ist der Mitarbeiter ein Name. 
- Sind die Timestamps korrekte Zeiten. Im richtigen Format und überhaupt möglich.  
- Ist das Pensum >0 und <100.
- Ist die maximal Arbeitszeit am Pensum angepasst und validiert mit dieser die Arbeitsstunden


### 3. File Processing

Das Programm liest die Daten, in dem es das Input CSV-File verwendet. 
Das Programm gibt Daten aus, in dem es die berechneten Resultate (Mitarbeiter, Überstunden, Minusstunden, Pensum, Rahmenbedinungen) in einem Output in der Konsole als Übersicht ausgibt. 

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces

### 📂 Repository Structure
```text
My-Project-DEV-Container-included-/
├── Data\Stempelzeiten KW_XX.csv		# Input File, mit Mitarbeiter, Pensum, Timestamps
├── Filehandling.py						# Verarbeitung der Daten und Output Generierung
└── README.md          	 				# Projektbeschrieb und Meilensteine
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 FileHandling.py
	```

1. Öffnen des reposotory in **GitHub Codespaces**
2. Input File in das Reposotory einfügen. 
3. Öffnen des Terminals.
3. Run:
	```bash
	python3 FileHandling.py
	```

### Libraries Used

- CSV für CSV Verarbeitung


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       		| Contribution                                 			  |
|------------		|-----------------------------------------------------|
| Denis Silva		|Stundenberechnung und Validierung, Rahmenbedingungen	|
| Mehmedali Abdiu 	|CSV Einlesung und Validierung						 	      |



## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
