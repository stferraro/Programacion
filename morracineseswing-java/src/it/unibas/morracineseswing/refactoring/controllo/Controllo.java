package it.unibas.morracineseswing.refactoring.controllo;

import it.unibas.morracineseswing.refactoring.modello.*;
import it.unibas.morracineseswing.refactoring.vista.Utilita;
import it.unibas.morracineseswing.refactoring.vista.Vista;

public class Controllo {
    
    private Vista vista;
    private Modello modello;
    
    public Controllo() {
        this.modello = new Modello();
        this.modello.setGioco(new Gioco());
        this.vista = new Vista(this, modello);
    }
    
    public void inizializza() {
        abilitaAzioniNuovaPartita();
        vista.inizializza();
        vista.getPannelloPrincipale().schermoIniziale();        
    }
    
    public Vista getVista() {
        return this.vista;
    }
    
    public Modello getModello() {
        return this.modello;
    }

    /* ************************************
     *      Proprieta' per le azioni
     * ********************************** */
    
    private AzioneNuovaPartita azioneNuovaPartita = new AzioneNuovaPartita();
    private AzioneInterrompiPartita azioneInterrompiPartita = new AzioneInterrompiPartita();
    private AzionePunteggio azionePunteggio = new AzionePunteggio();
    private AzioneEsci azioneEsci = new AzioneEsci();
    private AzioneAbout azioneAbout = new AzioneAbout();
    private AzioneGiocata azioneGiocataCarta = new AzioneGiocata(Mano.CARTA);
    private AzioneGiocata azioneGiocataForbici = new AzioneGiocata(Mano.FORBICI);
    private AzioneGiocata azioneGiocataSasso = new AzioneGiocata(Mano.SASSO);
            
    public AzioneAbout getAzioneAbout() {
        return this.azioneAbout;
    }

    public AzioneEsci getAzioneEsci() {
        return this.azioneEsci;
    }

    public AzioneGiocata getAzioneGiocataCarta() {
        return this.azioneGiocataCarta;
    }

    public AzioneGiocata getAzioneGiocataForbici() {
        return this.azioneGiocataForbici;
    }

    public AzioneGiocata getAzioneGiocataSasso() {
        return this.azioneGiocataSasso;
    }

    public AzioneInterrompiPartita getAzioneInterrompiPartita() {
        return this.azioneInterrompiPartita;
    }

    public AzioneNuovaPartita getAzioneNuovaPartita() {
        return this.azioneNuovaPartita;
    }

    public AzionePunteggio getAzionePunteggio() {
        return this.azionePunteggio;
    }

    private void abilitaAzioniNuovaPartita() {
        this.azioneNuovaPartita.setEnabled(true);
        this.azioneInterrompiPartita.setEnabled(false);
        this.azioneGiocataCarta.setEnabled(false);
        this.azioneGiocataForbici.setEnabled(false);
        this.azioneGiocataSasso.setEnabled(false);
    }
    
    private void abilitaAzioniPartitaInCorso() {
        this.azioneNuovaPartita.setEnabled(false);
        this.azioneInterrompiPartita.setEnabled(true);
        this.azioneGiocataCarta.setEnabled(true);
        this.azioneGiocataForbici.setEnabled(true);
        this.azioneGiocataSasso.setEnabled(true);
    }
    
    /* *******************************************
     *              Main
     * ********************************************/
    
    public static void main(String[] args){
        javax.swing.SwingUtilities.invokeLater(
                new Runnable() {
            public void run() {
                Controllo controllo = new Controllo();
                controllo.inizializza();
            }
        }
        );
    }
    
   /* *******************************************
    *       Classi delle azioni
    * ********************************************/
    
    class AzioneNuovaPartita extends javax.swing.AbstractAction {
        public AzioneNuovaPartita() {
            this.putValue(javax.swing.Action.NAME, "Nuova Partita");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Inizia una nuova partita");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_N));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            modello.setPartita(new Partita());
            abilitaAzioniPartitaInCorso();
            vista.getPannelloPrincipale().schermoNuovaPartita();
        }
    }
    
    class AzioneInterrompiPartita extends javax.swing.AbstractAction {
        public AzioneInterrompiPartita() {
            this.putValue(javax.swing.Action.NAME, "Interrompi Partita");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Interrompe la partita in corso");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_I));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            abilitaAzioniNuovaPartita();
            vista.getPannelloPrincipale().schermoIniziale();
        }
    }
    
    class AzionePunteggio extends javax.swing.AbstractAction {
        public AzionePunteggio() {
            this.putValue(javax.swing.Action.NAME, "Visualizza Punteggio Partite");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Riassume le partite vinte dal giocatore e dal computer");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_P));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            vista.finestraPunteggio();
        }
    }
    
    class AzioneAbout extends javax.swing.AbstractAction {
        public AzioneAbout() {
            this.putValue(javax.swing.Action.NAME, "Informazioni sulla Morra Cinese");
            this.putValue(javax.swing.Action.SHORT_DESCRIPTION, "Informazioni sul gioco");
            this.putValue(javax.swing.Action.MNEMONIC_KEY, new Integer(java.awt.event.KeyEvent.VK_M));
        }
        
        public void actionPerformed(java.awt.event.ActionEvent e) {
            vista.finestraInformazioni();
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
            Partita partita = modello.getPartita();
            Mano mano = partita.giocaMano(giocata);
            modello.setMano(mano);
            if (partita.getStato() != Partita.PARTITAINCORSO) {
                Gioco gioco = modello.getGioco();
                gioco.gestisciPartita(partita);
                abilitaAzioniNuovaPartita();
            }
            vista.getPannelloPrincipale().schermoPartitaInCorso();
        }
        
    }
    
}