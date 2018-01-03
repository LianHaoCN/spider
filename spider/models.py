# _*_ coding:utf-8 _*_  
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider(models.Model):
    name = models.CharField(default='spider_', max_length=100, verbose_name='��������')
    deep = models.SmallIntegerField(default=1, verbose_name='�������')
    parser_threads = models.SmallIntegerField(default=1, verbose_name='�����߳�����')
    fetch_threads = models.SmallIntegerField(default=1, verbose_name='��ȡ�߳�����')
    save_threads = models.SmallIntegerField(default=1, verbose_name='�����߳�����')
    max_parser_queue = models.SmallIntegerField(default=1, verbose_name='���������������')
    max_fetch_queue = models.SmallIntegerField(default=1, verbose_name='��ȡ�����������')
    max_save_queue = models.SmallIntegerField(default=1, verbose_name='��������������')
    class Meta:
        db_table = 'spider_project'
        permissions = (
            ("can_read_spider", "��ȡ�ʲ�Ȩ��"),
            ("can_change_spider", "�����ʲ�Ȩ��"),
            ("can_add_spider", "����ʲ�Ȩ��"),
            ("can_delete_spider", "ɾ���ʲ�Ȩ��"),
        ) 
        verbose_name = '�����'  
        verbose_name_plural = '�����'  