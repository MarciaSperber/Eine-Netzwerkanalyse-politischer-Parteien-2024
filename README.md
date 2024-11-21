# Eine Netzwerkanalyse politischer Parteien der Europawahl Deutschlands im Jahr 2024
*von Marcia Sperber im Rahmen des Seminars "Die Methode der Netzwerkanalyse in Theorie und Praxis" im SoSe 2024 an der Universität Stuttgart.*

Zur Nachvollziehbarkeit der Arbeit und auch der Weiterverwendung der Daten, stellt dieses Repository die Daten und Ergebnisse zur Verfügung, die aus dem praktischen Teil hervorgegangen sind.

Die Hausarbeit untersucht die Verbindungen zwischen den 14 politischen Parteien und Vereinigungen, die 2024 einen Sitz im Europaparlament erhalten haben. Vor dem Hintergrund der gebräuchlichen ideologischen Einordnung von Parteien im Spektrum links bis rechts, soll die Arbeit untersuchen, ob linke oder rechte Gruppierungen dieselben Themenschwerpunkte aufweisen. Der Fokus liegt hierbei auf Übereinstimmungen der Wahlprogramme der Parteien mit erarbeiteten Schlüsselwörtern zu bestimmten politisch relevanten Themengebieten. Diese Themen sind aus xxx entnommen worden. Die Schlüsselwörter wurden mithilfe von ChatGPT generiert.

Die genutzten Wahlprogramme der 14 politischen Parteien werden im Ordner "Wahlprogramme der EU-Wahl 2024" in Form von Textdateien verortet.

Im Ordner "Python-Code" befindet sich der Python-Code sowie das Ergebnis in Form einer Excel-Tabelle. Der Python-Code beinhaltet die sieben Themengebiete sowie jeweils 10 Schlüsselwörter. Die Schlüsselwörter werden so formuliert, dass der Wortstamm mit beliebigen Präfixen und Suffixen gefunden wird. Der Relevanzwert jeder Themenkategorie pro Partei wird dann aus der Häufigkeit des Schlüsselworts im Verhältnis zum Textumfang berechnet.

Der Ordner "Knoten und Kanten" beinhaltet zwei Versionen von Knoten- und Kanten-Tabellen, da für die Hausarbeit zwei verschiedene Netzwerke generiert wurden. 
Die erste Version stellt die Prominenz der erarbeiteten Themengebiete in den jeweiligen Wahlprogrammen 2024 dar. Zugrunde liegen die Datei "Knoten_Partei_Themengebiet.csv" und "Kanten_Partei_Themengebiet.csv".
Die zweite Version "Kanten_Partei_Partei.csv" setzt Parteienpaare unter Einbezug aller Themenkategorien in Beziehung zueinander und nimmt dabei den allgemeinen Relevanzwert als Gewichtung. Zu der zweiten Version der Kanten gehört die Berechnung der allgemeinen und themenspezifischen Relevanzwerte, die dann als Daten für die Kanten genutzt werden. Die Berechnungsdatei xxx nutzt Excel-Befehle, um die Relevanz einer Thematik zwischen zwei Parteien in Form der absoluten Differenz sowie die Cosinus-Ähnlichkeit als allgemeiner Relevanzwert zu berechnen. Zudem bezeichet die Knotendatei "Knoten_Partei_Partei.csv" neben den Parteinamen sowie deren Kürzel, das Attribut Stimmenanteil in Prozent sowie die Zuordnung der Parteien zu entweder (ideologisch) links oder rechts.
