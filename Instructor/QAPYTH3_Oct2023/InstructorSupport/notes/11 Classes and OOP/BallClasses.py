class _Ball:

    def __init__(self):
        print(__class__.__name__)
        
class BasketBall(_Ball):

    def __init__(self):
        super().__init__()
        print(__class__.__name__)