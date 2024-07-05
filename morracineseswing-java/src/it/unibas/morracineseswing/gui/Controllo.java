package it.unibas.morracineseswing.gui;

import it.unibas.morracineseswing.modello.*;

public class Controllo extends javax.swing.JFrame {
    
    private Gioco gioco;
    private Partita partita;
    private Mano mano;
    
    /* *******************************************
     *       Componenti
     * ********************************************/
    private javax.swing.JPanel pannello;
    private javax.swing.JLabel punteggioGiocatore;
    private javax.swing.JLabel punteggioComputer;
    private javax.swing.JLabel pareggi;
    private javax.swing.JLabel valorePunteggioGiocatore;
    private javax.swing.JLabel valorePunteggioComputer;
    private javax.swing.JLabel valorePareggi;
    private javax.swing.JLabel messaggio1;
    private javax.swing.JLabel messaggio2;
    private javax.swing.JLabel iconaGiocatore;
    private javax.swing.JLabel iconaComputer;
    
    /* *******************************************
     *       Inizializzazione del frame
     * ********************************************/
    
    public void inizializza() {
        this.gioco = new Gioco();
        creaFrame();
        creaMenu();
        creaBottoniMosse();
        creaPunteggi();
        creaIconeMosse();
        creaIconeMano();
        creaMessaggi();
        this.azioneInterrompiPartita.setEnabled(false);
        this.setVisible(true);
    }
    
    private void creaFrame() {
        this.pannello = (javax.swing.JPanel)this.getContentPane();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setTitle("La Morra Cinese");
        this.setLayout(null);
        this.setSize(500, 500);
    }
    
    private void creaMenu() {
        javax.swing.JMenuBar barraMenu = new javax.swing.JMenuBar();
        this.setJMenuBar(barraMenu);
        creaMenuGioco(barraMenu);
        creaMenuPartita(barraMenu);
        creaMenuHelp(barraMenu);
    }
    
    private void creaMenuGioco(javax.swing.JMenuBar barraMenu) {
        javax.swing.JMenu menuGioco = new javax.swing.JMenu("Gioco");
        menuGioco.setMnemonic(java.awt.event.KeyEvent.VK_G);
        barraMenu.add(menuGioco);
        javax.swing.JMenuItem voceNuovaPartita =
                new javax.swing.JMenuItem(azioneNuovaPartita);
        javax.swing.JMenuItem voceInterrompiPartita =
                new javax.swing.JMenuItem(azioneInterrompiPartita);
        javax.swing.JMenuItem vocePunteggio =
                new javax.swing.JMenuItem(azionePunteggio);
        javax.swing.JMenuItem voceEsci =
                new javax.swing.JMenuItem(azioneEsci);
        menuGioco.add(voceNuovaPartita);
        menuGioco.add(voceInterrompiPartita);
        menuGioco.addSeparator();
        menuGioco.add(vocePunteggio);
        menuGioco.addSeparator();
        menuGioco.add(voceEsci);
    }
    
    private void creaMenuPartita(javax.swing.JMenuBar barraMenu) {
        javax.swing.JMenu menuPartita = new javax.swing.JMenu("Partita");
        menuPartita.setMnemonic(java.awt.event.KeyEvent.VK_P);
        barraMenu.add(menuPartita);
        javax.swing.JMenuItem voceCarta =
                new javax.swing.JMenuItem(azioneGiocataCarta);
        javax.swing.JMenuItem voceForbici =
                new javax.swing.JMenuItem(azioneGiocataForbici);
        javax.swing.JMenuItem voceSasso =
                new javax.swing.JMenuItem(azioneGiocataSasso);
        menuPartita.add(voceCarta);
        menuPartita.add(voceForbici);
        menuPartita.add(voceSasso);
    }
    
    private void creaMenuHelp(javax.swing.JMenuBar barraMenu) {
        javax.swing.JMenu menuHelp = new javax.swing.JMenu("?");
        menuHelp.setMnemonic(java.awt.event.KeyEvent.VK_H);
        barraMenu.add(menuHelp);
        javax.swing.JMenuItem voceAbout =
                new javax.swing.JMenuItem(azioneAbout);
        menuHelp.add(voceAbout);
    }
    
