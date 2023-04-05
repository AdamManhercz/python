"""Exception customizations"""


class AvailabilityError(Exception):
    """Raised if a book is not available in the library"""

    pass


class BalanceError(Exception):
    """Raised if the student has negative balance"""

    pass


class LoanVolumeError(Exception):
    """Raised if the student has negative balance"""

    pass
