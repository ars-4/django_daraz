from core.models import Shop, Person, Picture



# Get or Create Shop for seller
def get_or_create_shop(person):
        shops = Shop.objects.filter(owner=person)
        if len(shops) == 0:
            shop = Shop.objects.create(
                owner=person,
                shop_name="shop_name",
                address="shop_address"
            )
            shop.save()
        else:
            shop = shops[0]
        return shop

def add_image(field_name, request, shop):
    if request.FILES.get(field_name):
            shop_picture = Picture.objects.create(
                title=shop.shop_name,
                image=request.FILES.get(field_name)
            )
            shop_picture.save()
            shop.images.add(shop_picture)
            shop.save()

def update_shop(request, shop):
    if request.POST.get('shop_name') or request.POST.get('shop_address'):
        shop.shop_name = request.POST.get('shop_name')
        shop.address = request.POST.get('shop_address')
        shop.save()