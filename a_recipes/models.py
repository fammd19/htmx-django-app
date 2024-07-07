from django.db import models

class Recipe(models.Model):
    title=models.CharField(max_length=500)
    image=models.URLField(max_length=500)
    summary=models.TextField()
    prep_time=models.CharField(max_length=50)
    cook_time=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']

class Ingredient(models.Model):
    unit_of_measure=models.CharField(max_length=50)
    quantity=models.DecimalField(decimal_places=2,max_digits=6)
    ingredient=models.CharField(max_length=5)
    notes=models.CharField(max_length=50,default=None, blank=True, null=True)
    recipe=models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)

