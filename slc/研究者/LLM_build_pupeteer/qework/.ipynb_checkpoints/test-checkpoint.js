const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const timeout = 4000;
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

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
    
    
    
    await page.goto('https://looka.com/explore', {
        waitUntil: "domcontentloaded",
        timeout: timeout,
    });
    await page.locator('xpath///*[@id="industry"]').fill('kkkk') // industry
    await page.locator('xpath///*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/button').click() // skip 
    await page.locator('xpath///*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/div/button').click() // skip 
    await page.locator('xpath///*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/button').click() // skip 
    await page.locator('xpath///*[@id="name"]').fill('xxxx') // company name
    await page.locator('xpath///*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/button').click() // skip 
    await page.locator('xpath///*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/button').click() // skip 
    
    
    
    
    
    
    // 写一个等待程序
    await page.waitForTimeout(20000);
    console.log('start');
    
    
    for (let i = 1; i <= 9; i++) {
      console.log(i);
      let eles = `//*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/div[${i}]`;
      const [element] = await page.$x(eles);
            
      if (element) {
        // 截图元素
        await page.evaluate(el => el.style.border = '4px solid red', element);
        await element.screenshot({ path: `element_screenshot_${i}.png` });
        console.log('Screenshot saved as element_screenshot_i.png');
      } else {
        console.log('No element found for the given XPath.');
      }

    }

    const elements = await page.$x('//*[@id="logojoy-root"]/div[2]/div[1]/div[2]/div[2]/div/div/div');
    console.log(elements.length);
    if (elements.length > 0) {
    const element = elements[0];
        await page.evaluate(el => el.style.border = '2px solid red', element);
        sleep(1000)
        // 截图
        await element.screenshot({ path: 'element_screenshot.png' });
        console.log('Screenshot saved as element_screenshot.png');
      } else {
        console.log('No elements found for the given XPath.');
      }
    
    
    
    await page.screenshot({
        path: "qework/screenshot.jpg",
        fullPage: true,
    });
    
    // await browser.close();
})();
