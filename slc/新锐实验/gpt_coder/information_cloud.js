const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const path = require('path');
const fs = require('fs');

puppeteer.use(StealthPlugin());

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    // code 
    // Launch the browser and open a new blank page
    const browser = await puppeteer.launch({
      headless: false, // 非无头模式
    executablePath: '/Users/zhaoxuefeng/.cache/puppeteer/chrome/mac_arm-121.0.6167.85/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing',
    userDataDir: './engine',
    });
    const page = await browser.newPage('https://www.qbitai.com/category/资讯');
    await page.setViewport({
        width: 1200,
        height: 1200,
        deviceScaleFactor: 1,
    });
    // Navigate the page to a URL
    await page.goto('https://www.qbitai.com/category/资讯');
    console.log('open')
    const infos = await page.$$("xpath//html/body/div[1]/div[1]/div/div");

    console.log("xxx")      
    console.log(infos.length)
    let myList = [];
    for (let i = 0; i< infos.length; i++) {
        const html = await page.evaluate(element => element.innerHTML, infos[i]);
               
        console.log(html)
        console.log('xxxxxxxxxxxxxx')
        
        const titleMatch = html.match(/<h4><a href="([^"]*)" [^>]*>([^<]*)<\/a><\/h4>/);
        const title = titleMatch ? titleMatch[2] : '';
        const titleLink = titleMatch ? titleMatch[1] : '';

        // 使用正则表达式提取作者
        const authorMatch = html.match(/<span class="author"><a [^>]*>([^<]*)<\/a><\/span>/);
        const author = authorMatch ? authorMatch[1] : '';

        // 使用正则表达式提取发布时间
        const timeMatch = html.match(/<span class="time">([^<]*)<\/span>/);
        const time = timeMatch ? timeMatch[1] : '';

        // 使用正则表达式提取标签
        const tagsMatch = html.match(/<div class="tags_s">([\s\S]*?)<\/div>/);
        const tags = tagsMatch ? tagsMatch[1].match(/<a [^>]*>([^<]*)<\/a>/g).map(tag => tag.replace(/<a [^>]*>([^<]*)<\/a>/, '$1')) : [];

        console.log({
            title,
            titleLink,
            author,
            time,
            tags
        });
        myList.push({
            title,
            titleLink,
            author,
            time,
            tags
        })
        const newPage = await browser.newPage();
        await newPage.goto(titleLink);
        await page.waitForTimeout(100); // 等待页面加载完成
        await page.pdf({path:`${title}.pdf`,});

        await newPage.close();
        await page.bringToFront();

        
        
    }
    console.log(myList);
    
    
    
    
    
    const fs = require('fs');
    
    const jsonString = JSON.stringify(myList, null, 2);

    fs.writeFile('articles.json', jsonString, (err) => {
      if (err) {
        console.error('Error writing file', err);
      } else {
        console.log('Successfully wrote file');
      }
    });
    

    
    
    // const htmlContent = await page.$eval('xpath//html/body/div[1]/div[1]/div', element => element.innerHTML);
    // console.log(htmlContent)
    
    
    // await browser.close();
    
})();
