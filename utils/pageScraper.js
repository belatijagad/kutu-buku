const fs = require('fs')
const Papa = require('papaparse')

const scraperObject = {
    url: 'https://www.wuxiaworld.com/novels',
    async scraper(browser) {
        let page = await browser.newPage()
        console.log(`Navigating to ${this.url}...`)
        await page.goto(this.url)

        await page.waitForTimeout(1000);

        const button = await page.waitForXPath("//span[contains(., 'Popular')]");
        await button.click()

        let urls = [];
        const viewportHeight = page.viewport().height;
        let scrollPosition = 0;
        let prevLength = -1;
        let counter = 0;

        while (true) {
            // Extract URLs
            await page.waitForTimeout(1000)
            const href = await page.$$eval('div > p > a', anchors => {
                return anchors.map(anchor => anchor.getAttribute('href'));
            });
            urls = [...new Set([...urls, ...href])];

            if (urls.length == prevLength) {
                counter++;
                if (counter > 3) break;
            } else {
                counter = 0;
            }

            scrollPosition += 2 * viewportHeight;
            await page.evaluate(scrollPosition => {
                window.scrollTo(0, scrollPosition)
            }, scrollPosition);

            prevLength = urls.length;
        }

        let pagePromise = (link) => new Promise(async (resolve, reject) => {
            let dataObj = {}
            let newPage = await browser.newPage()
            await newPage.goto(`https://wuxiaworld.com${link}`)
            await page.waitForTimeout(1000)
            dataObj['title'] = await newPage.$eval('div > h1', h1 => h1.textContent);
            dataObj['author'] = await newPage.$eval('.space-x-4 > div + div', div => div.textContent);
            dataObj['chapters'] = await newPage.$eval('.font-set-m12 + div', div => parseInt(div.textContent.replace(' Chapters', '')));
            dataObj['img_src'] = await newPage.$eval('div > div > img', img => img.src);
            dataObj['genres'] = await newPage.$$eval('a > div > div', divs => {
                return divs.map(div => div.textContent).filter(text => text != '');
            })
            dataObj['synopsis'] = await newPage.$$eval('div.font-set-r13 > span > span', paragraphs => {
                return paragraphs.map(p => p.textContent).filter(text => text.length > 20).join('|');
            });

            dataObj['reviewers'] = await newPage.$eval('span + div > span', span => parseInt(span.textContent.replace(' Reviews', '')));
            dataObj['score'] = await newPage.$eval('span > svg + span', span => parseInt(span.textContent.replace('%', '')));
            resolve(dataObj)
            await newPage.close()
        })
        let novels = []
        for (link in urls) {
            let data = await pagePromise(urls[link])
            novels.push(data);
        }
        fs.writeFileSync('./utils/output/novels.json', JSON.stringify(novels));
        browser.close()
    }
}

module.exports = scraperObject