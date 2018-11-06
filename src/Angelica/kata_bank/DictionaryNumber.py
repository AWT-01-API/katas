class DictionaryNumber:

    def __init__(self,ch_hr, ch_v, cond_pos):
        self.ch_hr = ch_hr
        self.ch_v = ch_v
        self.cond_pos = cond_pos

    def get_number(self):
        if self.ch_hr == 2 and self.ch_v == 4:
            return 0
        elif self.ch_v == 2:
            return 1
        elif self.ch_hr == 3 and self.ch_v == 2 and self.cond_pos == 1:
            return 2
        elif self.ch_hr == 3 and self.ch_v == 2:
            return 3
        elif self.ch_hr == 1 and self.ch_v == 3:
            return 4
        elif self.ch_hr == 3 and self.ch_v == 2 and self.cond_pos == 3:
            return 5
        elif self.ch_hr == 3 and self.ch_v == 3 and self.cond_pos == 3:
            return 6
        elif self.ch_hr == 1 and self.ch_v == 2:
            return 7
        elif self.ch_hr == 4 and self.ch_v == 4:
            return 8
        elif self.ch_hr == 3 and self.ch_v == 3 and self.cond_pos == 4:
            return 9
