# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import md5sum
from scrapy.http import Request
from scrapy_splash import SplashRequest

class NewsmthimagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, headers={'Title':item['title']}) for x in item.get(self.images_urls_field, [])]

    def persist_gif(self, path, url, info):
        if path.endswith('.jpg'):
            path = path[:-4]
        path = path + '.gif'
        absolute_path = self.store._get_filesystem_path(path)
        self.store._mkdir(os.path.dirname(absolute_path), info)
        print "***** Gif Found: *****" + path + ", " + absolute_path
        urllib.urlretrieve(url, absolute_path)
        #with open(absolute_path, 'wb') as f:
        #    f.write(buf.getvalue())

    def image_downloaded(self, response, request, info):
        checksum = None
        for path, image, buf in self.get_images(response, request, info):
            if checksum is None:
                buf.seek(0)
                checksum = md5sum(buf)
            width, height = image.size
            path_list = list(os.path.split(path))
            path_list.insert(-1, request.headers['Title'])
            path = '/'.join(path_list)
            print path
            if response.headers['Content-Type'] == 'image/gif':
                self.persist_gif(path, request.url, info)
            else:
                self.store.persist_file(
                        path, buf, info,
                        meta={'width': width, 'height': height},
                        headers={'Content-Type': 'image/jpeg'})
        return checksum
