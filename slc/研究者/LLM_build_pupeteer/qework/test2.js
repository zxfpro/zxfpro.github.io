const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const timeout = 4000;

(async () => {
    const browser = await puppeteer.launch({
        headless: false, // 非无头模式
        // executablePath: '/Applications/Google Chrome.app/Contents/MacOS',
        executablePath: '/Users/zhaoxuefeng/.cache/puppeteer/chrome/mac_arm-121.0.6167.85/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing',
        // userDataDir: '/Users/zhaoxuefeng/Library/Application Support/Google/Chrome',
        // devtools: true, //开发者模式打开
    });
    const page = await browser.newPage();

    await page.setViewport({
        width: 1200,
        height: 1200,
        deviceScaleFactor: 1,
    });
    
    
    
    await page.goto('http://www.baidu.com', {
        waitUntil: "domcontentloaded",
        timeout: timeout,
    });

    await page.waitForTimeout(timeout);

    // element = await page.locator('xpath///*[@id="lg"]')
    
    const [element] = await page.$x('//*[@id="lg"]');
    
    
    if (element) {
    // 截图元素
    await page.evaluate(el => el.style.border = '2px solid red', element);
    await element.screenshot({ path: 'element_screenshot.png' });
    console.log('Screenshot saved as element_screenshot.png');
  } else {
    console.log('No element found for the given XPath.');
  }
    
    await page.screenshot({
        path: "qework/screenshot.jpg",
        fullPage: true,
    });
    
    // await browser.close();
})();
