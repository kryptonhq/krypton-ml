from krypton_ml.core.models.registry import KryptonCustomModel


class CustomModelExample(KryptonCustomModel):
    def __init__(self):
        self.model = lambda x, y: x + y

    def predict(self, input):
        return self.model(input["x"], input["y"])
