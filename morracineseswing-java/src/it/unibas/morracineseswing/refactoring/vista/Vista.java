package it.unibas.morracineseswing.refactoring.vista;

import it.unibas.morracineseswing.refactoring.modello.*;
import it.unibas.morracineseswing.refactoring.controllo.Controllo;

public class Vista extends javax.swing.JFrame {
    
    private Modello modello;
    private Controllo controllo;
    private SchermoPrincipale pannello;
    
    public Vista() {}
    
    public Vista(Controllo controllo, Modello modello) {
        this.modello = modello;
        this.controllo = controllo;
    }
    
    public Controllo getControllo() {
        return this.controllo;
    }
    
    public Modello getModello() {
        return this.modello;
    }
    
    public SchermoPrincipale getPannelloPrincipale() {
        return this.pannello;
    }

    /* *******************************************
     *       Frame principale 
     * ********************************************/

    public void inizializza() {
        creaMenu();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setTitle("La Morra Cinese");
        this.setLayout(null);
        this.setSize(500, 500);
        this.pannello = new SchermoPrincipale(this);
        this.pannello.inizializza();
        this.getContentPane().add(this.pannello);
        this.setVisible(true);        
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
                new javax.swing.JMenuItem(controllo.getAzioneNuovaPartita());
        javax.swing.JMenuItem voceInterrompiPartita = 
                new javax.swing.JMenuItem(controllo.getAzioneInterrompiPartita());
        javax.swing.JMenuItem vocePunteggio = 
                new javax.swing.JMenuItem(controllo.getAzionePunteggio());
        javax.swing.JMenuItem voceEsci = 
                new javax.swing.JMenuItem(controllo.getAzioneEsci());
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
                new javax.swing.JMenuItem(controllo.getAzioneGiocataCarta());
        javax.swing.JMenuItem voceForbici = 
                new javax.swing.JMenuItem(controllo.getAzioneGiocataForbici());
        javax.swing.JMenuItem voceSasso = 
                new javax.swing.JMenuItem(controllo.getAzioneGiocataSasso());
        menuPartita.add(voceCarta);
        menuPartita.add(voceForbici);
        menuPartita.add(voceSasso);
    }

    private void creaMenuHelp(javax.swing.JMenuBar barraMenu) {
        javax.swing.JMenu menuHelp = new javax.swing.JMenu("?");
        menuHelp.setMnemonic(java.awt.event.KeyEvent.VK_H);
        barraMenu.add(menuHelp);
        javax.swing.JMenuItem voceAbout = 
                new javax.swing.JMenuItem(controllo.getAzioneAbout());
        menuHelp.add(voceAbout);
    }

    /* *******************************************
     *              Finestre di dialogo
     * ********************************************/

    public void finestraPunteggio() {
        Gioco gioco = modello.getGioco();
        StringBuffer messaggio = new StringBuffer();
        messaggio.append("Partite vinte dal giocatore: ");
        messaggio.append(gioco.getPartiteVinteDalGiocatore() + "\n");
        messaggio.append("\n");
        messaggio.append("Partite vinte dal computer: ");
        messaggio.append(gioco.getPartiteVinteDalComputer() + "\n");
        javax.swing.JOptionPane.showMessageDialog(this, messaggio.toString(), "Punteggi", javax.swing.JOptionPane.INFORMATION_MESSAGE);
    }
    
    public void finestraInformazioni() {
        StringBuffer messaggio = new StringBuffer();
        messaggio.append("La Morra Cinese\n");
        messaggio.append("Esempio sviluppato a scopo didattico\n");
        messaggio.append("\n");
        messaggio.append("Corso di Laurea in Informatica\n");
        messaggio.append("Università della Basilicata\n");
        messaggio.append("mecca@unibas.it\n");
        javax.swing.JOptionPane.showMessageDialog(this, messaggio.toString(), "Informazioni", javax.swing.JOptionPane.INFORMATION_MESSAGE);
    }

           
}


