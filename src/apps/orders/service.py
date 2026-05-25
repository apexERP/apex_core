

from .models import Orders

class OrderService:
    
    
    @classmethod
    def get_all_orders(
        cls,
        status: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ):
        
        orders = Orders.objects.all()
        
        if status:
            orders = orders.filter(order_status=status)
        
        if limit:
            orders = orders[:limit]
        
        if offset:
            orders = orders[offset:]
        
        return orders
    
    
    
    
    @classmethod
    def create_order(cls, first_name: str, phone_number: str):

        order = Orders.objects.create(
            first_name=first_name,
            phone_number=phone_number,
            status=Orders.OrderStatus.NEW
        )
        return order



    @classmethod
    def change_order_status(cls, order_id: int, status: str):

        order = Orders.objects.get(id=order_id)
        order.order_status = status
        order.save()
        return order

