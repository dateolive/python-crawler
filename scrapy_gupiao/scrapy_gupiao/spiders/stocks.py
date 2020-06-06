# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stock_list.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = 'http://gu.qq.com/' + stock + '/gp'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockName = response.css('.title_bg')
        stockInfo = response.css('.col-2.fr')
        name = stockName.css('.col-1-1').extract()[0]
        code = stockName.css('.col-1-2').extract()[0]
        info = stockInfo.css('li').extract()
        for i in info[:13]:
            key = re.findall('>.*?<', i)[1][1:-1]
            key = key.replace('\u2003', '')
            key = key.replace('\xa0', '')
            try:
                val = re.findall('>.*?<', i)[3][1:-1]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update({'股票名称': re.findall('\>.*\<', name)[0][1:-1] + \
                                 re.findall('\>.*\<', code)[0][1:-1]})
        yield infoDict
