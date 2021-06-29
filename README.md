# airquality-measurement-device
IoT-Projekt @ Fachhochschule Aachen Industrielle Produktion und Industrie 4.0

# Aufgabenstellung

- Suchen Sie sich eine Aufgabenstellung des Industrial Engineerings, bei der Sie eine Zeitreihenmessung benötigen
- Beschreiben Sie den Use Case mit Problemstellung und den Versuchsaufbau
- Erstellen Sie den Prototyp und führen die Messung durch; Übertragung und Darstellung der Messwerte ins Internet erforderlich
- Auswertung und Interpretation der Messreihe
- Lessons Learned

# Deliverable 1

## Problembeschreibung
Durch die anhaltende Coronavirus Pandemie hat der Infektionsschutz einen neuen Stellenwert erlangt. Um Infektionen mit dem SARS-CoV-2 Virus vorzubeugen sind     verschiedenste Maßnahmen umzusetzen. In geschlossenen Räumen ist dies vor allem das regelmäßige erneuern der Raumluft zur Verringerung der Aerosolbelastung.    Die Aerosolbelastung durch Covid Viren ist allerdings nicht direkt messbar. Die CO2-Konzentration kann als Qualitätsmerkmal genutzt werden, da Menschen beim Atmen CO2 und Aerosole ausstoßen. [1] Die Lüftungsdauer bis zum Erreichen einer akzeptablen Co2-Konzentration ist von diversen Einflussfaktoren wie aktuelle CO2-Konzentration, Raumgröße, Anzahl Personen sowie Innen- und Außentemperatur abhängig. Aus diesem Grund werden Faustregeln ausgesprochen die sich in Abhängigkeit vom Anwendungsfall und Jahreszeit unterscheiden [2] und mobile Anwendungen zur Berechnung der Lüftungsdauer empfohlen [3].
Aufgrund der diversen und oftmals unbekannten Einflussgrößen können die Faustregeln und Berechnungen zu falschen Ergebnissen und Handlungen führen, die in einem mangelndem Infektionsschutz münden.
    
## Lösungsansatz als Use-Case oder Prozessbeschreibung: Welche Sensoren wollen Sie einsetzen, um was zu messen und welche Auswertung planen Sie auf welche Art und Weise?
Um das Problem falsch abgeleiteter Handlungen aus fehlerbehafteten Ergebnissen zu Umgehen wird ein Prototyp eines Frühwarnsystems entwickelt, dass bei schlechter Luftqualität Handlungsempfehlungen vorgibt. Das System soll Anwendung in geschlossenen Räumen wie Klassenzimmern, Büros und auch privaten Räumlichkeiten finden. Mit einem Luftqualitäts-Sensor (MQ135) wird die CO2-Konzentration in der Raumluft gemessen und regelbasiert in Echtzeit bewertet. Die Luftqualität wird über ein Ampelsystem visualisiert und bei Überschreitung eines definierten Grenzwertes wird eine Handlungsempfehlung via Benachrichtigung ausgegeben. Des Weiteren wird ein Programm zur quantitativen Bewertung und graphischen Darstellung des zeitlichen Verlaufs der Luftqualität geschrieben.

## Technisches Konzept – grafische Darstellung der geplanten Architektur
Der Prototyp wird nach der 5-A Architektur aufgebaut. 

