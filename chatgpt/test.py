

We would need to see the HTML code for the web page to provide an accurate answer.


This cannot be done with a single code. You will have to create 5 different codes, each for testing a different form element.


Assuming that the form has been given an id of "myForm":

driver.find_element_by_id("myForm").submit()


public class SeleniumTest {

public static void main(String[] args) {

WebDriver driver = new FirefoxDriver();

driver.get("http://www.google.com/");

WebElement element = driver.findElement(By.name("q"));

element.sendKeys("Cheese!");

element.submit();

}

}
