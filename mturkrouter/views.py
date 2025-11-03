import json
import re
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import MTurkLog

_ID_RE = re.compile(r'^[A-Za-z0-9_-]{5,32}$')

@csrf_exempt
def mturk_log(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Bad JSON")

    mturk_id = (payload.get("mturk_id") or "").strip()
    if not _ID_RE.match(mturk_id):
        return HttpResponseBadRequest("Invalid mturk_id")

    country      = (payload.get("country") or "").strip()
    region       = (payload.get("region") or "").strip()
    region_key   = (payload.get("region_key") or "").strip()
    assigned_url = (payload.get("assigned_url") or "").strip()
    try:
        assigned_idx = int(payload.get("assigned_idx") or 0)
    except Exception:
        assigned_idx = 0

    ua = (request.META.get("HTTP_USER_AGENT", "") or "")[:1000]
    ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
    ip = (ip.split(",")[0].strip() if isinstance(ip, str) else None)

    MTurkLog.objects.create(
        mturk_id=mturk_id,
        country=country,
        region=region,
        region_key=region_key,
        assigned_url=assigned_url,
        assigned_idx=assigned_idx,
        user_agent=ua,
        ip_address=ip,
    )
    return JsonResponse({"ok": True})
