import java.net.ServerSocket;
import java.io.IOException;
import java.net.Socket;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Server extends Thread {
	
	// Attribut
	private int number;
	
	// Konstruktor, damit der „Server“ im Anschluss schließt
	public Server(int number) {
		this.number = number;
	}
	
	public void run() {
		
		// Es ist nicht möglich, „extends“ und „throws“ gleichzeitig zu nutzen – deshalb der „try“-Block
		try {
			// „Server“ kreieren
			ServerSocket ss = new ServerSocket(8081);
			
			// Schleife um nach „number“-Durchläufen den „Server“ zu schließen
			for(int i=0; i<number; i++) {
				// Verbindung mit dem Client
				Socket s = ss.accept();
				
				System.out.println("Verbindung zu 127.0.0.1 an Port 8081.");
				
				// „InputStream“, um das gesendete zu empfangen
				InputStreamReader in = new InputStreamReader(s.getInputStream());
				BufferedReader br = new BufferedReader(in);
				String str = br.readLine();
				
				if(str.equals("x"))
					continue;
				
				System.out.println("server: " + str);
			}
			
			System.out.println("\nProcess finished with exit code 0");
			System.exit(0);
			
		} catch (IOException e) { System.out.println(e); }
		
	}
	
}