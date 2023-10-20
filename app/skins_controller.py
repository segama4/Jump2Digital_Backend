from .models import Skin


def get_available_skins():
    return Skin.objects().to_json()


def buy_skin(data):
    skin_data = {
        "name": data["name"],
        "type": data["type"],
        "price": data["price"],
        "color": data["color"]
    }
    skin = Skin(**skin_data).save()
    return skin.to_json()


def get_my_skins():
    return Skin.objects().to_json()


def change_skin_color(data):
    skin = Skin.objects.get(id=data["id"])
    skin.color = data["color"]
    skin.save()
    return skin.to_json()


def delete_skin(id):
    skin = Skin.objects.get(id=id)
    if not skin:
        return {"message": "Skin not found"}
    skin.delete()
    return {"message": "Skin deleted"}


def get_skin(id):
    skin = Skin.objects.get(id=id)
    return skin.to_json()