    private void creaPunteggi() {
        this.punteggioGiocatore = new javax.swing.JLabel();
        this.punteggioGiocatore.setBounds(30, 30, 140, 30);
        this.valorePunteggioGiocatore = new javax.swing.JLabel();
        this.valorePunteggioGiocatore.setBounds(180, 30, 10, 30);
        this.punteggioComputer = new javax.swing.JLabel();
        this.punteggioComputer.setBounds(200, 30, 150, 30);
        this.valorePunteggioComputer = new javax.swing.JLabel();
        this.valorePunteggioComputer.setBounds(360, 30, 10, 30);
        this.pareggi = new javax.swing.JLabel();
        this.pareggi.setBounds(380, 30, 60, 30);
        this.valorePareggi = new javax.swing.JLabel();
        this.valorePareggi.setBounds(450, 30, 10, 30);
        this.pannello.add(punteggioGiocatore);
        this.pannello.add(valorePunteggioGiocatore);
        this.pannello.add(punteggioComputer);
        this.pannello.add(valorePunteggioComputer);
        this.pannello.add(pareggi);
        this.pannello.add(valorePareggi);
    }
    
    private void creaBottoniMosse() {
        javax.swing.JButton bottoneCarta =
                new javax.swing.JButton(azioneGiocataCarta);
        bottoneCarta.setBounds(80, 80, 100, 30);
        javax.swing.JButton bottoneForbici =
                new javax.swing.JButton(azioneGiocataForbici);
        bottoneForbici.setBounds(200, 80, 100, 30);
        javax.swing.JButton bottoneSasso =
                new javax.swing.JButton(azioneGiocataSasso);
        bottoneSasso.setBounds(320, 80, 100, 30);
        this.pannello.add(bottoneCarta);
        this.pannello.add(bottoneForbici);
        this.pannello.add(bottoneSasso);
    }
    
    private void creaIconeMosse() {
        javax.swing.JLabel iconaCarta = new javax.swing.JLabel(
                new javax.swing.ImageIcon(Utilita.urlIcona(Utilita.ICONA_CARTA_GIOCATORE)));
        iconaCarta.setBounds(90, 120, 100, 110);
        javax.swing.JLabel iconaForbici = new javax.swing.JLabel(
                new javax.swing.ImageIcon(Utilita.urlIcona(Utilita.ICONA_FORBICI_GIOCATORE)));
        iconaForbici.setBounds(200, 120, 100, 110);
        javax.swing.JLabel iconaSasso = new javax.swing.JLabel(
                new javax.swing.ImageIcon(Utilita.urlIcona(Utilita.ICONA_SASSO_GIOCATORE)));
        iconaSasso.setBounds(310, 120, 100, 110);
        this.pannello.add(iconaCarta);
        this.pannello.add(iconaForbici);
        this.pannello.add(iconaSasso);
    }
    
    private void creaIconeMano() {
        this.iconaGiocatore = new javax.swing.JLabel();
        this.iconaGiocatore.setBounds(140, 240, 100, 110);
        this.iconaComputer = new javax.swing.JLabel();
        this.iconaComputer.setBounds(260, 240, 100, 110);
        this.pannello.add(iconaGiocatore);
        this.pannello.add(iconaComputer);
    }
    
    private void creaMessaggi() {
        this.messaggio1 = new javax.swing.JLabel();
        this.messaggio1.setBounds(150, 360, 250, 30);
        this.messaggio2 = new javax.swing.JLabel();
        this.messaggio2.setBounds(150, 400, 300, 30);
        this.pannello.add(messaggio1);
        this.pannello.add(messaggio2);
    }
    
    /* *******************************************
     *       Schermo Iniziale
     * ********************************************/
    
    public void schermoIniziale() {
        eliminaPunteggi();
        ripulisciIconeMano();
        messaggioIniziale();
    }
    
