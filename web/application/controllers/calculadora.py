import web
import app
render = web.template.render('application/views/')

class Calculadora:
    def GET(self):
        data = []
        data.append(1)
        data.append(1)
        data.append(1)
        data.append(1)
        data.append(1)
        data.append(1)
        return  render.calculadora(data)

    def GET(self):
        form = web.input()
        number1 = int(form["number1"])
        number2 = int(form["number2"])
        add = number1 + number2
        res = number1 - number2
        mul = number1 * number2
        div = number1 / number2

        data = []
        data.append(number1)
        data.append(number2)
        data.append(add)
        data.append(res)
        data.append(mul)
        data.append(div)

        return  render.calculadora(data)


if __name__ == "__main__":
    web.config.debug= False
    app.run()