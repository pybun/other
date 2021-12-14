import java.io.PrintWriter;

public class Person {
	
	public double energie;
	public double fett;
	public double zucker;
	public double salz;
	public String name;
	
	public Person(String name) {
		this.name = name;
	}
	
	void consume(Food f, double amountInGrams) {
		energie += f.energie;
		fett += (f.fett / 100) * amountInGrams;
		zucker += (f.zucker / 100) * amountInGrams;
		salz += (f.salz / 100) * amountInGrams;
	}
	
	void consume(Food f) {
		energie += f.energie;
		fett += f.fett;
		zucker += f.zucker;
		salz += f.salz;
	}
	
	public String toString() {
		return name + " - Aufgenommene Nährwerte - Energie: " + energie + " kcal, Fett: " + fett + "g, Zucker " + zucker + "g, Salz: " + salz + "g";
	}
	
	public boolean saveFile() {
		try(PrintWriter pw = new PrintWriter(name + ".txt")) {
			pw.println(toString());
			return true;
		}
		catch(Exception e) {
			return false;
		}
		
	}

}
