package it.unibas.morracineseswing.refactoring.vista;

import it.unibas.morracineseswing.refactoring.modello.*;
import it.unibas.utilita.Logger;

public class Utilita {
    
    /* *******************************************
     *           Membri statici
     * ********************************************/
    public final static String prefissoRisorse = "/risorse/";
    public final static String ICONA_CARTA_GIOCATORE = prefissoRisorse + "carta1.gif";
    public final static String ICONA_FORBICI_GIOCATORE = prefissoRisorse + "forbici1.gif";
    public final static String ICONA_SASSO_GIOCATORE = prefissoRisorse + "sasso1.gif";
    
    public final static String ICONA_CARTA_COMPUTER = prefissoRisorse + "carta2.gif";
    public final static String ICONA_FORBICI_COMPUTER = prefissoRisorse + "forbici2.gif";
    public final static String ICONA_SASSO_COMPUTER = prefissoRisorse + "sasso2.gif";
    
    public static String stringaIconaGiocatore(int mossa) {
        if (mossa == Mano.CARTA) {
            return ICONA_CARTA_GIOCATORE;
        } else if (mossa == Mano.FORBICI) {
            return ICONA_FORBICI_GIOCATORE;
        }
        return ICONA_SASSO_GIOCATORE;
    }
    
    public static String stringaIconaComputer(int mossa) {
        if (mossa == Mano.CARTA) {
            return ICONA_CARTA_COMPUTER;
        } else if (mossa == Mano.FORBICI) {
            return ICONA_FORBICI_COMPUTER;
        }
        return ICONA_SASSO_COMPUTER;
    }
    
    public static String nomeOggetto(int giocata) {
        if (giocata == Mano.CARTA) {
            return "Carta";
        } else if (giocata == Mano.FORBICI) {
            return "Forbici";
        }
        return "Sasso";
    }
    
    public static java.net.URL urlIcona(String nomeIcona) {
        java.net.URL url = Utilita.class.getResource(nomeIcona);
        Logger.logFine("ControlloPartita", "getFileIcona", url.toString());
        return url;
    }

    public static String stringaEsitoMano(int esitoMano) {
        if (esitoMano == Mano.MANOVINTADALGIOCATORE) {
            return "Bravo, hai vinto la mano ............";
        } else if (esitoMano == Mano.MANOVINTADALCOMPUTER) {
            return "Il computer ha vinto la mano ........";
        }   
        return "Si è verificato un pareggio .........";
    }

    public static String stringaEsitoPartita(int esitoPartita) {
        if (esitoPartita == Partita.PARTITAVINTADALGIOCATORE) {
            return "Bravo, giocatore, hai vinto la partita";
        } else if (esitoPartita == Partita.PARTITAVINTADALCOMPUTER) {
            return "Peccato, il computer ha vinto la partita";
        }   
        return "La partita è attualmente in corso";
    }

}