from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem

class CartView(APIView):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return Response({"items": [{"id": item.id, "product": item.product.name, "quantity": item.quantity} 
            for item in cart.items.all()]})
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        if not created: cart_item.quantity += quantity
        cart_item.save()
        return Response({'message': 'Item added to cart'}, status=status.HTTP_201_CREATED)
    def delete(self, request, item_id):
        try:
            CartItem.objects.get(id=item_id, cart__user=request.user).delete()
            return Response({'message': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)