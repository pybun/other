public class Race {

	public static void main(String[] args) {
		Horse[] array = new Horse[5]; // Zum anpassen Zahl im Array sowie Index – z.B „array[0]“ – anpassen
		
		array[0] = new Horse() {
			{
				name = "Max";
			}
		};
		
		array[1] = new Horse() {
			{
				name = "Anton";
			}
		};
		
		array[2] = new Horse() {
			{
				name = "Claudia";
			}
		};
		
		array[3] = new RacingHorse() {
			{
				name = "Wirbelwind";
			}
		};
		
		array[4] = new Champion(5) {
			{
				name = "Eclipse";
			}
		};
		
		double[] values = new double[array.length];
		
		for(int i=0; i<array.length; i++) {
			array[i].number += 1;
			float run = 0;
			for(int j=0; j<10; j++) {
				run += array[i].gallop(array[i].getMaxSpeed());
			}
			values[i] = run;
			System.out.println(array[i].toString() + Math.round(run) + " Meter");
		}
		
		int maxAt = 0;

		for(int i=0; i<array.length; i++) {
		    if(values[i] > values[maxAt])
				maxAt = i;
			else
				maxAt = maxAt;
		}
		
		System.out.println("\nGewinner: " + array[maxAt].name);
		
	}

}

/*

Mit „array[x].setMaxSpeed(x);“ kann man – wie von der Aufgabenstellung verlangt – die Maximalgeschwindigkeit individuell anpassen.

*/
