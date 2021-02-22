package pkgDemo;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
//import io.github.bonigarcia.wdm.WebDriverManager;

public class OpenGoogle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//WebDriverManager.chromeDriver().setup();
		ChromeDriver chromeDriver = new ChromeDriver();
		chromeDriver.manage().window().maximize();
		chromeDriver.get("https://www.facebook.com");	
		chromeDriver.findElement(By.id("email")).sendKeys("your_email_id");
		chromeDriver.findElement(By.id("pass")).sendKeys("password");
		chromeDriver.manage().timeouts().implicitlyWait(40, TimeUnit.SECONDS);
		chromeDriver.findElement(By.name("login")).click();
		chromeDriver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);	
		//chromeDriver.quit();
	}

}
