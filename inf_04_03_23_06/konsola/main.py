class Film:
    def __init__(self):
        self._title = None
        self._num_rentals = 0
    
    def set_title(self, title: str) -> None:
        self._title = title
    
    def get_title(self) -> str:
        return self._title
    
    def get_num_rentals(self) -> int:
        return self._num_rentals
    
    def increment_rentals(self) -> None:
        self._num_rentals += 1
