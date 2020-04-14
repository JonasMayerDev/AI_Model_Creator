# AI_Model_Creator v 0.0.1 (Pre-Alpha)
Diese Software soll einen easy to use (, deutschsprachigen) KI-Model Creator für Bilderkennung darstellen, welche trotz der einfachen Bedienbarkeit eine hohe Variabilität erreicht, um SIE möglichst bei IHREM nächsten Bilderkennungsprojekt zu unterstützen. Die erstellten Models können zumindest zurzeit ausschließlich mit der [Realtime_Detect](https://github.com/BySuxax/Realtime_Detect) Software ausgeführt werden! Der [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator) installiert Realtime_Detect falls sie wollen automatisch. <br>
Wenn aber Fehler bei der Installation auftreten oder sonst etwas mit dieser Software getan werden soll, kann dieses Programm auch manuell installiert werden wie [hier](https://github.com/BySuxax/Realtime_Detect) beschrieben.

**Kompatibilität** | **Sollte Funktionieren** | **Tut auf frischem System (getestet)**
------------ | ------------- | -------------
Ubuntu 18.04.4| :heavy_check_mark: |:heavy_check_mark:	|
Linux Mint| :heavy_check_mark:	| :white_check_mark:	|
Debian basierte Linux Distros| :heavy_check_mark:| :x:|
Andere Linux Distros| :x: | :x: |
Windows| :x: | :x: |
Mac | :x: | :x: | <br>



### Um den AI_Model_Creator zu installieren und ein Model zu generieren, musst du folgendes tun:

I. Stellen sie sicher, dass Python 3, wie es eigentlich auf allen Debian basierten Systemen der Fall sein sollte, installiert ist:<br> `python3 --version`<br> Ansonsten installieren sie es durch: <br>`sudo apt-get install python3`


II. Falls sie in Betracht ziehen die Realtime_Detect Software zu benutzen, um Bilder ihrer Kamera durch ihr erstelltes Model zu verarbeiten, können sie schon im voraus ROS Melodic, wie [hier](http://wiki.ros.org/melodic/Installation/Ubuntu) beschrieben, installieren. Und gehen sie sicher, dass dieser Command in jedem Terminal, das benutzt wird ausgeführt wird:<br> `source /opt/ros/melodic/setup.bash` <br> Dies können sie sich aber auch später entscheiden. Entweder, wenn das Training beendet ist, auf "Mit Realtime_Detect fortfahren" klicken (dann muss ROS Melodic manuell [so](http://wiki.ros.org/melodic/Installation/Ubuntu) installiert sein), dann wird nämlich Realtime_Detect automatisch installiert, oder sie können sie jeder Zeit, nach der Modelerstellung, manuell wie [hier](https://github.com/BySuxax/Realtime_Detect) beschrieben installieren. 


1. Als Erstes sollten sie das Git Repository clonen: <br>
`git clone https://github.com/BySuxax/AI_Model_Creator.git` <br>
Es kann sein, dass es nötig ist, erst Git zu installieren: `sudo apt install git`


1. Als Nächstes können sie, um das Programm zu starten **UND AUTOMATISCH GEBRAUCHTE LIBRARIES ZU INSTALLIEREN (Alle automatisch installierten Libraries stehen im File: LicenseInformation.txt)**, folgenden Command ausführen: <br>**(Ich übernehme keine Haftung für Systemschäden, Dateiverlust oder ähnlichem. Es werden durch Python Libraries, Programmeigene Ordner gelöscht. Eine Fehlfunktion kann nicht ausgeschlossen werden!)** <br> `python3 AI_Model_Creator/startAPI.py` <br> 
**!! Achten sie auf die Konsole! Es kann sein, dass sie ihr Root Passwort eingeben müssen, um die Libraries zu installieren !! (Falls sie dies nicht wollen reicht es folgende Programme mithilfe von `sudo apt-get install` zu installieren: `python3` , `python3-venv`. Die sonstigen Pakete sollten ohne Root installierbar sein.)** <br>Es sollte sich nach einiger Zeit ein Fenster zur Einstellung von Trainingsparametern öffnen.

1. Stellen sie die Parameter für sich passend ein. Die Angaben dort sind nur ungefähre Angaben und müssen nicht der Wirklichkeit entsprechen. Das Training hat leider zurzeit noch keine Abbrechen-Taste. Daher sollten sie darauf achten die Länge des Trainings nicht zu groß zu machen. (Maximum, was eingestellt werden kann, ist ca. 4 Stunden je nach PC und menge der Daten) (Wird bald bessere Lösungen geben, wenn dieses Projekt weiterentwickelt wird.)

1. Geben sie einen Namen ein unter dem das Model gespeichert wird. ***Dann drücken sie auf "Save Name"!*** (Es soll keine Endung wie .pt enthalten sein) Nun können sie auf weiter drücken. Es sollte sich ein Fenster für die Trainings-Bilder Auswahl öffnen. <br> 

1. Wählen sie einen Bilderordner in welchem die Bilder sind, die sie der KI zu trainieren geben wollen. (Sie können natürlich auch zwischendrin den Ordner wechseln, um andere Bilder zu wählen.) Es sollten nach einer kurzen Lade-Pause alle Bilder in diesem Ordner in dem linken großen Kasten angezeigt werden. Wählen sie die Bilder aus die zu einer Klasse gehören indem sie auf sie links klicken. Wenn sie ausgewählt sind, sind die Bildumrandungen rot markiert.


1. Wenn sie die Bilder ausgewählt haben, die sie einer Klasse hinzufügen wollen, drücken sie auf "Füge ausgewählte Bilder einer Klasse hinzu". Es sollte sich ein kleines Fenster öffnen, in welchem sie neue Klassen hinzufügen, indem sie den Klassennamen in das Textfeld eingeben und auf "Neue Klasse hinzufügen" drücken. Mit der Combobox können sie dann die Klasse auswählen, welcher die Bilder hinzufügen werden sollen. Dann bestätigen sie mit "Mit ausgewählten Klasse fortfahren". Nun können sie wieder neue Bilder auswählen und sie entweder einer neuen oder der gleichen Klasse hinzufügen.

1. Wenn sie mit dem Auswählen fertig sind (am besten für jede Klasse mindestens 10 Bilder), können sie auf "weiter" drücken, um mit dem Training zu beginnen. Jetzt sollte sich ein Fenster öffnen, in welchem dir Infos zum Training gegeben werden (keine sorge, es kann etwas dauern bis das Training beginnt) und wie es weiter geht. Die große Progressbar zeigt an, wie lange noch trainiert wird. Die Beiden oben zeigen an wie gut die KI bereits ist. Desto weniger Fehler sie macht, desto besser ist sie natürlich auch. Der Unterschied ist, dass bei "Fehler Training" die KI mit Bildern getestet wird, die sie schon gesehen hat, währen bei "Fehler Test" die KI die Bilder noch nie gesehen hat.

1. Sie können nun entweder das Programm schließen über den "Beenden" Button oder mit der Realtime_Detect Software fortfahren. Wenn sie mit Realtime_Detect fortfahren, muss ROS Melodic installiert sein oder umgehend installiert werden und der Befehl muss in deinem ".bashrc" Skript in deinem Home-Verzeichniss stehen:<br> `source /opt/ros/melodic/setup.bash`<br> Wenn du auf "Weiter mit Realtime_Detect" drückst, wird die Software automatisch installiert. Du kannst das Programm aber auch beenden und Realtime_Detect wie [hier](https://github.com/BySuxax/Realtime_Detect) beschrieben manuell installieren. In beiden Fällen findest du [hier](https://github.com/BySuxax/Realtime_Detect) wie du weiter machen musst um das erstellte Model anwenden zu können.

Mir ist deine Rückmeldung sehr wichtig! Schrieb gerne was dich stört aber natürlich auch gefällt oder wenn etwas nicht geklappt hat, hoffentlich finden wir dann eine Lösung. Meine E-Mail: BySuxaxofficial@gmail.com

All automatically installed Libraries are mentioned in "LicenseInformation.txt"
