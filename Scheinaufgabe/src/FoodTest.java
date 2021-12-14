import java.io.FileNotFoundException;

public class FoodTest {

	public static void main(String[] args) throws FileNotFoundException {
		Food nutella = new Food("Nutella", 539, 30.9, 56.3, 0.107);
		Food stangensellerie = new Food("Stangensellerie", 19, 0.3, 0.7, 0.3175);
		Food rindersteak = new Food("Rindersteak", 133, 5.6, 0, 0.4);
		
		System.out.println(nutella.toString());
		System.out.println(stangensellerie.toString());
		System.out.println(rindersteak.toString());
		
		System.out.println("");
		
		Person mirjamMuster = new Person("Mirjam Muster");
		mirjamMuster.consume(nutella);
		mirjamMuster.consume(rindersteak);
		System.out.println(mirjamMuster.toString());
		mirjamMuster.saveFile();
		
		Person maxMustermann = new Person("Max Mustermann");
		maxMustermann.consume(nutella);
		maxMustermann.consume(stangensellerie);
		maxMustermann.consume(rindersteak);
		System.out.println(maxMustermann.toString());
		maxMustermann.saveFile();
	}

}
