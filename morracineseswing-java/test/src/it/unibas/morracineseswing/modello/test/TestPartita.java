package it.unibas.morracineseswing.modello.test;

import junit.framework.*;
import it.unibas.morracineseswing.modello.*;

public class TestPartita extends TestCase {

    private Partita partita;
    private int pareggi;
    private int vittorieComputer;
    private int vittorieGiocatore;

    public void setUp() {
        partita = new Partita();
        pareggi = 0;
        vittorieComputer = 0;
        vittorieGiocatore = 0;
    }

    public void testPartita1() {
        verificaPunteggi(0, 0, 0);
        verificaManoCarta();
        verificaManoForbici();
        verificaManoSasso();
        while (partita.getStato() == Partita.PARTITAINCORSO) {
            verificaManoCarta();
        }
        if (vittorieComputer > vittorieGiocatore) {
            Assert.assertTrue("vince il computer", partita.getStato() == Partita.PARTITAVINTADALCOMPUTER);
            Assert.assertTrue("punti computer", partita.getManiVinteDalComputer() == Partita.LIMITEMANI);
        } else {
            Assert.assertTrue("vince il computer", partita.getStato() == Partita.PARTITAVINTADALGIOCATORE);
            Assert.assertTrue("punti giocatore", partita.getManiVinteDalGiocatore() == Partita.LIMITEMANI);
        }
    }

    public void testPartita2() {
        verificaPunteggi(0, 0, 0);
        while (partita.getStato() == Partita.PARTITAINCORSO) {
            verificaManoCarta();
        }
        try {
            verificaManoCarta();
            Assert.fail();
        } catch (java.lang.AssertionError e) {}
    }

    private void verificaManoCarta() {
        Mano mano = partita.giocaMano(Mano.CARTA);
        if (mano.getGiocataComputer() == Mano.CARTA) {
            verificaPunteggi(++pareggi, vittorieComputer, vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.FORBICI) {
            verificaPunteggi(pareggi, ++vittorieComputer, vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.SASSO) {
            verificaPunteggi(pareggi, vittorieComputer, ++vittorieGiocatore);
        }
    }

    private void verificaManoForbici() {
        Mano mano = partita.giocaMano(Mano.FORBICI);
        if (mano.getGiocataComputer() == Mano.CARTA) {
            verificaPunteggi(pareggi, vittorieComputer, ++vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.FORBICI) {
            verificaPunteggi(++pareggi, vittorieComputer, vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.SASSO) {
            verificaPunteggi(pareggi, ++vittorieComputer, vittorieGiocatore);
        }
    }

    private void verificaManoSasso() {
        Mano mano = partita.giocaMano(Mano.SASSO);
        if (mano.getGiocataComputer() == Mano.CARTA) {
            verificaPunteggi(pareggi, ++vittorieComputer, vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.FORBICI) {
            verificaPunteggi(pareggi, vittorieComputer, ++vittorieGiocatore);
        } else if (mano.getGiocataComputer() == Mano.SASSO) {
            verificaPunteggi(++pareggi, vittorieComputer, vittorieGiocatore);
        }
    }

    private void verificaPunteggi(int pareggi, int vittorieComputer, int vittorieGiocatore) {
        Assert.assertTrue("pareggi", partita.getPareggi() == pareggi);
        Assert.assertTrue("mani vinte dal computer", partita.getManiVinteDalComputer() == vittorieComputer);
        Assert.assertTrue("mani vinte dal giocatore", partita.getManiVinteDalGiocatore() == vittorieGiocatore);
    }
}