    private void ripulisciIconeMano() {
        this.iconaGiocatore.setIcon(null);
        this.iconaComputer.setIcon(null);
    }
    
    private void eliminaPunteggi() {
        this.punteggioGiocatore.setText("");
        this.valorePunteggioGiocatore.setText("");
        this.punteggioComputer.setText("");
        this.valorePunteggioComputer.setText("");
        this.pareggi.setText("");
        this.valorePareggi.setText("");
    }
    
    private void messaggioIniziale() {
        this.messaggio1.setText("Benvenuto nel gioco della Morra Cinese");
        this.messaggio2.setText("");
    }
    
    /* *******************************************
     *       Schermo Iniziale Partita
     * ********************************************/
    
    public void schermoNuovaPartita() {
        ripulisciIconeMano();
        ripulisciPunteggi();
        ripulisciMessaggi();
    }
    
    private void ripulisciPunteggi() {
        this.punteggioGiocatore.setText("Mani vinte dal giocatore :");
        this.valorePunteggioGiocatore.setText("0");
        this.punteggioComputer.setText("Mani vinte dal computer :");
        this.valorePunteggioComputer.setText("0");
        this.pareggi.setText("Pareggi :");
        this.valorePareggi.setText("0");
    }
    
    private void ripulisciMessaggi() {
        this.messaggio1.setText("Usa i pulsanti o il menu per giocare");
        this.messaggio2.setText("");
    }
    
    /* *******************************************
     *       Schermo Mano
     * ********************************************/
    
    public void schermoPartitaInCorso() {
        aggiornaPunteggi();
        aggiornaIconeMano();
        aggiornaMessaggi();
    }
    
    private void aggiornaPunteggi() {
        this.punteggioGiocatore.setText("Mani vinte dal giocatore :");
        this.valorePunteggioGiocatore.setText(partita.getManiVinteDalGiocatore() + "");
        this.punteggioComputer.setText("Mani vinte dal computer :");
        this.valorePunteggioComputer.setText(partita.getManiVinteDalComputer() + "");
        this.pareggi.setText("Pareggi :");
        this.valorePareggi.setText(partita.getPareggi() + "");
    }
    
    private void aggiornaIconeMano() {
        java.net.URL urlGiocatore = Utilita.urlIcona(Utilita.stringaIconaGiocatore(this.mano.getGiocataGiocatore()));
        javax.swing.ImageIcon immagineGiocatore = new javax.swing.ImageIcon(urlGiocatore);
        this.iconaGiocatore.setIcon(immagineGiocatore);
        java.net.URL urlComputer = Utilita.urlIcona(Utilita.stringaIconaComputer(this.mano.getGiocataComputer()));
        javax.swing.ImageIcon immagineComputer = new javax.swing.ImageIcon(urlComputer);
        this.iconaComputer.setIcon(immagineComputer);
    }
    
    private void aggiornaMessaggi() {
        this.messaggio1.setText(Utilita.stringaEsitoMano(this.mano.getEsito()));
        this.messaggio2.setText(Utilita.stringaEsitoPartita(this.partita.getStato()));
    }
    
    /* *******************************************
     *              Finestre di dialogo
     * ********************************************/
    
    public void finestraPunteggio() {
        StringBuffer messaggio = new StringBuffer();
        messaggio.append("Partite vinte dal giocatore: ");
        messaggio.append(gioco.getPartiteVinteDalGiocatore() + "\n");
        messaggio.append("\n");
        messaggio.append("Partite vinte dal computer: ");
        messaggio.append(gioco.getPartiteVinteDalComputer() + "\n");
        javax.swing.JOptionPane.showMessageDialog(this, messaggio.toString());
    }
    
    public void finestraAbout() {
        StringBuffer messaggio = new StringBuffer();
        messaggio.append("La Morra Cinese\n");
        messaggio.append("Esempio sviluppato a scopo didattico\n");
        messaggio.append("\n");
        messaggio.append("Corso di Laurea in Informatica\n");
        messaggio.append("Università della Basilicata\n");
        messaggio.append("mecca@unibas.it\n");
        javax.swing.JOptionPane.showMessageDialog(this, messaggio.toString());
    }
    
