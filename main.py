from views import CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin
from search import search_object

class Cars(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    def _get_or_objects_and_id(self):
        return super()._get_or_objects_and_id()
    
    def __init__(self) -> None:
        super().__init__()
    
    def create(self, **kwargs):
        return super().create(**kwargs)

    def list(self):
        return super().list()
    
    @search_object
    def detail(self, id, **kwargs):
        return super().detail(id, **kwargs)
    
    @search_object
    def patch(self, id, **kwargs):
        return super().patch(id, **kwargs)
    
    @search_object
    def delete(self, id, **kwargs):
        return super().delete(id, **kwargs)

    def save (self):
        import json
        with open ('data_2.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'
    


cars = Cars() 
print(cars.create(brand='BMW', model='X6',year=2017, color='white', type=6, probeg=200,  price=25500))
print(cars.create(brand='Toyota', model='Camry',year=2018, color='black', type=3, probeg=152,  price=17000))
print()



