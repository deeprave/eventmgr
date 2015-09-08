"""
    Some enumeration types used in django models
"""

from django_enumfield import enum


# Type descriptor for addresses

class AddressType(enum.Enum):
    ANY = 0
    RESIDENCE = 1
    BUSINESS = 2
    MAIN = 3
    BRANCH = 4
    MAIL = 5
    BILLING = 6
    LEGAL = 7
    CAMPUS = 8
    DORMITORY = 9
    CONTACT = 10
    ICE_CONTACT = 11
    OTHER = 12

    labels = {
        ANY: 'Unspecified',
        RESIDENCE: 'Residential',
        BUSINESS: 'Business',
        MAIN: 'Main Office',
        BRANCH: 'Branch Office',
        MAIL: 'Mailing',
        BILLING: 'Billing',
        LEGAL: 'Registered Legal',
        CAMPUS: 'Campus',
        DORMITORY: 'Dormitory',
        CONTACT: 'Contact',
        ICE_CONTACT: 'Emergency Contact',
        OTHER: 'Other',
    }


class PhoneType(enum.Enum):
    ANY = 0
    HOME = 1
    WORK = 2
    MOBILE = 3
    MAIN = 4
    FAX = 5

    labels = {
        ANY: 'Other',
        HOME: 'Home',
        WORK: 'Work',
        MOBILE: 'Mobile',
        MAIN: 'Main',
        FAX: 'Fax',
    }