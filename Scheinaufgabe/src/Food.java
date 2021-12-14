public class Food {
	
	public String name;
	public double energie;
	public double fett;
	public double zucker;
	public double salz;
	
	public Food(String name, double energie, double fett, double zucker, double salz) {
		this.name = name;
		this.energie = energie;
		this.fett = fett;
		this.zucker = zucker;
		this.salz = salz;
	}

	public String getFett() {
		if(fett < 3)
			return "grün";
		else if(fett >= 3 & fett <= 17.5)
			return "gelb";
		else
			return "rot";
	}
	
	public String getZucker() {
		if(zucker < 5)
			return "grün";
		else if(zucker >= 5 & zucker <= 22.5)
			return "gelb";
		else
			return "rot";
	}
	
	public String getSalz() {
		if(salz < 0.3)
			return "grün";
		else if(salz >= 0.3 & salz <= 1.5)
			return "gelb";
		else
			return "rot";
	}
	
	public String toString() {
		return name + " - Energie: " + energie + " kcal, Fett: " + fett + "g (" + getFett() + "), Zucker: " + zucker + "g (" + getZucker() + "), Salz: " + salz + ("g (" + getSalz() + ")");
	}

}
