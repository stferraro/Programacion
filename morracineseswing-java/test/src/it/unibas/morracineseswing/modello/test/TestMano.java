package it.unibas.morracineseswing.modello.test;

import junit.framework.*;
import it.unibas.morracineseswing.modello.Mano;

public class TestMano extends TestCase {

    private Mano mano;

    public void setUp() {
        mano = new Mano();
    }

    public void testIsValida() {
        Assert.assertTrue("carta", mano.isValida(Mano.CARTA));
        Assert.assertTrue("forbici", mano.isValida(Mano.FORBICI));
        Assert.assertTrue("sasso", mano.isValida(Mano.SASSO));
        Assert.assertTrue("non valido a", !mano.isValida(Mano.CARTA - 1));
        Assert.assertTrue("non valido b", !mano.isValida(Mano.SASSO + 1));
    }

    public void testGioca1() {
        mano.gioca(Mano.CARTA);
        if (mano.getGiocataComputer() == Mano.CARTA) {
            Assert.assertTrue("pareggio", mano.getEsito() == Mano.MANOINPAREGGIO);
        } else if (mano.getGiocataComputer() == Mano.SASSO) {
            Assert.assertTrue("vince il giocatore", mano.getEsito() == Mano.MANOVINTADALGIOCATORE);
        } else if (mano.getGiocataComputer() == Mano.FORBICI) {
            Assert.assertTrue("vince il computer", mano.getEsito() == Mano.MANOVINTADALCOMPUTER);
        }
    }

    public void testGioca2() {
        mano.gioca(Mano.FORBICI);
        if (mano.getGiocataComputer() == Mano.FORBICI) {
            Assert.assertTrue("pareggio", mano.getEsito() == Mano.MANOINPAREGGIO);
        } else if (mano.getGiocataComputer() == Mano.CARTA) {
            Assert.assertTrue("vince il giocatore", mano.getEsito() == Mano.MANOVINTADALGIOCATORE);
        } else if (mano.getGiocataComputer() == Mano.SASSO) {
            Assert.assertTrue("vince il computer", mano.getEsito() == Mano.MANOVINTADALCOMPUTER);
        }
    }

    public void testGioca3() {
        mano.gioca(Mano.SASSO);
        if (mano.getGiocataComputer() == Mano.SASSO) {
            Assert.assertTrue("pareggio", mano.getEsito() == Mano.MANOINPAREGGIO);
        } else if (mano.getGiocataComputer() == Mano.FORBICI) {
            Assert.assertTrue("vince il giocatore", mano.getEsito() == Mano.MANOVINTADALGIOCATORE);
        } else if (mano.getGiocataComputer() == Mano.CARTA) {
            Assert.assertTrue("vince il computer", mano.getEsito() == Mano.MANOVINTADALCOMPUTER);
        }
    }

    public void testGiocateComputer() {
        int[] statistica = new int[4];
        for (int i = 0; i < 20; i++) {
            mano.gioca(Mano.CARTA);
            statistica[mano.getGiocataComputer()]++;
        }
        Assert.assertTrue("tutti gli oggetti", statistica[Mano.CARTA] != 0);
        Assert.assertTrue("tutti gli oggetti", statistica[Mano.FORBICI] != 0);
        Assert.assertTrue("tutti gli oggetti", statistica[Mano.SASSO] != 0);
    }

}
