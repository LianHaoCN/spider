# _*_ coding:utf-8 _*_  
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider(models.Model):
    name = models.CharField(default='spider_', max_length=100, verbose_name='爬虫名称')
    deep = models.SmallIntegerField(default=1, verbose_name='爬虫深度')
    parser_threads = models.SmallIntegerField(default=1, verbose_name='解析线程数量')
    fetch_threads = models.SmallIntegerField(default=1, verbose_name='获取线程数量')
    save_threads = models.SmallIntegerField(default=1, verbose_name='保存线程数量')
    max_parser_queue = models.SmallIntegerField(default=1, verbose_name='解析队列最大数量')
    max_fetch_queue = models.SmallIntegerField(default=1, verbose_name='获取队列最大数量')
    max_save_queue = models.SmallIntegerField(default=1, verbose_name='保存队列最大数量')
    class Meta:
        db_table = 'spider_project'
        permissions = (
            ("can_read_spider", "读取资产权限"),
            ("can_change_spider", "更改资产权限"),
            ("can_add_spider", "添加资产权限"),
            ("can_delete_spider", "删除资产权限"),
        ) 
        verbose_name = '爬虫表'  
        verbose_name_plural = '爬虫表'  