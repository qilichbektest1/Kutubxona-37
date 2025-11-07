import datetime
from django.db import models
from django.core.validators import MaxValueValidator

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=255)
    kurs = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=1)
    kitob_soni = models.PositiveIntegerField(default=0)

    objects: models.Manager['Talaba']  # type hint (IDE uchun)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Talabalar'


class Muallif(models.Model):
    objects: models.Manager['Muallif']  # type hint (IDE uchun)

    class JINS_CHOICES(models.TextChoices):
        ERKAK = "Erkak","Erkak"
        AYOL = "Ayol", "Ayol"

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=20, choices=JINS_CHOICES.choices)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(default=1)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Mualliflar'


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Kitoblar'


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.TimeField(default=datetime.time(hour=8))

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Kutubxonachilar'


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True,blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True,blank=True  )
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True,blank=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytargan_sana = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        t = ""
        if self.talaba:
            t += self.talaba.ism
        if self.kitob:
            if self.talaba:
                t += " - "
            t += self.kitob.nom
        if self.kutubxonachi:
            if self.talaba or self.kitob:
                t += " - "
            t += self.kutubxonachi.ism

        if not t:
            return t if t else f"RECORD (ID: {self.pk}){str(self.olingan_sana)[:16]}"
        return t + "" + str(self.olingan_sana)[:16]

    class Meta:
        verbose_name_plural = 'Recordlar'
