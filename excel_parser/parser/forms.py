from django import forms


class CustomDateInput(forms.DateInput):
    input_type = "date"


class InputForm(forms.Form):
    file = forms.FileField(allow_empty_file=False, required=False, label="Выберите файл",
                           widget=forms.FileInput(attrs={"class": "file-input", "accept": ".xlsx,.xls"}))
    date_1 = forms.DateField(label="Выберите первую дату", widget=CustomDateInput(attrs={"class": "date-input"}))
    date_2 = forms.DateField(label="Выберите вторую дату", widget=CustomDateInput(attrs={"class": "date-input"}))

    def clean_file(self):
        file_object = self.cleaned_data.get("file")
        if file_object:
            if file_object.name.endswith(".xlsx"):
                return file_object
            else:
                raise forms.ValidationError("Допустимы только файлы формата xslx")

    def check_date(self):
        date_1 = self.cleaned_data.get("date_1")
        date_2 = self.cleaned_data.get("date_2")
        if date_1 == date_2 or ((date_1.year != date_2.year) or (date_1.month != date_2.month)):
            return False
        return True

    def clean(self):
        cleaned_data = super().clean()
        if not self.check_date():
            self.add_error("date_1", "Даты должны быть в пределах одного года и месяца и различаться хотя бы на 1 день")
        return cleaned_data
