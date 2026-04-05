from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ["title", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Добавьте описание"}
        )

        self.fields["image"].widget.attrs.update({"class": "form-control"})

        self.fields["category"].widget.attrs.update({"class": "form-select"})

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "step": "0.01", "min": "0"}
        )

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if title:
            title_lower = title.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in title_lower:
                    raise forms.ValidationError(f'Слово "{word}" запрещено в названии')

        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if description:
            desc_lower = description.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in desc_lower:
                    raise forms.ValidationError(f'Слово "{word}" запрещено в описании')

        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is None:
            raise forms.ValidationError("Цена обязательна для заполнения")

        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")

        if price == 0:
            raise forms.ValidationError("Цена не может быть равна нулю")

        return price
