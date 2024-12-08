

class SortVO:
    def __init__(self, sort_title_list, sort_item_list):
        self.sort_title_list = sort_title_list
        self.sort_item_list = sort_item_list

    def to_dict(self):
        return {
            "title1": self.status,
            "data": self.data,
        }
