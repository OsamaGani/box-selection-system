
from decimal import Decimal
from itertools import permutations

from .models import ShippingBox


def _can_pack_products(products, box):
    """
    Try to place every product inside the box without overlap.
    Uses a simple 3D shelf-placement heuristic.
    """

    box_length = float(box.length)
    box_width = float(box.width)
    box_height = float(box.height)

    # Sort larger products first to improve placement.
    dimensions = sorted(
        [
            (
                float(product.length),
                float(product.width),
                float(product.height),
            )
            for product in products
        ],
        key=lambda item: item[0] * item[1] * item[2],
        reverse=True,
    )

    # Each shelf stores its starting position, height and used width.
    shelves = []
    current_layer_z = 0.0
    layer_height = 0.0
    layer_y = 0.0
    layer_used_width = 0.0

    for length, width, height in dimensions:
        placed = False

        for a, b, c in set(permutations((length, width, height))):
            # Try placing on an existing shelf.
            for shelf in shelves:
                if (
                    a <= box_length - shelf["used_length"]
                    and b <= shelf["width"]
                    and c <= shelf["height"]
                ):
                    shelf["used_length"] += a
                    placed = True
                    break

            if placed:
                break

            # Try creating a new shelf in the current layer.
            if (
                layer_y + b <= box_width
                and c <= box_height - current_layer_z
                and a <= box_length
            ):
                shelves.append({
                    "used_length": a,
                    "width": b,
                    "height": c,
                })
                layer_y += b
                layer_height = max(layer_height, c)
                placed = True
                break

            # Try starting a new vertical layer.
            if current_layer_z + layer_height + c <= box_height:
                current_layer_z += layer_height
                layer_height = c
                layer_y = b
                shelves = [{
                    "used_length": a,
                    "width": b,
                    "height": c,
                }]
                placed = True
                break

        if not placed:
            return False

    return True


def recommend_box(products):
    """
    Recommend the lowest-cost box that can accommodate all products
    under its maximum weight capacity and placement constraints.
    """

    products = list(products)

    if not products:
        raise ValueError("Order must contain at least one product.")

    total_weight = sum(
        (product.weight for product in products),
        Decimal("0"),
    )

    suitable_boxes = []

    for box in ShippingBox.objects.all():
        if total_weight > box.max_weight:
            continue

        if _can_pack_products(products, box):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    return min(suitable_boxes, key=lambda box: (box.cost, box.pk))
