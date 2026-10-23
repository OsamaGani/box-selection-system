import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product
from .services import recommend_box


@csrf_exempt
@require_POST
def recommend_box_api(request):
    # Parse the JSON request body
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Request body must contain valid JSON."},
            status=400,
        )

    # Validate product_ids
    product_ids = data.get("product_ids")

    if not isinstance(product_ids, list) or not product_ids:
        return JsonResponse(
            {"error": "product_ids must be a non-empty list."},
            status=400,
        )

    if any(
        type(product_id) is not int or product_id <= 0
        for product_id in product_ids
    ):
        return JsonResponse(
            {"error": "Each product ID must be a positive integer."},
            status=400,
        )

    # Fetch products from the database
    unique_ids = set(product_ids)
    products = list(Product.objects.filter(id__in=unique_ids))

    if len(products) != len(unique_ids):
        return JsonResponse(
            {"error": "One or more products were not found."},
            status=404,
        )

    # Recommend a suitable shipping box
    try:
        box = recommend_box(products)
    except ValueError as error:
        return JsonResponse({"error": str(error)}, status=400)

    if box is None:
        return JsonResponse(
            {"message": "No suitable shipping box found."},
            status=404,
        )

    # Return the recommended box
    return JsonResponse({
        "box": box.name,
        "dimensions": {
            "length": str(box.length),
            "width": str(box.width),
            "height": str(box.height),
        },
        "max_weight": str(box.max_weight),
        "cost": str(box.cost),
    })