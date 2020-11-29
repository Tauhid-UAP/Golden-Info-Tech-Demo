from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.user_type = 1

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)





class MyUser(AbstractBaseUser):

    # required to include
    email = models.EmailField(verbose_name='email', unique=True, max_length=60)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # new

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    ADMIN = 1
    MEMBER = 2

    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin (superuser or admin)'),
        (MEMBER, 'Member'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    # user_type = models.PositiveSmallIntegerField(null=True, blank=True)

class Member(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    STATUS_CHOICES = (
        (ACTIVE, ACTIVE),
        (INACTIVE, INACTIVE),
    )

    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    telephone_home = models.CharField(max_length=200, null=True, blank=True)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    mother_name = models.CharField(max_length=200, null=True, blank=True)
    permanent_address = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)
    representative_name = models.CharField(max_length=200, null=True, blank=True)
    representative_father_name = models.CharField(max_length=200, null=True, blank=True)
    representative_mother_name = models.CharField(max_length=200, null=True, blank=True)
    representative_address = models.CharField(max_length=200, null=True, blank=True)
    member_subscription_receipt_no = models.CharField(max_length=200, null=True, blank=True)
    member_status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.myuser.username

class TransactionType(models.Model):
    DEPOSIT = 'Deposit'
    EXPENSE = 'Expense'
    TRANSACTION_TYPES = (
        (DEPOSIT, DEPOSIT),
        (EXPENSE, EXPENSE),
    )

    name = models.CharField(max_length=200, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.name

class Issue(models.Model):
    FEE = 'Fee'
    LOAN = 'Loan'
    ISSUE_TYPES = (
        (FEE, FEE),
        (LOAN, LOAN),
    )

    name = models.CharField(max_length=200, choices=ISSUE_TYPES)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    PAID = 'Paid'
    DUE = 'Due'
    STATUS_CHOICES = (
        (PAID, PAID),
        (DUE, DUE),
    )

    transaction_no = models.CharField(max_length=200, null=True, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    transactiontype = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    amount = models.FloatField()
    amount_in_word = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)

    def __str__(self):
        return self.transaction_no