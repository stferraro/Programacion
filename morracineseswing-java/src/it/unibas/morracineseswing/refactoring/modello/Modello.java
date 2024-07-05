package it.unibas.morracineseswing.refactoring.modello;

public class Modello {
    
    private Gioco gioco;
    private Partita partita;
    private Mano mano;
    
    public Gioco getGioco() {
        return this.gioco;
    }

    public void setGioco(final Gioco gioco) {
        this.gioco = gioco;
    }

    public Partita getPartita() {
        return this.partita;
    }

    public void setPartita(final Partita partita) {
        this.partita = partita;
    }

    public Mano getMano() {
        return this.mano;
    }

    public void setMano(final Mano mano) {
        this.mano = mano;
    }
}