![image](https://user-images.githubusercontent.com/62206220/123763514-2c19a580-d8c4-11eb-9bad-4adc28cb15ec.png)

# Deliverable 2

> Problem und ggf. Quantifizierung des Problems
> Use-Case beschreiben mit Lösungsidee
> Umsetzung der Lösungsidee in Code/Flow Chart und Schaltbild
> Darstellung der erzeugten Informationen (Zeitreihen)
> Interpretation der Zeitreihen
> Kritische Diskussion und ggf. Ableiten von Verbesserungsideen; ggf. Anwendungsszenario im Industriellen Kontext
> Anhang: Code abbilden

Durch die anhaltende Coronavirus Pandemie hat der Infektionsschutz einen neuen Stellenwert erlangt. Um Infektionen mit dem SARS-CoV-2 Virus vorzubeugen sind verschiedenste Maßnahmen umzusetzen. In geschlossenen Räumen ist dies vor allem das regelmäßige lüften der Raumluft. Gerade bei kalten Temperaturen draußen ist es oftmals ein Streitpunkt wann und wie lange gelüftet werden soll. 
Dieses Projekt soll diesen Streitpunkt beseitigen. Das Projekt verfolgt das Ziel die Menschen mit einem visuellen Signal permanent über den aktuellen Zustand der Raumluft zu informieren. Außerdem soll bei einer Grenzwertüberschreitung automatisiert eine E-Mail Benachrichtigung versendet werden.
Coronavieren als solche sind nicht ohne weiteres in der Raumluft zu messen. Wenn ein Mensch ausatmet stößt er neben den sogenannten Aerosolen die mit Coronavieren belastet sein können auch CO2 aus. Dieser Zusammenhang zwischen der CO2-Konzentration und Coronavieren in der Luft macht die CO2-Konzentration zu einem guten Indikator für Coronavieren.*

Um die CO2-Konzentration in einem Raum Messen zu können wurde ein Prototyp entwickelt. Das Nachfolge Bild zeigt den fertigen Aufbau in der Praxis. Schematisch ist der Prototyp in der Datei "board_Steckplatine" dargestellt.

![IMG_20210628_134908__01](https://user-images.githubusercontent.com/84568672/123632162-e901f880-d817-11eb-8385-2ec570b12084.jpg)

Der Prototyp setzt sich aus folgenden Komponenten zusammen:

-ESP8266 v2

-MQ-135Gas Sensor Luftqualität Modul

-BME280 Barometrischer Sensor für Temperatur, Luftfeuchtigkeit und Luftdruck

-RGB LED

-Stromversorgungsmodul für MB102 Breadboard



Auf dem ESP8266 werden die Messwerte intern verarbeitet um die LED als Warnsignal zu steuern. Desweiteren werden die Messwerte vom Mikrocontroller zu AWS gesendet und in einer Datenbank gespeichert. Wird ein vorab festgelegter Grenzwert für CO2 überschritten sendet AWS automatisch durch Simple Notification Services eine Mail mit der Aufforderung zum Lüften. Mittels Boto3 lassen sich die generierten Daten auslesen und tiefergehend analysieren.


Nach einer ausführlichen Testphase des Prototypens konnten Probleme mit dem CO2 Sensor MQ-135 nicht behoben werden. Eine tiefgehende Recherche konnte auch keine Klarheit bringen. 
Die Messwerte für CO2 schwanken extrem sprunghaft und nicht nachvollziehbar in einem nicht realistischen Rahmen. Dieses Verhalten ist der nachfolgenden Abbildung dargestellt.

#![Diagramm](https://user-images.githubusercontent.com/84568672/123634648-008eb080-d81b-11eb-96e6-c89908083383.JPG)

Zwischenzeitlich konnten plausible Messwerte generiert werden. In diesem Zeitraum konnte die Funktion des Systems überprüft werden:
Steigt die CO2-Konzentration über 1000ppm begint die LED gelb zu leuchten. Steigt die CO2-Konzentration weiter auf über 2000ppm leuchtet die LED rot. Außerdem wird durch die Grenzwertüberschreitung von 2000ppm automatisiert eine E-Mail versendet. 

Zusammenfassend lässt sich sagen, dass das Projekt ein Teilerfolg ist. Durch den unzuverlässigen CO2 Sensor kann der aktuelle Prototyp nicht in der Praxis verwendet werden. Ersetzt man den sehr kostengünstigen MQ-135 durch den teureren MH-Z19C ist mit guten aussagekräftigen Messwerten zu rechnen. Dann ist von einem problemlosen Betrieb des Prototypen auszugehen. 

Um die Nutzbarkeit des Prototypens zukünftig weiter zu verbessern sollte zusätzlich noch ein LCD Modul verbaut werden. Damit kann permanent ohne große Umwege die CO2-Konzentration in der Raumluft abgelesen werden. Desweiteren sollte die Einfache aktuell verbaute LED durch eine helleres Modell ausgetauscht werden. So kann auch bei hellen Tageslicht sichergestellt werden, dass die LED gesehen wird. 
Für eine langfristige Verwendung des Prototypen sollte eine Schutzhülle erstellt werden. Es würde sich anbieten diese Schutzhülle 3D zu drucken. Ein entsprechender Prototyp dafür muss jedoch noch erstellt werden.


Bei diesem Github Repository handelt es sich um Dokumentation die als Anhang der ppt-Datei zu bewerten ist.

*https://frida-kahlo-schule.lvr.de/media/lvrfridakahloschule/aktuelles/corona/Lueften_in_Klassenraeumen_Empfehlungen_LVR_Dezernat_12.40_Arbeitssicherheit.pdf

## Literatur
[1] AR-CoV-2
[2] Coronavirus-BGHM-Zusatzinformationen-Lueftungsverhalten
[3] Lueften_in_Klassenraeumen_Empfehlungen_LVR_Dezernat_12.40_Arbeitssicherheit
[4] hartmann_kriegel_2020_de


