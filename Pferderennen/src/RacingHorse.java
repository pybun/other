public class RacingHorse extends Horse {
	
	private double maxSpeed = 60;

	public void setMaxSpeed(double maxSpeed) {
		if(maxSpeed < 1.0)
			this.maxSpeed = 1.0;
		else if(maxSpeed > this.maxSpeed)
			this.maxSpeed = 60.0;
		else
			this.maxSpeed = maxSpeed;
	}
	
	public double getMaxSpeed() {
		return maxSpeed;
	}
	
	public String toString() {
		return ("Rennpferd #" + number + " " + name + ", Maximalgeschwindigkeit " + getMaxSpeed() + ": ");
	}
	

}
