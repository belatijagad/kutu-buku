const puppeteer = require('puppeteer')

async function startBrowser() {
    let browser;
    try {
        console.log("Opening the server...")
        browser = await puppeteer.launch({
            headless: false,
            args: ['--disable-setuid-sandbox'],
            'ignoreHTTPSErrors': true,
        })
    } catch (err) {
        console.log("Could not create browser instance: ", err)
    }
    return browser;
}

module.exports = {
    startBrowser
}