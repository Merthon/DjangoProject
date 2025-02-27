# analysis/views.py
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from analysis.models import FateAnalysisRecord
from analysis.llm_integration import get_fate_analysis

# 获取日志记录器
logger = logging.getLogger('analysis')

@csrf_exempt
def analyze_fate(request):
    """
    API 接口：接收用户提交的出生数据，调用 LLM 模块生成分析报告，并保存记录。
    只允许 POST 请求。
    """
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': '只支持 POST 请求'}, status=405)

    try:
        # 解析前端传来的 JSON 数据
        data = json.loads(request.body)
        openid = data.get('openid')
        birth_datetime = data.get('birth_datetime')
        birth_place = data.get('birth_place')

        if not (openid and birth_datetime and birth_place):
            return JsonResponse({'status': 'error', 'message': '参数不全'}, status=400)

        # 调用 LLM 模块生成分析报告
        analysis = get_fate_analysis(birth_datetime, birth_place)

        # 保存命理分析记录到数据库
        record = FateAnalysisRecord.objects.create(
            openid=openid,
            birth_datetime=birth_datetime,
            birth_place=birth_place,
            analysis_result=analysis
        )
        logger.info(f"新命理记录创建：Record ID {record.id} for openid {openid}")

        # 返回分析报告给前端
        return JsonResponse({'status': 'success', 'analysis': analysis})
    except Exception as e:
        logger.exception("处理分析请求时发生异常")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
