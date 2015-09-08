from django.db import models
from .enums import AddressType, PhoneType
from django_enumfield import enum

""" Basic address book tables """


class Country(models.Model):
    abbrev = models.CharField(max_length=5)
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.abbrev, self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'countries'


class State(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=64)
    abbrev = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Locality(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=64)
    postcode = models.CharField(max_length=8)

    def __str__(self):
        return "%s (%s)" % (self.name, self.state.name)

    class Meta:
        ordering = ('name', 'state')
        verbose_name_plural = 'localities'


class Address(models.Model):
    type = enum.EnumField(AddressType)
    locality = models.ForeignKey(Locality)
    title = models.CharField(blank=True, null=True, max_length=254)
    contact_name = models.CharField(blank=True, null=True, max_length=1022)
    address_1 = models.CharField(blank=False, max_length=1022)
    address_2 = models.CharField(blank=True, null=True, max_length=1022)

    def __str__(self):
        result = "%s %s %s %s %s %s" % (self.title, self.addres_1, self.address_2, self.locality.name,
                                        self.locality.state.name, self.locality.postcode)
        return result.replace('  ', ' ').strip()

    class Meta:
        ordering = ('title', 'address_1', 'address_2')
        verbose_name_plural = 'addresses'


class Email(models.Model):
    address = models.EmailField(blank=False)

    @property
    def is_valid(self):
        return self.address and '@' in self.address

    @property
    def username(self):
        return self.address.split('@', 1)[0] if self.is_valid else ''

    @property
    def domain(self):
        return self.address.split('@', 1)[1] if self.is_valid else ''

    def __str__(self):
        return self.address


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=32)
    phone_type = enum.EnumField(PhoneType)

    def __str__(self):
        return self.phone_number


TITLE_CHOICES = (
    # common
    (None, 'None'),
    ('Mr.', 'MR'), ('Miss', 'MISS'), ('Ms.', 'MS'), ('Mrs.', 'MRS'),
    # less common
    ('Dr.', 'DR'), ('Prof.', 'PROF'), ('Rev.', 'REV'),
    # military
    ('Lt.', 'LT'), ('Cpt.', 'CPT'), ('Maj.', 'MAJ'), ('Gen.', 'GEN'),
    # rare
    ('Esq', 'ESQ'), ('Sr.', 'SR'), ('Jr.', 'JR'), ('Hon.', 'HON'), ('Rt. Hon.', 'RT HON')
)


class Contact(models.Model):
    name = models.CharField(blank=False, max_length=254)
    nick = models.CharField(blank=True, null=True, max_length=64)
    company = models.BooleanField(default=False)
    title = models.CharField(blank=True, null=True, max_length=16, choices=TITLE_CHOICES)
    emails = models.ManyToManyField(Email)
    addresses = models.ManyToManyField(Address)
    phones = models.ManyToManyField(PhoneNumber)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
