import java.util.Scanner;
import java.io.FileReader;
import java.util.ArrayList;
import java.io.FileWriter;

public class FileIO {

	public static String[] read(String file) {
		// Fügt jede Zeile zusammen
		StringBuilder sb = new StringBuilder();
		
		// Ließt die Eingaben (z. B. „bar.txt“ und „foo.txt“) zeilenweise ein und fügt diese dem „StringBuilder“ hinzu
		try (Scanner in = new Scanner(new FileReader(file))) {
			while(in.hasNextLine())
		        sb.append(in.nextLine());
		}
		// Wenn die Datei nicht gefunden wurde, wird eine entsprechende Meldung geworfen
		catch (Exception e) {
			System.out.println("„" + file + "“ nicht gefunden.");
		}
	    
		// Der gelesene Inhalt wird anhand eines Kommatas getrennt und als „Array“ zurückgegeben
		return sb.toString().split(",");
	}
	
	public static void main(String[] args) {
		// Scanner zum Einlesen der Eingaben
		Scanner sc = new Scanner(System.in);
		System.out.print("Bitte geben Sie den Dateinamen einer Datei mit Zahlen ein: ");
		String firstInput = sc.nextLine();
		System.out.print("Bitte geben Sie den Dateinamen einer weiteren Datei mit Zahlen ein: ");
		String secondInput = sc.nextLine();
		System.out.print("Bitte geben Sie den Dateinamen zum Speichern der gemeinsamen Zahlen ein: ");
		String thirdInput = sc.nextLine();
		
		// Aufruf der Methode „read“ um Redundanzen zu vermeiden
		String[] first = read(firstInput);
		String[] second = read(secondInput);
		// Liste zum Hinzufügen gemeinsamer Elemente
		ArrayList<String> third = new ArrayList<String>();
		
		// Durchläuft die erste mit dem zweiten „Array“ und prüft, ob Inhalte gleich sind
		// Wenn Duplikate auftreten, werden diese nicht weiter behandelt – in der Aufgabenstellung steht, dass Duplikate ignoriert werden dürfen
		for (int i=0; i<first.length; i++) {
			for (int j=0; j<second.length; j++) {
				// Wenn der Inhalt gleich ist, wird dieser „third“ hinzugefügt
				if (first[i].equals(second[j]))
					third.add(first[i]);
			}
		}
		
		// Die Datei – wo gemeinsame Elemente hineingeschrieben werden – wird erstellt
		try (FileWriter fw = new FileWriter(thirdInput)) {
			for (int i=0; i<third.size(); i++)
				fw.write(third.get(i) + ",");
		}
		catch (Exception e) { }
	}

}