import puppeteer from 'puppeteer';

async function scrapeProduct(url){
    const browser = await puppeteer.launch({
        headless: headless,
        devtools: true,
        args: [
            '--disable-web-security',
            '--disable-features=IsolateOrigins',
            '--disable-site-isolation-trials'
        ]
    });
    const page = await browser.newPage();
    page.goto(url); 

    const [el] = await page.$x('//*[@id="home-content"]/div[1]/div[2]');
    console.log({el})

    browser.close();


}

scrapeProduct("https://www1.flightrising.com")