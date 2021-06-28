# airquality-measurement-device
IoT-Project @ Fachhochschule Aachen Industrielle Produktion und Industrie 4.0

Durch die anhaltende Coronavirus Pandemie hat der Infektionsschutz einen neuen Stellenwert erlangt. Um Infektionen mit dem SARS-CoV-2 Virus vorzubeugen sind verschiedenste Maßnahmen umzusetzen. In geschlossenen Räumen ist dies vorallem das regelmäßige lüften der Raumluft. Gerade bei kalten Temperaturen draußen ist es jedoch oftmals ein Streipunkt wann und wie lange gelüftet werden soll. 
Dieses Projekt soll diesen Streitpunkt beseitigen. Das Projekt verfolgt das Ziel die Menschen mit einem visuellen Signal permanent über den aktuellen Zustand der raumluft informieren. Außerdem soll bei einer Grenzwertüberschreitung automatisiert eine E-Mail Benachrichtigung versendet werden.
Coronavieren als solche sind nicht ohne weiteres in der Raumluft zu messen. Wenn ein Mensch ausatmet stößt er neben den sogenannten Aerosolen die mit Coronavieren belastet sein können auch CO2 aus. Dieser Zusammenhang zwischen der CO2-Konzentration und Coronavieren in der Luft macht die CO2-Konzentration zu einem guten Indikator für Coronavieren. 1

Um die CO2-Konzentration in einem Raum Messen zu können wurde ein Prototyp entwickelt. Das Nachfolge Bild zeigt den fertigen Aufbau in der Praxis. Schematisch ist der Prototyp in der Datei "board_Steckplatine" dargestellt.

![IMG_20210628_134908__01](https://user-images.githubusercontent.com/84568672/123632162-e901f880-d817-11eb-8385-2ec570b12084.jpg)

Der Prototyp setzt sich aus folgenden Komponenten zusammen:
-ESP8266 v2
-MQ-135Gas Sensor Luftqualität Modul
-BME280 Barometrischer Sensor für Temperatur, Luftfeuchtigkeit und Luftdruck
-RGB LED
-Stromversorgungsmodul für MB102 Breadboard




1 https://frida-kahlo-schule.lvr.de/media/lvrfridakahloschule/aktuelles/corona/Lueften_in_Klassenraeumen_Empfehlungen_LVR_Dezernat_12.40_Arbeitssicherheit.pdf
