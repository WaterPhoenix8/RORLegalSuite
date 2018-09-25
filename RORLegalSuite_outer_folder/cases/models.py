from django.db import models

class Suffix(models.Model):
    """Table 1. Name Suffixes."""
    suffix = models.CharField(max_length=5, primary_key=True)

class Seafarer(models.Model):
    """Table 2. Name of Seafarers"""
    seafarer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=4, blank=True)
    last_name = models.CharField(max_length=35)
    suffix = models.ForeignKey(Suffix, blank=True)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX, blank=True)

class LocalAgent(models.Model):
    """Table 3. Local Agent is the manning agency of the Principal or shipowner."""
    localagent_name = models.CharField(max_length=100, primary_key=True)

class Principal(models.Model):
    """Table 4. Principal is also the shipowner."""
    principal_name = models.CharField(max_length=100, primary_key=True)

class Correspondent(models.Model):
    """Table 5. Correspondents are local port advisers to and assistants of Clubs and Members (or shipowners)."""
    correspondent_name = models.CharField(max_length=100, primary_key=True)

class CaseHandler(models.Model):
    """Table 6. A Case Handler is a/the point person of the Correspondent"""
    casehandler_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=4, blank=True)
    last_name = models.CharField(max_length=35)
    suffix = models.ForeignKey(Suffix, blank=True)
    nickname = models.CharField(max_length=50, blank=True)
    correspondent = models.ForeignKey(Correspondent)

class Vessel(models.Model):
    """Table 7. Vessel is the name of the ship."""
    vessel_name = models.CharField(max_length=75, primary_key=True)

class TypeOfClaim(models.Model):
    """Table 8. Types of Claim."""
    claim_type = models.CharField('type of claim', max_length=50, primary_key=True)

class CounselOfSeafarer(models.Model):
    """Table 9. Lawyer for the Seafarer."""
    counselor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=4, blank=True)
    last_name = models.CharField(max_length=35)
    suffix = models.ForeignKey(Suffix, blank=True)
    nickname = models.CharField(max_length=50, blank=True)

class Club(models.Model):
    """Table 10. P&I Club or Protection and Indemnity Insurance Club
     is an association of shipowners for mutual protection."""
    club_name = models.CharField(max_length=100, primary_key=True)

class Case(models.Model):
    """Table 11. Master List of Cases."""
    case_id = models.AutoField(primary_key=True)

    ref_no = models.CharField('reference number', max_length=30)

    seafarer = models.ForeignKey(Seafarer)

    localagent = models.ForeignKey(LocalAgent)

    principal = models.ForeignKey(Principal)

    case_no = models.CharField('case number', max_length=50)

    #max_length of case_title == total max_length of (seafarer's name, len('  vs  '), and local agent)
    case_title = models.CharField(max_length=200, default='' + '  vs  ' + '' + ', et al.')

    correspondent = models.ForeignKey(Correspondent)

    casehandler = models.ForeignKey(CaseHandler)

    vessel = models.ForeignKey(Vessel)

    typeofclaim = models.ForeignKey(TypeOfClaim)

    contract = models.BooleanField('POEA SEC with CBA')

    diagnosis = models.TextField()

    #treatment_day1 = models.DateTimeField('1st day of treatment', auto_now_add=True, blank=True, null=True)
    treatment_day1 = models.DateTimeField('1st day of treatment', blank=True, null=True)

    counselofseafarer = models.ForeignKey(CounselOfSeafarer, verbose_name="seafarer's counsel")

    club = models.ForeignKey(Club)

    legal_opinion = models.BooleanField()

    remarks = models.TextField(blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)

    datetime_updated = models.DateTimeField(auto_now=True)

# Create your models here.
