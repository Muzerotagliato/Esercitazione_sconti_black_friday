"""Un sistema gestisce negozi online che regalano sconti ai primi utenti che fanno acquisti
 sul sito nel giorno del Black Friday. Gli utenti hanno un username, una password e uno slot “sconto”.
Chiedere in ingresso quanti sconti sono disponibili, creare un gruppo di utenti e poi usare un algoritmo per
assegnare gli sconti agli utenti fino a quando sono disponibili.

Considerare sia il caso in cui ci siano più utenti che sconti, sia il contrario."""

from classes import Utente, assegna_sconti

numero_sconti=int(input("Quanti sconti sono disponibili?"))
assegna_sconti(numero_sconti)
print("\nCodice modificato per il secondo upgrade")