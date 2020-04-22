from django.db import models

# Create your user model
class user(models.Model):

    generatedId = 4

    # Types of roles
    Developer = 'Dev' #, _('Developer')
    Designer = 'UI/UX'   #, _('Designer')
    Consultant = 'Consultant'   #, _('Consultant')
    Manager = 'Manager'     #, _('Manager')

    roleChoices = [
        (Developer, 'Developer'), 
        (Designer, 'Designer'), 
        (Consultant, 'Consultant'), 
        (Manager, 'Manager')
    ]

    idUser = models.IntegerField(primary_key=True, db_index=True, default=generatedId, editable=False)
    userName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, blank=True) # Could not set as unique=True
    name = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    
    role = models.CharField(
        max_length=10, 
        blank=True,
        choices=roleChoices,
        default = Manager
    )
    
    descriptionShort = models.CharField(max_length=250, blank=True)
    descriptionLong = models.TextField(blank=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    imageProfile = models.ImageField(upload_to='images/', blank=True)
    isAdmin = models.BooleanField()
    
# Add the Blog App to the settings


# Create Migration


# Migrate


# Add to the Admin

