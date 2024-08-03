const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());


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
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');

    
    
    await page.goto('https://chatgpt.com', {
        waitUntil: "domcontentloaded",
    });
    
    // await browser.close();
})();
