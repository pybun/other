public class ClientServerCommunication {
	
	public static void main(String[] args) throws InterruptedException {
		
		// Attribut
		int number = 6;
		
		// Erzeugt und startet Instanz der „Server“-Klasse mit „number“
		Server s = new Server(number);
		s.start();
		
		// Erzeugt und startet „number“ Instanzen der „Client“-Klasse
		for(int i=0; i<number; i++) {
			Client c = new Client();
			c.start();
			c.join();
		}
		
    }
}