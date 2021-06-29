# airquality-measurement-device
IoT-Projekt @ Fachhochschule Aachen Industrielle Produktion und Industrie 4.0

# Zusammenfassung

Für das Modul Industrielle Produktion und Industrie 4.0 des Studiengangs Industrial Engineering an der Fachhochschule Aachen wurde ein System zur Messung und Bewertung der Luftqualität in geschlossenen Räumen entwickelt. Vor dem Hintergrund der Covid-19 Pandemie dient das System zur Gewährleistung des Gesundheitsschutz und Reduzierung des Infektionsrisikos durch frühzeitige Warnung bei schlechter Luftqualität und Handlungsaufforderungen zum Lüften.

![image](https://user-images.githubusercontent.com/62206220/123784157-70627100-d8d7-11eb-9fbd-799bf865e21b.jpeg)

# Aufgabenstellung
- Suchen Sie sich eine Aufgabenstellung des Industrial Engineerings, bei der Sie eine Zeitreihenmessung benötigen
- Beschreiben Sie den Use Case mit Problemstellung und den Versuchsaufbau
- Erstellen Sie den Prototyp und führen die Messung durch; Übertragung und Darstellung der Messwerte ins Internet erforderlich
- Auswertung und Interpretation der Messreihe
- Lessons Learned

## Deliverable 1
- Problembeschreibung
- Lösungsansatz als Use-Case oder Prozessbeschreibung: Welche Sensoren wollen Sie einsetzen, um was zu messen und welche Auswertung planen Sie auf welche Art und Weise?
- Technisches Konzept – grafische Darstellung der geplanten Architektur

## Deliverable 2
- Problem und ggf. Quantifizierung des Problems
- Use-Case beschreiben mit Lösungsidee
- Umsetzung der Lösungsidee in Code/Flow Chart und Schaltbild
- Darstellung der erzeugten Informationen (Zeitreihen)
- Interpretation der Zeitreihen
- Kritische Diskussion und ggf. Ableiten von Verbesserungsideen; ggf. Anwendungsszenario im Industriellen Kontext
- Anhang: Code abbilden

# Problembeschreibung
Durch die anhaltende Coronavirus Pandemie hat der Infektionsschutz einen neuen Stellenwert erlangt. Um Infektionen mit dem SARS-CoV-2 Virus vorzubeugen sind     verschiedenste Maßnahmen umzusetzen. In geschlossenen Räumen ist dies vor allem das regelmäßige erneuern der Raumluft zur Verringerung der Aerosolbelastung.    Die Aerosolbelastung durch Covid Viren ist allerdings nicht direkt messbar. Die CO2-Konzentration kann als Qualitätsmerkmal genutzt werden, da Menschen beim Atmen CO2 und Aerosole ausstoßen. [1] Die Lüftungsdauer bis zum Erreichen einer akzeptablen Co2-Konzentration ist von diversen Einflussfaktoren wie aktuelle CO2-Konzentration, Raumgröße, Anzahl Personen sowie Innen- und Außentemperatur abhängig. Aus diesem Grund werden Faustregeln ausgesprochen die sich in Abhängigkeit vom Anwendungsfall und Jahreszeit unterscheiden [2] und mobile Anwendungen zur Berechnung der Lüftungsdauer empfohlen [3].
Aufgrund der diversen und oftmals unbekannten Einflussgrößen können die Faustregeln und Berechnungen zu falschen Ergebnissen und Handlungen führen, die in einem mangelndem Infektionsschutz münden.
    
# Lösungsansatz
Um das Problem falsch abgeleiteter Handlungen aus fehlerbehafteten Ergebnissen zu Umgehen wird ein Prototyp eines Frühwarnsystems entwickelt, dass bei schlechter Luftqualität Handlungsempfehlungen vorgibt. Das System soll Anwendung in geschlossenen Räumen wie Klassenzimmern, Büros und auch privaten Räumlichkeiten finden.

![image](https://user-images.githubusercontent.com/62206220/123765719-49e80a00-d8c6-11eb-8da1-aadc0ec09129.png)

Mit einem Luftqualitäts-Sensor wird die CO2-Konzentration in der Raumluft gemessen und regelbasiert in Echtzeit bewertet. Die Luftqualität wird über ein Ampelsystem visualisiert und bei Überschreitung eines definierten Grenzwertes wird eine Handlungsempfehlung via Benachrichtigung ausgegeben. Des Weiteren wird ein Programm zur quantitativen Bewertung, Modellbildung und graphischen Darstellung des zeitlichen Verlaufs der Luftqualität geschrieben. 

# Technisches Konzept
Der Prototyp wird nach der 5-A Architektur aufgebaut und unterteilt sich in Datenerfassung, -sicherung und -analyse sowie Modellbildung und Handlungsaufforderung.

![image](https://user-images.githubusercontent.com/62206220/123763514-2c19a580-d8c4-11eb-9bad-4adc28cb15ec.png)

# Umsetzung der Lösungsidee
Im folgendem wird die Umsetzung der Lösungsidee beschrieben. Der Prototyp unterteilt sich auf die System- und Hardwareebene. 

![image](https://user-images.githubusercontent.com/62206220/123784061-5759c000-d8d7-11eb-87c9-3c1a872df978.png)

## Systemebene

**Messsystem:** 
Das Messsystem umfasst die gesame Hardware, Datenverarbeitung und Visualisierung der Luftqualität.

**Datenübertragung:** 
Die Datenübertragung dient zur Übermittlung der Messwerte an die Cloud und wird über Wifi und MQTT realisiert.

**Cloud:** 
Die Cloud zur Speicherung der Daten in der Datenbank und weiteren Verarbeitung. Es wird der Cloud-Computing Anbieter Amazon-Web-Services (AWS) genutzt. Insbesondere die Services IoT Core, IoT Analytics und IoT SNS.

**Ausgabe:** 
Die Ausgabe umfasst das Programm zur quantitativen Bewertung und graphischen Darstellung des zeitlichen Verlaufs der Luftqualität.

## Hardwareebene
**Sensorik:** 
Es werden zwei Sensoren verwendet. Zum einen der MQ-135 Luftqualitäts-Sensor zur Messung der CO2-Konzentration. Außerdem der BME280 Temperatur, Luftfeuchtigkeit und -druck Sensor. Der BME280 Sensor dient zur Kalibrierung des MQ-135. 

**Microcontroller:** 
Als Microcontroller wird ein ESP8266 verwendet. Der Microcontroller dient zur Datenverarbeitung und -übertragung. 

**RGB LED:** 
Die RGB LED dient zur Visualisierung der Luftqualität.

## Flowchart
Der Programmablauf wird im folgenden Flussdiagramm dargestellt.
![image](https://user-images.githubusercontent.com/62206220/123785024-54ab9a80-d8d8-11eb-855c-e65ddfe68724.png)


Die Regeln zur Bewertung der Luftqualität sind in folgender Tabelle dargestellt.
![image](https://user-images.githubusercontent.com/62206220/123783435-a4896200-d8d6-11eb-8635-22f19b2113e8.png) [3]


# Ergebnisse

## Darstellung der Messwerte
Auf folgender Abbildung ist der zeitliche Verlauf der CO2-Konzentration vom 17.05. bis zum 13.06.2021 (links) und 01.06. bis zum 04.06.2021 (rechts) dargestellt.   

![image](https://user-images.githubusercontent.com/62206220/123775211-7738b600-d8ce-11eb-8a8d-e2776c73dd43.png)  

## Auswertung
Es ist zu erkennen, dass die Messwerte über den Zeitraum vom 17.05. bis zum 13.06.2021 stark schwanken und unrealistische Werte annehmen. Im Zeitraum vom 01.06. bis zum 04.06.2021 konnten realistische Werte aufgenommen werden. Der Verlauf der CO2 Konzentration zeigt den erwarteten nahezu linearen Verlauf.

## Diskussion
**Kritische Betrachtung**  
Wie bereits beschrieben sind die gemessen Werte überwiegend nicht aussagekräftig. Zwischenzeitlich konnten plausible Messwerte aufgenommen werden und die Funktion des Systems bestätigt werden. Sobald die CO2-Konzentration 1000 ppm überschritt begann die LED gelb zu leuchten. Stieg die CO2-Konzentration weiter auf über 2000ppm leuchtete die LED rot. Desweiteren wurde durch die Grenzwertüberschreitung von 2000ppm automatisiert eine E-Mail versendet. Aufgrund der schlechten Datenbasis ließ sich kein akkurates Modell bilden. 

**Verbesserungsmöglichkeiten**  
Die Problemanalyse ergab das die Ursache der schlechten Datenqualität an dem Luftqualitätssensor liegt. Eine Recherche ergab das der MH-Z19C CO2-Sensor zuverlässiger und genauer ist. Dieser Sensor ist zwar teurer, aber gewährt die Funktion und Erfüllung der Aufgabe.
Um die Nutzbarkeit des Prototypens zukünftig weiter zu verbessern sollte zusätzlich noch ein LCD Modul verbaut werden. Damit kann permanent ohne große Umwege die CO2-Konzentration in der Raumluft abgelesen werden. 
Desweiteren sollte die Einfache aktuell verbaute LED durch eine helleres Modell ausgetauscht werden. So kann auch bei hellen Tageslicht sichergestellt werden, dass die LED gesehen wird. 
Für eine langfristige Verwendung des Prototypen sollte eine Gehäuse erstellt werden. Es würde sich anbieten dieses Gehäuse aufgrund vorhandener Ressourcen im additiv zu fertigen. Eine entsprechende Konstruktion müsste noch erstellt werden.

**Learnings**
1. Programmierung in Python, SQL und Micropython
2. Datenübertragung mit MQTT
3. Nutzung von Cloud-Computing Technologien
4. Microcontroller und Sensorik
5. Datenanalyse und -visualisierung

**Lessons Learned**  
- Vor Beschaffung der einzelnen Komponenten sollte in folgenden Projekten eine intensivere Recherche erfolgen
- größeren Fokus auf das Projektmanagement
    - Projektinitalisierung:
        - Anforderungsdefinition
        - Ziele klar definieren (SMART); Inhalt- und Umfang eingrenzen  
    - Projektdurchführung & -controlling
        - Zeit- und Ressourcenplanung

**Fazit**  
Zusammenfassend lässt sich sagen, dass das Projekt ein Teilerfolg ist. Die Funktionen der Teilkomponenten werden zwar erfüllt, durch den unzuverlässigen CO2 Sensor kann der aktuelle Prototyp allerdings bisher nicht in der Praxis verwendet werden.

## Literatur
[1] AR-CoV-2   
[2] Coronavirus-BGHM-Zusatzinformationen-Lueftungsverhalten  
[3] Lueften_in_Klassenraeumen_Empfehlungen_LVR_Dezernat_12.40_Arbeitssicherheit  
