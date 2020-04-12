# AI_ModelCreater
Diese Software soll ein easy to use (, deutschsprachigen) KI-Model Creator für Bilderkennung darstellen, welcher trotz der einfchen Bedienbarkeint eine hohe Variabilität erreicht um SIE möglichst bei IHREM nächsten Bilderkennungsprojekt zu unterstützen. Die erstellten Models können zumindest zurzeit ausschließlich mit der [Realtime_Detect](https://github.com/BySuxax/Realtime_Detect) Software ausgeführt werden! Der [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator) installiert Realtime_Detect falls sie wollen automatisch. <br>
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

1. Falls sie in Betracht ziehen die Realtime_Detect Software zu benutzen um Bilder ihrer Kamera durch ihr erstelltes Model zu verarbeiten können sie schon im vorraus ROS wie [hier](http://wiki.ros.org/melodic/Installation/Ubuntu) besch
rieben installieren. Und gehen sie sicher, dass dieser Command in jedem Terminal, das benutzt wird ausgeführt wird: `source /opt/ros/melodic/setup.bash` Dies können sie sich aber auch später entscheiden entweder, wenn das Training beendet ist auf "Mit Realtime_Detect fortfahren" klicken (dann muss ROS manuell [so](http://wiki.ros.org/melodic/Installation/Ubuntu)(http://wiki.ros.org/melodic/Installation/Ubuntu) installiert sein), dann wird Realtime_Detect automatisch installiert, oder sie können sie jeder Zeit nach der Model-Erstellung Manuel wie [hier](https://github.com/BySuxax/Realtime_Detect) beschrieben installieren. 


1. Als erstes sollten sie das Git Repository clonen: <br>
`git clone https://github.com/BySuxax/AI_Model_Creator.git` <br>
Es kann sein, dass es nötig ist, erst Git zu installieren: `sudo apt install git`


1. Als nächstes können sie, um das Programm zu starten **UND AUTOMATISCH GEBRAUCHTE LIBRARIES ZU INSTALLIEREN** folgenden command ausführen: <br>**(Ich übernehme keine Haftung für Systemschäden, Dateiverlust oder ähnlichem. Es werden durch python Libraries, Programmeigene Ordner gelöscht. Eine Fehlfunktion kann nicht ausgeschlossen werden!)** <br> `python3 AI_Model_Creator/startAPI.py` <br> 
**!! Achten sie auf die Konsole! Es kann sein, dass sie ihr Root Passwort eingeben müssen um die Libraries zu installieren !! (Falls sie dies nicht wollen reicht es folgende programme mithilfe von sudo apt-get zu installieren: `python3` , `python3-venv`. Die sonstigen pakete sollten ohne Root installierbar sein.)** <br>Es sollte sich daraufhin ein Fenster zur Einstellung von Trainingsparametern öffnen.

1. Stellen sie die Parameter für sich passend ein. Die Angaben dort sind nur ungefähre angaben und müssen nicht der Wirklichkeit entsprechen. Das Training hat leider zur Zeit noch keine Abbrechen taste. Daher sollten sie darauf achten die Länge des trainigs nicht zu groß zu machen. (Max ist ca. 4 Stunden je nach PC) (Wird bald bessere Lösungen geben wenn dieses Projekt weiterentwickelt wird. Dafür ist uns eure  Rückmeldung sehr wichtig! Schriebt gerne was euch stört aber natürlich auch gefällt oder wenn etwas nicht geklappt hat)

1. Geben sie einen Namen ein unter dem das Model gespeichert wird. ***Dann drücken sie auf Save Name!*** (Es soll keine Endung wie .pt enthalten sein) Nun können sie auf weiter drücken. Es sollte sich ein Fenster für die Trainings-Bilder auswahl öffnen. <br> 

1. Wählen sie einen Bilderordner inwelchem die Bilder sind, die sie der KI zu trainieren geben wollen. (Sie können natürlich auch zwischendrin den Ordner wechseln um andere Bilder zu wählen.) Es sollten nach einer kurzen Lade-Pause alle Bilder in diesem Ordner in dem Linken Großen Kasten angezeigt werden. Wählen sie die Bilder aus die zu einer Klasse gehören indem sie auf sie linksklicken. Wenn sie ausgewäht sind, sind die Bildumrandungen rot makiert.


1. Wenn sie die Bilder ausgewählt haben die sie einer Klasse hinzufügen wollen, drücken sie auf "Füge ausgewählte Bilder einer Klasse hinzu". Es sollte sich ein kleines Fenster öffnen, inwelchem sie neue Klassen hinzufügen indem sie den Klassennamen in das Textfeld eingen und auf "Neue Klasse hinzufügen" drücken. Mit der Combobox könnt ihr dann die Klasse auswählen, der ihr die Bilder hinzufügen wollt. Dann bestätigt ihr mit "Mit ausgewählten Klasse fortfahren". Nun könnt ihr wieder neue Bilder auswählen und sie entweder einer Neuen oder der Gleichen Klasse hinzufügen.

1. Wenn sie mit dem auswählen fertig sind, können sie auf "weiter" drücken, um mit dem Training zu beginnen. Jetzt sollte sich ein Fenster öffen, inwelchem dir Infos zum Training gegeben werden (keine sorge, es kann etwas dauern bis das Training beginnt) und wie es weiter geht. Die Große Progressbar zeigt an, wie lange noch trainiert wird. Die Beiden oben zeigen an wie gut die KI bereits ist. Desto weniger Fehler sie macht desto besser ist sie natürlich auch. Der unterschied ist, dass bei "Fehler Training" die KI mit Bildern getestet wird, die sie schon gesehen hat, währen bei "Fehler Test" die KI die Bilder noch nie gesehen hat.

1. Sie können nun das Programm schließen.

### Um nun auch dieses Launchfile auszuführen muss folgendes getan werden:
 1. Sie müssen sicherstellen, dass das Terminal, das sie benutzen mit ROS und ihrem ros_ws "bekannt" gemacht wurde:  <br>
 ` source /opt/ros/melodic/setup.bash `<br>` source Realtime_Detect/ros_ws/devel/setup.bash ` <br> Wenn sie wollen können sie auch diese beiden Befehle zur .bashrc in ihrem Home-Directory hinzufügen.

1. Jetzt können sie die Bilderkennung ganz einfach mit diesem Command starten: <br> `roslaunch realtime_detect IHR_GEWÄHLTER_NAME.launch` <br> Ersetzen sie einfach noch IHR_GEWÄHLTER_NAME mit dem Namen, den sie beim Launchfile generieren angegeben haben.

 1. Die Ergebnisse können sie jetzt über das ROS-Topic `/classified_Name` auslesen. Wie sie dies in verschiedenen Programmiersprachen tun können, wird hier erklärt: <br> [Python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) <br>
 [C++](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
 <br> Sie können auch einfach über den folgenden Befehl die Ausgaben in der Konsole einsehen: <br>
 `rostopic echo /classified_Name`
 
 Wenn es irgendwelche Schwirigkeiten oder Fehler gibt, dann schreiben sie gerne einen Kommentar, um das Programm zu verbessern und ihnen weiterzuhelfen.
