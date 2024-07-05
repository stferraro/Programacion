package it.unibas.morracineseswing.modello;

public class Partita {
    public final static int LIMITEMANI = 3;
    
    public final static int PARTITAVINTADALCOMPUTER = 0;
    public final static int PARTITAVINTADALGIOCATORE = 1;
    public final static int PARTITAINCORSO = 2;
    
    private int maniVinteDalComputer = 0;
    private int maniVinteDalGiocatore = 0;
    private int pareggi = 0;
    private Mano ultimaMano;
    
    public int getManiVinteDalComputer() {
        return this.maniVinteDalComputer;
    }
    
    public int getManiVinteDalGiocatore() {
        return this.maniVinteDalGiocatore;
    }
    
    public int getPareggi() {
        return this.pareggi;
    }
    
    public Mano getUltimaMano() {
        return this.ultimaMano;
    }
    
    public Mano giocaMano(int giocata) {
        assert(this.getStato() == Partita.PARTITAINCORSO) : "Partita conclusa. Stato partita: " + this.getStato();
        Mano mano = new Mano();
        mano.gioca(giocata);
        int esito = mano.getEsito();
        if (esito == Mano.MANOVINTADALCOMPUTER) {
            this.maniVinteDalComputer++;
        } else if (esito == Mano.MANOVINTADALGIOCATORE) {
            this.maniVinteDalGiocatore++;
        } else if (esito == Mano.MANOINPAREGGIO) {
            this.pareggi++;
        }
        this.ultimaMano = mano;
        return mano;
    }
    
    public int getStato(){
        int stato = Partita.PARTITAINCORSO;
        if (this.maniVinteDalComputer == Partita.LIMITEMANI) {
            stato = Partita.PARTITAVINTADALCOMPUTER;
        } else if (this.maniVinteDalGiocatore == Partita.LIMITEMANI) {
            stato = Partita.PARTITAVINTADALGIOCATORE;
        }
        return stato;
    }
    
    public String getStringaStato(){
        if (this.getStato() == Partita.PARTITAVINTADALCOMPUTER) {
            return "Partita conclusa. Ha vinto il computer";
        } else if (this.getStato() == Partita.PARTITAVINTADALGIOCATORE) {
            return "Partita conclusa. Hai vinto";
        }
        return "La partita è in corso";
    }
    
}
