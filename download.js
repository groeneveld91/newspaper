var system = require('system');
var args = system.args;

var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'
page.customHeaders = {
	"Referer" : 'http://www.google.com'
};
page.open(args[1], function() {
  console.log(page.content);
  phantom.exit();
});