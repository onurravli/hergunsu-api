from fastapi import FastAPI
from random import randint
import uvicorn

_id = 0
app = FastAPI()


class Water:
    def __init__(self, brand: str, price: float, desc: str, img: str):
        self.brand = brand
        self.price = price
        self.desc = desc
        self.img = img


data = [
    Water(
        "Gumus",
        2,
        "2 liraya su aldığım için kendimi 2019da gibi hissettim",
        "https://pbs.twimg.com/media/F3lCZEbbAAAtwjb?format=jpg&name=large",
    ),
    Water(
        "Nestle Pure Life",
        3.5,
        "Bugünkü suyumuz Çandarlı Terminalinden tam tamına 3.5 TL bence f/p 👍🏻",
        "https://pbs.twimg.com/media/F3olHoTWsAAmJvr?format=jpg&name=large",
    ),
    Water(
        "Pursu",
        5,
        "Günaydın, bugünkü suyumuzun pek bi numarası yok, 5 TL ama soğuk soğuk güzeldi",
        "https://pbs.twimg.com/media/F3t3oDpW0AAgQI_?format=jpg&name=large",
    ),
    Water(
        "Ev Suyu",
        0,
        "Günaydın, bugünkü suyum evden ama doğal kaynak suyu. Bedava ve lezzetli. 👍🏻",
        "https://pbs.twimg.com/media/F3zC85mWAAAMYFv?format=jpg&name=large",
    ),
    Water(
        "Damla",
        7,
        "GÜÜÜNAAAAYYDIN (seda sayan sesiyle), iyi haftasonları arkadaşlar. Bugünkü suyumuz çay bahçesinden damla. Damlanın tadını hiç sevmesemde yıllar içinde biraz düzeldi gibi geliyor bana. 7 TL, çay bahçesi için okey ama damla olduğu için mmmeehhh",
        "https://pbs.twimg.com/media/F34Ov5bWAAAEQB0?format=jpg&name=large",
    ),
    Water(
        "Kaltun",
        5,
        "GÜNAYDIINN, tam bugün yeni suyum yok derken bunu hatırladım. Yürürken yanından geçtiğim tekelden Kaltun 5TL. Adı çok cezbedici gelmese de tadı okey bence. Tam da ortlama fiyatta.",
        "https://pbs.twimg.com/media/F39yn6AW4AEsh8n?format=jpg&name=large",
    ),
    Water(
        "Aritma Suyu",
        0,
        "Bugünkü suyumu @kodluyoruz ekibi eşliğinde paylaşacağım hahah (süpersiniz) arıtma suyu, filtrelerini sık sık değiştirdiğiniz sürece en büyük nimet bence, yıllardır damacana söylemiyoruz çünkü atık suyu çok, ama damacanadan ucuza geliyordur tahminimce f/p",
        "https://pbs.twimg.com/media/F4C5TMTWAAAkmMu?format=jpg&name=large",
    ),
]


@app.get("/")
async def root():
    return data


@app.get("/random")
async def random():
    _len = len(data)
    rnd = randint(0, _len - 1)
    return data[rnd]
