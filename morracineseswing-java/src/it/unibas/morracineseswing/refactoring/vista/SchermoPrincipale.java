package it.unibas.morracineseswing.refactoring.vista;

import it.unibas.morracineseswing.refactoring.modello.*;
import it.unibas.morracineseswing.refactoring.controllo.Controllo;

public class SchermoPrincipale extends javax.swing.JPanel {
    
    private Modello modello;
    private Vista vista;
    private Controllo controllo;

    public SchermoPrincipale(Vista vista) {
        this.vista = vista;
        this.modello = vista.getModello();
        this.controllo = vista.getControllo();
    }
    
    /* *******************************************
     *       Componenti 
     * ********************************************/
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
        this.setLayout(null);
        this.setBounds(0, 0, 500, 500);
        creaBottoniMosse();
        creaPunteggi();
        creaIconeMosse();
        creaIconeMano();
        creaMessaggi();
    }
        
    private void creaPunteggi() {
        this.punteggioGiocatore = new javax.swing.JLabel();
        this.punteggioGiocatore.setBounds(30, 30, 140, 30);
        this.valorePunteggioGiocatore = new javax.swing.JLabel();
        this.valorePunteggioGiocatore.setName("valorePunteggioGiocatore");
        this.valorePunteggioGiocatore.setBounds(180, 30, 10, 30);
        this.punteggioComputer = new javax.swing.JLabel();
        this.punteggioComputer.setBounds(200, 30, 150, 30);
        this.valorePunteggioComputer = new javax.swing.JLabel();
        this.valorePunteggioComputer.setName("valorePunteggioComputer");
        this.valorePunteggioComputer.setBounds(360, 30, 10, 30);
        this.pareggi = new javax.swing.JLabel();
        this.pareggi.setBounds(380, 30, 60, 30);
        this.valorePareggi = new javax.swing.JLabel();
        this.valorePareggi.setBounds(450, 30, 10, 30);
        this.valorePareggi.setName("valorePareggi");
        this.add(punteggioGiocatore);
        this.add(valorePunteggioGiocatore);
        this.add(punteggioComputer);
        this.add(valorePunteggioComputer);
        this.add(pareggi);
        this.add(valorePareggi);
    }
    
    private void creaBottoniMosse() {
        javax.swing.JButton bottoneCarta = 
                new javax.swing.JButton(controllo.getAzioneGiocataCarta());
        bottoneCarta.setName("bottoneCarta");
        bottoneCarta.setBounds(80, 80, 100, 30);
        javax.swing.JButton bottoneForbici = 
                new javax.swing.JButton(controllo.getAzioneGiocataForbici());
        bottoneForbici.setName("bottoneForbici");
        bottoneForbici.setBounds(200, 80, 100, 30);
        javax.swing.JButton bottoneSasso = 
                new javax.swing.JButton(controllo.getAzioneGiocataSasso());
        bottoneSasso.setName("bottoneSasso");
        bottoneSasso.setBounds(320, 80, 100, 30);
        this.add(bottoneCarta);
        this.add(bottoneForbici);
        this.add(bottoneSasso);
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
        this.add(iconaCarta);
        this.add(iconaForbici);
        this.add(iconaSasso);
    }
    
    private void creaIconeMano() {
        this.iconaGiocatore = new javax.swing.JLabel();
        this.iconaGiocatore.setBounds(140, 240, 100, 110);
        this.iconaComputer = new javax.swing.JLabel();
        this.iconaComputer.setBounds(260, 240, 100, 110);
        this.add(iconaGiocatore);
        this.add(iconaComputer);
    }

    private void creaMessaggi() {
        this.messaggio1 = new javax.swing.JLabel();
        this.messaggio1.setName("messaggio1");
        this.messaggio1.setBounds(150, 360, 250, 30);
        this.messaggio2 = new javax.swing.JLabel();
        this.messaggio2.setName("messaggio2 ");
        this.messaggio2.setBounds(150, 400, 300, 30);
        this.add(messaggio1);
        this.add(messaggio2);
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
        Partita partita = modello.getPartita();
        this.punteggioGiocatore.setText("Mani vinte dal giocatore :");
        this.valorePunteggioGiocatore.setText(partita.getManiVinteDalGiocatore() + "");
        this.punteggioComputer.setText("Mani vinte dal computer :");
        this.valorePunteggioComputer.setText(partita.getManiVinteDalComputer() + "");
        this.pareggi.setText("Pareggi :");
        this.valorePareggi.setText(partita.getPareggi() + "");
    }

    private void aggiornaIconeMano() {
        Mano ultimaMano = modello.getMano();
        java.net.URL urlGiocatore = Utilita.urlIcona(Utilita.stringaIconaGiocatore(ultimaMano.getGiocataGiocatore()));
        javax.swing.ImageIcon immagineGiocatore = new javax.swing.ImageIcon(urlGiocatore);
        this.iconaGiocatore.setIcon(immagineGiocatore);
        java.net.URL urlComputer = Utilita.urlIcona(Utilita.stringaIconaComputer(ultimaMano.getGiocataComputer()));
        javax.swing.ImageIcon immagineComputer = new javax.swing.ImageIcon(urlComputer);
        this.iconaComputer.setIcon(immagineComputer);
    }

    private void aggiornaMessaggi() {
        Partita partita = modello.getPartita();
        Mano ultimaMano = modello.getMano();
        this.messaggio1.setText(Utilita.stringaEsitoMano(ultimaMano.getEsito()));
        this.messaggio2.setText(Utilita.stringaEsitoPartita(partita.getStato()));
    }    
}
