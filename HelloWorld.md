# Things Needed

Testing - make sure we can run it without crashing
Resilience - might be nice to make it able to recover from a crash easier and/or restart where it left off (this is a larger change though)


## instructions
1. git clone
2. pipenv install
3. setup config file (chromedriver)
3. pipenv shell
4. python3 zoombot.py
4. if it crashes "chrome not reachable", delete the session_info file and retry

## Manual intervention
1. painful number of capchas after logging in
2. dismiss popup




Interesting:

print(element.text) might be helpful for identifying elements

java code for directly calling javascript:
WebDriver driver = new AnyDriverYouWant();

if (driver instanceof JavascriptExecutor)

 {

 ((JavascriptExecutor)driver).executeScript("yourScript();");

 } 



understanding  xpaths may help
## TODO:

- [] change activation command (easy)
-  
