# analysis/models.py
from django.db import models

class FateAnalysisRecord(models.Model):
    # 微信用户唯一标识
    openid = models.CharField(max_length=64, help_text="微信用户唯一标识")
    # 出生日期和时间，存储为 datetime 类型（确保前端传来的数据格式正确）
    birth_datetime = models.DateTimeField(help_text="出生日期和时间，格式应为 YYYY-MM-DD HH:MM:SS")
    # 出生地点信息
    birth_place = models.CharField(max_length=100, help_text="出生地点")
    # 存储生成的命理分析报告
    analysis_result = models.TextField(help_text="命理分析详细报告")
    # 自动记录创建时间
    created_at = models.DateTimeField(auto_now_add=True, help_text="记录创建时间")

    def __str__(self):
        return f"Record {self.id} - {self.openid}"
