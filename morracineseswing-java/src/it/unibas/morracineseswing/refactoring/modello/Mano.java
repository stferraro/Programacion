package it.unibas.morracineseswing.refactoring.modello;
    
public class Mano {

    private static java.util.Random generatore = new java.util.Random();

    public final static int CARTA = 1;
    public final static int FORBICI = 2;
    public final static int SASSO = 3;

    public final static int MANOVINTADALCOMPUTER = 0;
    public final static int MANOVINTADALGIOCATORE = 1;
    public final static int MANOINPAREGGIO = 2;

    private int giocataGiocatore;
    private int giocataComputer;

    public void gioca(int giocataGiocatore) {
        assert(isValida(giocataGiocatore)) : "Giocata non valida: " + giocataGiocatore;
        setGiocataGiocatore(giocataGiocatore);
        generaGiocataComputer();
    }

    public boolean isValida(int giocata) {
        return (giocata >= Mano.CARTA && giocata <= Mano.SASSO);
    }

    public int getGiocataGiocatore() {
        return this.giocataGiocatore;
    }

    public int getGiocataComputer() {
        return this.giocataComputer;
    }

    private void setGiocataGiocatore(int giocataGiocatore) {
        this.giocataGiocatore = giocataGiocatore;
    }

    private void generaGiocataComputer() {
        this.giocataComputer = Math.abs(Mano.generatore.nextInt(3) + 1);
    }

    public int getEsito() {
        int esito = Mano.MANOVINTADALCOMPUTER;
        if (this.giocataGiocatore == this.giocataComputer) {
            esito = Mano.MANOINPAREGGIO;
        } else if ((this.giocataGiocatore == Mano.CARTA) && (this.giocataComputer == Mano.SASSO)) {
            esito = Mano.MANOVINTADALGIOCATORE;
        } else if ((this.giocataGiocatore == Mano.FORBICI) && (this.giocataComputer == Mano.CARTA)) {
            esito = Mano.MANOVINTADALGIOCATORE;
        } else if ((this.giocataGiocatore == Mano.SASSO) && (this.giocataComputer == Mano.FORBICI)) {
            esito = Mano.MANOVINTADALGIOCATORE;
        }
        return esito;
    }

}