     /* *******************************************
      *              Gestori e Azioni
      * ********************************************/
    
    private AzioneNuovaPartita azioneNuovaPartita = new AzioneNuovaPartita();
    private AzioneInterrompiPartita azioneInterrompiPartita = new AzioneInterrompiPartita();
    private AzionePunteggio azionePunteggio = new AzionePunteggio();
    private AzioneEsci azioneEsci = new AzioneEsci();
    private AzioneAbout azioneAbout =  new AzioneAbout();
    private AzioneGiocata azioneGiocataCarta = new AzioneGiocata(Mano.CARTA);
    private AzioneGiocata azioneGiocataForbici = new AzioneGiocata(Mano.FORBICI);
    private AzioneGiocata azioneGiocataSasso = new AzioneGiocata(Mano.SASSO);
    
    class AzioneNuovaPartita extends javax.swing.AbstractAction {
        
        public AzioneNuovaPartita() {
            this.putValue(javax.swing.Action.NAME, "Nuova Partita");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Inizia una nuova partita");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_N));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            partita = new Partita();
            azioneNuovaPartita.setEnabled(false);
            azioneInterrompiPartita.setEnabled(true);
            azioneGiocataCarta.setEnabled(true);
            azioneGiocataForbici.setEnabled(true);
            azioneGiocataSasso.setEnabled(true);
            schermoNuovaPartita();
        }
    }
    
    class AzioneInterrompiPartita extends javax.swing.AbstractAction {
        
        public AzioneInterrompiPartita() {
            this.putValue(javax.swing.Action.NAME, "Interrompi Partita");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Interrompe la partita in corso");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_I));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            azioneNuovaPartita.setEnabled(true);
            azioneInterrompiPartita.setEnabled(false);
            azioneGiocataCarta.setEnabled(false);
            azioneGiocataForbici.setEnabled(false);
            azioneGiocataSasso.setEnabled(false);
            schermoIniziale();
        }
    }
    
    class AzionePunteggio extends javax.swing.AbstractAction {
        
        public AzionePunteggio() {
            this.putValue(javax.swing.Action.NAME, "Visualizza Punteggio Partite");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Riassume le partite vinte dal giocatore e dal computer");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_P));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            finestraPunteggio();
        }
    }
    
    class AzioneAbout extends javax.swing.AbstractAction {
        
        public AzioneAbout() {
            this.putValue(javax.swing.Action.NAME, "Informazioni sulla Morra Cinese");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Informazioni sul gioco");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_M));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            finestraAbout();
        }
    }
    
    class AzioneEsci extends javax.swing.AbstractAction {
        
        public AzioneEsci() {
            this.putValue(javax.swing.Action.NAME, "Esci");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Esce dal gioco");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_E));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            System.exit(0);
        }
    }
    
    class AzioneGiocata extends javax.swing.AbstractAction {
        
        public AzioneGiocata(int giocata) {
            this.setEnabled(false);
            this.putValue(javax.swing.Action.NAME, Utilita.nomeOggetto(giocata));
            this.putValue("giocata", new Integer(giocata));
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Gioca l'oggetto " + Utilita.nomeOggetto(giocata));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            int giocata = (Integer)this.getValue("giocata");
            mano = partita.giocaMano(giocata);
            schermoPartitaInCorso();
            if (partita.getStato() != Partita.PARTITAINCORSO) {
                gioco.gestisciPartita(partita);
                azioneGiocataCarta.setEnabled(false);
                azioneGiocataForbici.setEnabled(false);
                azioneGiocataSasso.setEnabled(false);
                azioneInterrompiPartita.setEnabled(false);
                azioneNuovaPartita.setEnabled(true);
            }
        }
    }
    
    /* *******************************************
     *              Main
     * ********************************************/
    
    public static void main(String[] args){
        javax.swing.SwingUtilities.invokeLater(
                new Runnable() {
            public void run() {
                Controllo principale = new Controllo();
                principale.inizializza();
                principale.schermoIniziale();
            }
        }
        );
    }
    
}


