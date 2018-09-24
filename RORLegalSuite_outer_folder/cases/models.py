from django.db import models

class Suffix(models.Model):
    """Table 1. Name Suffixes."""
    suffix_text = models.CharField(max_length=5, primary_key=True)

class Seafarer(models.Model):
    """Table 2. Name of Seafarers"""

class LocalAgent(models.Model):
    """Table 3. Local Agent is the manning agency of the Principal or shipowner."""

class Principal(models.Model):
    """Table 4. Principal is also the shipowner."""

class Correspondent(models.Model):
    """Table 5. Correspondents are local port advisers to and assistants of Clubs and Members (or shipowners)."""

class CaseHandler(models.Model):
    """Table 6. A Case Handler is a/the point person of the Correspondent"""

class Vessel(models.Model):
    """Table 7. Vessel is the name of the ship."""

class TypeOfClaim(models.Model):
    """Table 8. Types of Claim."""

class CouselOfSeafarer(models.Model):
    """Table 9. Lawyer for the Seafarer."""

class Club(models.Model):
    """Table 10. P&I Club or Protection and Indemnity Insurance Club is an association of shipowners for mutual protection."""

class Case(models.Model):
    """Table 11. Master List of Cases."""
















# Create your models here.
