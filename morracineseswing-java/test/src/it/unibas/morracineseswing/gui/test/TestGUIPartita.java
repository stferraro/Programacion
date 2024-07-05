package it.unibas.morracineseswing.gui.test;

import java.util.List;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import junit.extensions.jfcunit.JFCTestCase;
import junit.extensions.jfcunit.RobotTestHelper;
import junit.extensions.jfcunit.TestHelper;
import junit.extensions.jfcunit.eventdata.JMenuMouseEventData;
import junit.extensions.jfcunit.eventdata.MouseEventData;
import junit.extensions.jfcunit.eventdata.PathData;
import junit.extensions.jfcunit.finder.Finder;
import junit.extensions.jfcunit.finder.FrameFinder;
import junit.extensions.jfcunit.finder.JMenuItemFinder;
import junit.extensions.jfcunit.finder.NamedComponentFinder;
import it.unibas.morracineseswing.refactoring.controllo.Controllo;

public class TestGUIPartita extends JFCTestCase {
    
    public static final boolean RITARDO_ABILITATO = false;
    public static final int MILLISECONDI_RITARDO = 1000;
    
    private JFrame frame;
    private JButton bottoneCarta;
    private JButton bottoneForbici;
    private JButton bottoneSasso;
    private JLabel valorePunteggioGiocatore;
    private JLabel valorePunteggioComputer;
    private JLabel valorePareggi;
    private JLabel messaggio1;
    private JLabel messaggio2;
    private JLabel iconaGiocatore;
    private JLabel iconaComputer;
    
    public void setUp() throws Exception {
        super.setUp();
        setHelper(new RobotTestHelper());
        Controllo controllo = new Controllo();
        controllo.inizializza();
        Finder finder = new FrameFinder("La Morra Cinese");
        frame = (JFrame) finder.find();
    }
    
    public void tearDown() throws Exception {
        if (frame != null) {
            frame.setVisible(false);
            frame.dispose();
            frame = null;
        }
        TestHelper.cleanUp(this);
        super.tearDown();
    }
    
    /* ***************************************
     *  Test funzionale della partita
     *************************************** */
    
    public void testGUIPartita() throws Exception {
        assertNotNull("trovato il frame", frame);
        this.valorePunteggioGiocatore = (JLabel)new NamedComponentFinder(JLabel.class, "valorePunteggioGiocatore").find(frame, 0);
        this.valorePunteggioComputer = (JLabel)new NamedComponentFinder(JLabel.class, "valorePunteggioComputer").find(frame, 0);
        this.valorePareggi = (JLabel)new NamedComponentFinder(JLabel.class, "valorePareggi").find(frame, 0);
        assertNotNull(valorePunteggioGiocatore);
        assertNotNull(valorePunteggioComputer);
        assertNotNull(valorePareggi);
        assertEquals("", valorePunteggioGiocatore.getText());
        assertEquals("", valorePunteggioComputer.getText());
        assertEquals("", valorePareggi.getText());
        this.bottoneCarta = (JButton)new NamedComponentFinder(JButton.class, "bottoneCarta").find(frame, 0);
        this.bottoneForbici = (JButton)new NamedComponentFinder(JButton.class, "bottoneForbici").find(frame, 0);
        this.bottoneSasso = (JButton)new NamedComponentFinder(JButton.class, "bottoneSasso").find(frame, 0);
        assertNotNull(bottoneCarta);
        assertNotNull(bottoneForbici);
        assertNotNull(bottoneSasso);
        assertTrue(!bottoneCarta.isEnabled());
        assertTrue(!bottoneForbici.isEnabled());
        assertTrue(!bottoneSasso.isEnabled());
        this.messaggio1 = (JLabel)new NamedComponentFinder(JLabel.class, "messaggio1").find(frame, 0);
        this.messaggio2 = (JLabel)new NamedComponentFinder(JLabel.class, "messaggio2").find(frame, 0);
        assertNotNull("messaggio1", messaggio1);
        assertNotNull("messaggio1", messaggio1);
        assertEquals("Benvenuto nel gioco della Morra Cinese", messaggio1.getText());
        assertEquals("", messaggio2.getText());
        avviaPartita();
    }
    
    private void avviaPartita() {
        JMenu menuGioco = (JMenu)new JMenuItemFinder("Gioco").find(frame, 0);
        PathData path = new PathData(new String[] {"Gioco", "Nuova Partita"});
        JMenuBar barraMenu = (JMenuBar) path.getRoot(menuGioco);
        assertNotNull("menu gioco", menuGioco);
        getHelper().enterClickAndLeave(new JMenuMouseEventData(this, barraMenu,
                path.getIndexes(barraMenu)));
        flushAWT();
        giocaPartita();
    }
    
    private void giocaPartita() {
        assertEquals("0", valorePunteggioGiocatore.getText());
        assertEquals("0", valorePunteggioComputer.getText());
        assertEquals("0", valorePareggi.getText());
        assertTrue(bottoneCarta.isEnabled());
        assertTrue(bottoneForbici.isEnabled());
        assertTrue(bottoneSasso.isEnabled());
        assertEquals("Usa i pulsanti o il menu per giocare", messaggio1.getText());
        assertEquals("", messaggio2.getText());
        getHelper().enterClickAndLeave(new MouseEventData(this, bottoneCarta));
        flushAWT();
        rallenta();
        assertEquals("La partita è attualmente in corso", messaggio2.getText());
        int giocate = 1;
        while (messaggio2.getText().equals("La partita è attualmente in corso")) {
            getHelper().enterClickAndLeave(new MouseEventData(this, bottoneCarta));
            flushAWT();
            rallenta();
            controllaPunteggi(++giocate);
        }
        assertTrue(messaggio2.getText().indexOf("vinto la partita") != -1);
        assertTrue(messaggio2.getText().indexOf("vinto la partita") != -1);
    }
    
    private void controllaPunteggi(int giocate) {
        int vittorieGiocatore = Integer.parseInt(valorePunteggioGiocatore.getText());
        int vittorieComputer = Integer.parseInt(valorePunteggioComputer.getText());
        int pareggi = Integer.parseInt(valorePareggi.getText());
        assertEquals(giocate, vittorieGiocatore + vittorieComputer + pareggi);
    }
    
    /* ***************************************
     *  Test funzionale dei punteggi
     *************************************** */
    
    public void testPunteggi() {
        JMenu menuGioco = (JMenu)new JMenuItemFinder("Gioco").find(frame, 0);
        PathData path = new PathData(new String[] {"Gioco", "Visualizza Punteggio Partite"});
        JMenuBar barraMenu = (JMenuBar) path.getRoot(menuGioco);
        assertNotNull("menu gioco", menuGioco);
        getHelper().enterClickAndLeave(new JMenuMouseEventData(this, barraMenu,
                path.getIndexes(barraMenu)));
        flushAWT();
        rallenta();
        verificaFinestraDiDialogo();
    }
    
    private void verificaFinestraDiDialogo() {
        List listaFinestreDialogo = getHelper().getShowingDialogs(frame);
        assertEquals(1, listaFinestreDialogo.size());
        JDialog dialog = (JDialog) listaFinestreDialogo.get(0);
        assertEquals("Punteggi", dialog.getTitle());
        getHelper().disposeWindow(dialog, this);
    }
    
    private void rallenta() {
        if (RITARDO_ABILITATO) {
            try {
                Thread.currentThread().sleep(MILLISECONDI_RITARDO);
            } catch (InterruptedException ex) {}
        }
    }
    
}
