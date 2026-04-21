import json


# for i in range(0, 999):
#     print("('1734400668525609', 'test" + str(i) + "'),")

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    jsonString = """
    [{"longitude":118.826956,"latitude":31.956103},{"longitude":118.827048,"latitude":31.954114},{"longitude":118.827047,"latitude":31.953267},{"longitude":118.821367,"latitude":31.953316},{"longitude":118.820027,"latitude":31.958009},{"longitude":118.818171,"latitude":31.95753},{"longitude":118.819074,"latitude":31.953652},{"longitude":118.806136,"latitude":31.953608},{"longitude":118.80662,"latitude":31.941714},{"longitude":118.80688,"latitude":31.937029},{"longitude":118.807932,"latitude":31.927553},{"longitude":118.810175,"latitude":31.927751},{"longitude":118.821499,"latitude":31.927393},{"longitude":118.825131,"latitude":31.927266},{"longitude":118.828805,"latitude":31.927504},{"longitude":118.829888,"latitude":31.927972},{"longitude":118.831572,"latitude":31.928441},{"longitude":118.839442,"latitude":31.929376},{"longitude":118.851089,"latitude":31.932641},{"longitude":118.872189,"latitude":31.937869},{"longitude":118.870973,"latitude":31.944262},{"longitude":118.870458,"latitude":31.947203},{"longitude":118.870072,"latitude":31.950276},{"longitude":118.868999,"latitude":31.950727},{"longitude":118.868334,"latitude":31.954959},{"longitude":118.868157,"latitude":31.957057},{"longitude":118.867884,"latitude":31.958336},{"longitude":118.867868,"latitude":31.959827},{"longitude":118.86429,"latitude":31.95997},{"longitude":118.863528,"latitude":31.962095},{"longitude":118.863083,"latitude":31.964582},{"longitude":118.861521,"latitude":31.967397},{"longitude":118.86408,"latitude":31.968829},{"longitude":118.864407,"latitude":31.969532},{"longitude":118.863999,"latitude":31.970169},{"longitude":118.863347,"latitude":31.970107},{"longitude":118.85909,"latitude":31.967724},{"longitude":118.85685,"latitude":31.967489},{"longitude":118.857004,"latitude":31.966218},{"longitude":118.857208,"latitude":31.962069},{"longitude":118.851066,"latitude":31.961522},{"longitude":118.848854,"latitude":31.961377},{"longitude":118.846042,"latitude":31.961486},{"longitude":118.843214,"latitude":31.960589},{"longitude":118.842801,"latitude":31.962496},{"longitude":118.842398,"latitude":31.962401},{"longitude":118.842564,"latitude":31.960953},{"longitude":118.842569,"latitude":31.960464},{"longitude":118.84135,"latitude":31.960109},{"longitude":118.84117,"latitude":31.960319},{"longitude":118.840501,"latitude":31.962982},{"longitude":118.840242,"latitude":31.964063},{"longitude":118.840713,"latitude":31.964567},{"longitude":118.840573,"latitude":31.964943},{"longitude":118.840302,"latitude":31.964962},{"longitude":118.839625,"latitude":31.964616},{"longitude":118.838634,"latitude":31.963943},{"longitude":118.838804,"latitude":31.963636},{"longitude":118.839688,"latitude":31.9634},{"longitude":118.840679,"latitude":31.959815},{"longitude":118.839099,"latitude":31.959632},{"longitude":118.837968,"latitude":31.960086},{"longitude":118.836296,"latitude":31.960449},{"longitude":118.833982,"latitude":31.960235},{"longitude":118.83404,"latitude":31.961408},{"longitude":118.833988,"latitude":31.96375},{"longitude":118.830278,"latitude":31.964339},{"longitude":118.828542,"latitude":31.964654},{"longitude":118.829009,"latitude":31.960609},{"longitude":118.829139,"latitude":31.960252},{"longitude":118.827097,"latitude":31.960247}]
    """
    model = json.loads(jsonString)
    for item in model:
        print("fence.add(new Coordinate({},{}));".format(item["longitude"],item["latitude"]))
