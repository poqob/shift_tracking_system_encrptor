from actionsmodel import Actions

action = Actions(id=1, name="test")
action0 = Actions().parse(action.serialize())
print(action0.serialize())


from qrcodemodel import QrCode

code = QrCode(id=1, time="time", code="code", action=action)
code0 = QrCode().parse(code.serialize())
print(code0.serialize())
