import java.net.Socket;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Client extends Thread {

	public void run() {
		
		// Es ist nicht möglich, „extends“ und „throws“ gleichzeitig zu nutzen – deshalb der „try“-Block
		try {
			// „Client“ kreieren
			Socket s = new Socket("localhost", 8081);
			
			// „OutputStream“, da später etwas gesendet wird
			PrintWriter pw = new PrintWriter(s.getOutputStream());
			
			// „Scanner“ für die Eingabe des Nutzers
			Scanner sc = new Scanner(System.in);
			System.out.print("Bitte Ziffer eingeben ('x' für Exit): ");
	        String i = sc.next();
	        
	        // Dem Server etwas senden
	        pw.println(i + "\n");
	        pw.flush();
		} catch (IOException e) { System.out.println(e); }
		
	}
	
}