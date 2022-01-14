public class Horse {

	public String name;
	public static int number;
	private double maxSpeed = 40;
	
	public String getName() {
		return name;
	}
	
	public void setMaxSpeed(double maxSpeed) {
		if(maxSpeed < 1.0)
			this.maxSpeed = 1.0;
		else if(maxSpeed > this.maxSpeed)
			this.maxSpeed = 40.0;
		else
			this.maxSpeed = maxSpeed;
	}
	
	public double getMaxSpeed() {
		return maxSpeed;
	}
	
	public String toString() {
		return ("Pferd #" + number + " " + name + ", Maximalgeschwindigkeit " + getMaxSpeed() + ": ");
	}
	
	public double gallop(double maxSpeed) {
		return ((1 + (int)(Math.random() * ((maxSpeed - 1) + 1))) * 1000) / 60;
	}

}

/*

„name“ sowie „number“ öffentlich, da laut Aufgabenstellung hier keine Konstruktoren vererbt werden dürfen.

Dadurch entfällt außerdem die Erstellung von „get“-Methoden dieser Variablen; „set“-Methoden entfallen ohnehin
aufgrund „nicht mehr veränderbar sein.“ in der Aufgabenstellung.

*/