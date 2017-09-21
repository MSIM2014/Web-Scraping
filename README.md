# Web-Scraping
These are several coding exercises with web scraping. Used Python libraries include urllib2, BeautifulSoup, requests, lxml, csv and datetime.

1. Login is not required when accessing the url. For example, StockScraping.py.
2. Login is required when accessing the url. For example, atlassian.py, yelp.py. The most confusing part is to do with csrf token in regards to how to pass it to the post request. So far, only login name, password and csrf token submitted through form in POST is handled.

For example,

 <form action="/login" class="yform" id="ajax-login" method="POST">
        <input     type="hidden"    name="csrftok"    class="csrftok" value="cc0e797ca9b2659794c029e74c2ca81799f06e61e21fa7e412ca3a5643ef778f">
                <label class="placeholder-sub">Email</label>
                <input id="email" name="email" placeholder="Email" required="required" type="email" value="">
                <label class="placeholder-sub">Password</label>
                <input id="password" name="password" placeholder="Password" required="required" type="password" value="">
                <div class="forgot-password">
                    <a href="/forgot" class="forgot-link">Forgot password?</a></small>
                </div>
                <div class="captcha login-captcha"></div>
                <button type="submit" value="submit" class="ybtn ybtn--primary submit ybtn-full"><span>Log In</span></button>
    </form>
 
