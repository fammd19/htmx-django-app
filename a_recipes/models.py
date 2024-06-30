from django.db import models

class Recipe(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title=models.CharField(max_length=500)
    image=models.URLField(max_length=500)
    summary=models.TextField()
    prep_time=models.CharField(max_length=50)
    cook_time=models.CharField(max_length=50)

    def __str__(self):
        return f"ID {self.id}: {self.title}"

# class Ingredients(models.Model):
#     id = models.IntegerField(unique=True, primary_key=True)
#     unit_of_measure=models.CharField(max_length=50)
#     quantity=models.DecimalField(decimal_places=2)
#     ingredient=models.IntegerField(max_length=5)
#     notes=models.IntegerField(max_length=5)
#     recipe_id=models.ForeignKey(Recipe, on_delete=models.CASCADE)

