1# -*- coding: utf-8 -*-

import logging
import sys
import os
from datetime import date

from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler
from icrawler.examples import FlickrImageCrawler
from icrawler.examples import GreedyImageCrawler
# load keywords from list



def test_google(keyword,folder,count):
    folder = 'google/'+folder
    google_crawler = GoogleImageCrawler(folder, log_level=logging.INFO)
    google_crawler.crawl(keyword, 0, count, date(2000, 1, 1),
                         date(2017, 1, 5), 1, 1, 4)


def test_bing(keyword,folder,count):
    bing_crawler = BingImageCrawler(folder)
    bing_crawler.crawl(keyword, 0, count, 1, 1, 4)


def test_baidu(keyword,folder):
    baidu_crawler = BaiduImageCrawler(folder)
    baidu_crawler.crawl(keyword, 0, count, 1, 1, 4)


def test_flickr(keyword,folder,count):
    folder = 'flicker/'+folder
    flickr_crawler = FlickrImageCrawler('983677f73df07199d3bc575c08a77c6b',
                                        folder)
    flickr_crawler.crawl(max_num=10, downloader_thr_num=4, tags=keyword,
                         tag_mode='all', group_id='68012010@N00')


def test_greedy(keyword,folder):
    greedy_crawler = GreedyImageCrawler(folder)
    greedy_crawler.crawl('bbc.com/sport', 1, 4, 1, min_size=(200, 200))


def main():
    count=20;
    lists = ['baby','toddler','young','middle age','old']
    f = open('Celebrity_usa.txt','r')
    for line in open('Celebrity_usa.txt'):
        name = f.readline()
        print name
        folder = 'images/' + name
        if not os.path.exists(folder):
            os.makedirs(folder)
        for age in lists:
            keyword = name + ' ' + age
            
            if len(sys.argv) == 1:
                dst = 'all'
            else:
                dst = sys.argv[1:]
            if 'all' in dst:
                dst = ['google', 'bing']
            if 'google' in dst:
                test_google(keyword,folder,count)
            if 'bing' in dst:
                test_bing(keyword,folder,count)
            if 'baidu' in dst:
                test_baidu(keyword,folder,count)
            if 'flickr' in dst:
                test_flickr(keyword,folder,count)
            if 'greedy' in dst:
                test_greedy(keyword,folder,count)


if __name__ == '__main__':
    main()
