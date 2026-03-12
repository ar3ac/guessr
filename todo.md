# Number Guessing Game — TODO

Obiettivo: costruire un gioco da terminale in cui il computer sceglie un numero casuale e il giocatore deve indovinarlo nel minor numero di tentativi possibile.

---

## Fase 0 — Setup progetto

- [x] Crea la cartella progetto e inizializza Git.
- [x] Crea i file base: `main.py`, `todo.md`, `README.md`, `.gitignore`.
- [x] Definisci il perimetro del progetto: terminale puro, niente GUI.
- [x] Decidi se vuoi una versione minima oppure una leggermente arricchita con livelli di difficoltà.

Criterio “done”:

- Il progetto è pronto e pulito prima di scrivere logica.

---

## Fase 1 — Struttura base del gioco

- [x] Importa il modulo necessario per generare numeri casuali.
- [x] Crea il flusso base del programma:
  - messaggio di benvenuto
  - spiegazione rapida delle regole
  - selezione del livello
  - avvio della partita
- [x] Decidi il range del numero da indovinare (es. da 1 a 100).
- [x] Decidi se il numero segreto viene generato subito o solo dopo la scelta della difficoltà.

Criterio “done”:

- Il programma parte, accoglie l’utente e arriva correttamente all’inizio della partita.

---

## Fase 2 — Livelli di difficoltà

- [x] Implementa almeno 3 livelli di difficoltà:
  - Easy
  - Medium
  - Hard
- [x] Associa a ogni livello un numero massimo di tentativi.
- [x] Valida l’input del livello scelto.
- [x] Gestisci il caso in cui l’utente inserisce un valore non valido.

Esempio logico:

- Easy → 10 tentativi
- Medium → 5 tentativi
- Hard → 3 tentativi

Criterio “done”:

- L’utente può scegliere un livello e il programma imposta correttamente i tentativi disponibili.

---

## Fase 3 — Generazione numero segreto

- [x] Genera un numero casuale nel range deciso.
- [x] Conserva il numero in una variabile dedicata.
- [x] Assicurati che il numero venga generato una sola volta per partita.
- [x] Verifica mentalmente il flusso: il numero non deve cambiare a ogni tentativo.

Criterio “done”:

- Ogni nuova partita ha un solo numero segreto stabile da indovinare.

---

## Fase 4 — Input del giocatore

- [x] Chiedi all’utente di inserire un tentativo.
- [x] Converti l’input in intero.
- [x] Gestisci input non numerici senza far crashare il programma.
- [x] Controlla che il numero inserito sia nel range consentito.
- [x] Se il valore è fuori range, mostra un messaggio chiaro e non contare il tentativo (oppure decidi esplicitamente di contarlo).

Criterio “done”:

- Il gioco accetta input validi e gestisce quelli non validi in modo pulito.

---

## Fase 5 — Logica del confronto

- [x] Confronta il numero inserito con il numero segreto.
- [x] Se il numero è troppo basso, mostra un messaggio tipo “Too low”.
- [x] Se il numero è troppo alto, mostra un messaggio tipo “Too high”.
- [x] Se il numero è corretto, mostra un messaggio di vittoria.
- [x] Interrompi il gioco appena il giocatore indovina.

Criterio “done”:

- Il feedback al giocatore è sempre corretto.

---

## Fase 6 — Conteggio tentativi

- [ ] Tieni traccia dei tentativi usati.
- [ ] Riduci i tentativi rimasti dopo ogni input valido.
- [ ] Mostra quanti tentativi restano dopo ogni errore.
- [ ] Quando i tentativi finiscono, il gioco deve terminare.
- [ ] Alla sconfitta, mostra il numero corretto.

Criterio “done”:

- Il numero di tentativi si aggiorna bene e il gioco termina nei casi giusti.

---

## Fase 7 — Fine partita

- [ ] Gestisci i due scenari finali:
  - vittoria
  - sconfitta
- [ ] Mostra un messaggio finale pulito e leggibile.
- [ ] Indica quanti tentativi sono stati usati per vincere, se applicabile.
- [ ] Rivela sempre il numero corretto in caso di sconfitta.

Criterio “done”:

- La partita si chiude bene senza loop strani o output confusi.

---

## Fase 8 — Giocare di nuovo

- [ ] Chiedi all’utente se vuole fare un’altra partita.
- [ ] Accetta input tipo `y/n` oppure `yes/no`.
- [ ] Se la risposta è positiva, resetta correttamente tutte le variabili della partita.
- [ ] Se la risposta è negativa, chiudi il programma con un messaggio finale.
- [ ] Gestisci input non validi anche qui.

Criterio “done”:

- Il gioco può ripartire senza dover rilanciare manualmente lo script.

---

## Fase 9 — Pulizia del codice

- [ ] Controlla se ci sono parti ripetute e prova a spostarle in funzioni.
- [ ] Dai nomi chiari alle variabili.
- [ ] Evita blocchi troppo lunghi nel main.
- [ ] Valuta di creare funzioni tipo:
  - `choose_difficulty()`
  - `generate_secret_number()`
  - `get_user_guess()`
  - `play_game()`
- [ ] Rimuovi eventuali print di debug.

Criterio “done”:

- Il codice è leggibile e diviso in responsabilità sensate.

---

## Fase 10 — Edge cases

- [ ] Input vuoto.
- [ ] Input testuale invece di un numero.
- [ ] Numero fuori range.
- [ ] Selezione difficoltà non valida.
- [ ] Replay con risposta non valida.
- [ ] Verifica che il programma non mostri traceback all’utente nei casi normali.

Criterio “done”:

- Il gioco è robusto e “a prova di utente distratto”.

---

## Fase 11 — README

- [ ] Scrivi una breve descrizione del progetto.
- [ ] Spiega come eseguire il programma.
- [ ] Elenca le funzionalità.
- [ ] Inserisci almeno un esempio di sessione di gioco.
- [ ] Aggiungi una sezione “What I practiced” con i concetti imparati.
- [ ] Aggiungi una sezione “Possible improvements”.

Criterio “done”:

- Il repository è comprensibile anche a chi lo vede per la prima volta.

---

## Fase 12 — Chiusura progetto

- [ ] Fai un test finale completo.
- [ ] Controlla che il flusso vittoria/sconfitta/replay sia corretto.
- [ ] Esegui `git add .`
- [ ] Esegui un commit finale con un messaggio chiaro.
- [ ] Fai push su GitHub.

Esempio commit finale:

- `git commit -m "feat: complete number guessing game project"`
