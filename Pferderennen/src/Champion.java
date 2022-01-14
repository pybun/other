public class Champion extends RacingHorse{
	
	private double maxSpeed = 75;
	private int stars;
	
	public Champion(int stars) {
		if(stars < 1)
			this.stars = 1;
		else if(stars > 5)
			this.stars = 5;
		else
			this.stars = stars;
	}
	
	public void setMaxSpeed(double maxSpeed) {
		if(maxSpeed < 1.0)
			this.maxSpeed = 1.0;
		else if(maxSpeed > this.maxSpeed)
			this.maxSpeed = 75.0;
		else
			this.maxSpeed = maxSpeed;
	}
	
	public double getMaxSpeed() {
		return maxSpeed;
	}
	
	public int getStars() {
		return stars;
	}
	
	public String toString() {
		return ("Champion (" + "*".repeat(getStars()) + ") #" + number + " " + name + ", Maximalgeschwindigkeit " + getMaxSpeed() + ": ");
	}

}
