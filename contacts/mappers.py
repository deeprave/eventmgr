from nap.datamapper import ModelDataMapper
from .models import Locality, State, Country


class CountryMapper(ModelDataMapper):
    class Meta:
        model = Country
        fields = '__all__'


class StateMapper(ModelDataMapper):
    class Meta:
        model = State
        fields = '__all__'
        exclude = ['country']


class LocalityMapper(ModelDataMapper):
    class Meta:
        model = Locality
        fields = '__all__'
        exclude = ['state']

