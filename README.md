# airquality-measurement-device
IoT-Project @ Fachhochschule Aachen Industrielle Produktion und Industrie 4.0

Durch die anhaltende Coronavirus Pandemie hat der Infektionsschutz einen neuen Stellenwert erlangt. Um Infektionen mit dem SARS-CoV-2 Virus vorzubeugen sind verschiedenste Maßnahmen umzusetzen. In geschlossenen Räumen ist dies vor allem das regelmäßige lüften der Raumluft. Gerade bei kalten Temperaturen draußen ist es oftmals ein Streitpunkt wann und wie lange gelüftet werden soll. 
Dieses Projekt soll diesen Streitpunkt beseitigen. Das Projekt verfolgt das Ziel die Menschen mit einem visuellen Signal permanent über den aktuellen Zustand der Raumluft informieren. Außerdem soll bei einer Grenzwertüberschreitung automatisiert eine E-Mail Benachrichtigung versendet werden.
Coronavieren als solche sind nicht ohne weiteres in der Raumluft zu messen. Wenn ein Mensch ausatmet stößt er neben den sogenannten Aerosolen die mit Coronavieren belastet sein können auch CO2 aus. Dieser Zusammenhang zwischen der CO2-Konzentration und Coronavieren in der Luft macht die CO2-Konzentration zu einem guten Indikator für Coronavieren. 1

Um die CO2-Konzentration in einem Raum Messen zu können wurde ein Prototyp entwickelt. Das Nachfolge Bild zeigt den fertigen Aufbau in der Praxis. Schematisch ist der Prototyp in der Datei "board_Steckplatine" dargestellt.

![IMG_20210628_134908__01](https://user-images.githubusercontent.com/84568672/123632162-e901f880-d817-11eb-8385-2ec570b12084.jpg)

Der Prototyp setzt sich aus folgenden Komponenten zusammen:
-ESP8266 v2
-MQ-135Gas Sensor Luftqualität Modul
-BME280 Barometrischer Sensor für Temperatur, Luftfeuchtigkeit und Luftdruck
-RGB LED
-Stromversorgungsmodul für MB102 Breadboard

Auf dem ESP8266 werden die Messwerte intern verarbeitet um LED als Warnsignal zu steuern. Desweiteren werden die Messwerte vom Mikrocontroller zu AWS gesendet und in einer Datenbank gespeichert. Wird ein vorab festgelegter Grenzwert für CO2 überschritten sendet AWS automatisch durch Simple Notification Services eine Mail mit der Aufforderung zum Lüften. Mittels Boto3 lassen sich die generierten Daten auslesen und tiefergehend analysieren.


Nach einer ausführlichen Testphase des Prototypens konnten sich Probleme mit dem CO2 Sensor MQ-135 nicht beheben. Eine tiefgehende Recherche konnte auch keine Klarheit bringen. 
Die Messwerte für CO2 schwanken extrem stark in einem nicht realistischen Rahmen. Dieses Ergebnis ist der nachfolgenden Abbildung dargestellt.

#![Diagramm](https://user-images.githubusercontent.com/84568672/123634648-008eb080-d81b-11eb-96e6-c89908083383.JPG)

Zwischenzeitlich konnten plausible Messwerte generiert werden. In diesem Zeitraum konnte die Funktion des Systems überprüft werden:
Steigt die CO2-Konzentration über 1000ppm begint die LED gelb zu leuchten. Steigt die CO2-Konzentration weiter auf über 2000ppm leuchtet die LED rot. Außerdem wird durch die Grenzwertüberschreitung von 2000ppm automatisiert eine E-Mail versendet. 

Zusammenfassend lässt sich sagen, dass das Projekt ein Teilerfolg ist. Durch den unzuverlässigen CO2 Sensor kann der aktuelle Prototyp nicht in der Praxis verwendet werden. Ersetzt man den sehr kostengünstigen MQ-135 durch den teuerren MH-Z19C ist mit guten aussagekräftigen Messwerten zu rechnen. 
Um die Nutzbarkeit des Prototypens zukünftig weiter zu verbessern sollte zusätzlich noch ein LCD Modul verbaut werden. Damit kann permanent ohne große Umwege die CO2-Konzentration in der Raumluft nachvollzogen werden. Desweiteren sollte die Einfache aktuell verbaute LED durch eine Helleres Modell ausgetauscht werden. So kann auch bei hellen Tageslicht sichergestellt werden, dass die LED gesehen wird. 
Für eine langfristige Verwendung des Prototypen sollte eine Schutzhülle erstellt werden. Es würde sich anbieten diese Schutzhülle 3D zu drucken. Ein entsprechender Prototyp dafür muss jedoch noch erstellt werden.


Bei diesem Github Repository handelt es sich um Dokumentation die als Anhang der ppt-Datei zu bewerten ist.

1 https://frida-kahlo-schule.lvr.de/media/lvrfridakahloschule/aktuelles/corona/Lueften_in_Klassenraeumen_Empfehlungen_LVR_Dezernat_12.40_Arbeitssicherheit.pdf
