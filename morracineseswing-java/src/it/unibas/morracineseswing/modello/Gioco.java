package it.unibas.morracineseswing.modello;

public class Gioco {

    private int partiteVinteDalComputer;
    private int partiteVinteDalGiocatore;
    private String nomeGiocatore;

    public String getNomeGiocatore() {
        return this.nomeGiocatore;
    }

    public void setNomeGiocatore(String nomeGiocatore) {
        this.nomeGiocatore = nomeGiocatore;
    }

    public int getPartiteVinteDalComputer() {
        return this.partiteVinteDalComputer;
    }

    public int getPartiteVinteDalGiocatore() {
        return this.partiteVinteDalGiocatore;
    }

    public void gestisciPartita(Partita partita) {
        assert(partita.getStato() != Partita.PARTITAINCORSO) : "La partita e' in corso";
        if (partita.getStato() == Partita.PARTITAVINTADALCOMPUTER) {
            this.partiteVinteDalComputer++;
        } else if (partita.getStato() == Partita.PARTITAVINTADALGIOCATORE) {
            this.partiteVinteDalGiocatore++;
        }
    }

}
