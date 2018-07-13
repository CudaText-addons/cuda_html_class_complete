from .cssclass_work import cssclass_on_complete

class Command:
    def on_complete(self, ed_self):
        res = cssclass_on_complete(ed_self)
        return res
        