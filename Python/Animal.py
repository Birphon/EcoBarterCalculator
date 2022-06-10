class Animal:
    def animal_size(self, bison=10, medium=5, small=2, tiny=1):
        self.bison = bison
        self.medium = medium
        self.samll = small
        self.tiny = tiny

    def bison_scale(self):
        bison_tiny = 0
        bison_med = 0
        bison_small = 0

        bison_tiny = self.bison/self.tiny  # should reutrn 10
        bison_med = self.bison/self.medium  # should return 2
        bison_small = self.bison/self.small  # should return 5
