# Ein Algorithmus zum Lösen von Sudokus
Dieses Projekt bietet die Funktionalität zum Lösen jedes lösbaren Sudokus und der Veranschaulichung des benutzten Algorithmus. Dafür läuft der Algorithmus rekursiv über das Sudoku-Borad und versucht die freien Stellen zu lösen. Wenn er an einer Stelle keine valide Lösung findet, geht er n Schritte zurück und versucht an einer früheren Stelle eine andere Lösung.

# Informationen zu dem Code
## sudokusolver.py
Diese Datei beinhaltet den grundlegenden Algorithmus und gibt über die Konsole die Lösung zu einem im Code erstellten Sudoku-Board aus. 

## sudoku_gui.py
In dieser Datei wird der gleiche Algorithmus verwendet, aber zum Zwecke der Veranschaulichung verlangsamt. Hierfür kann auf einer GUI ein belibiges (lösbares) Sudoku angeben werden und durch die Leertaste wird der Lösungsvorgang gestartet.

# Requirements
* pygame
* time
* threading 

