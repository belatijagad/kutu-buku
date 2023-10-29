from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label='Cari')
    sort_by = forms.ChoiceField(
        choices=[
            ('', 'Pilih pengurutan'),
            ('nama', 'Nama'),
            ('-tanggal', 'Tanggal terbaru'),
            ('tanggal', 'Tanggal terlampau'),
        ],
        required=False,
        initial='',
        widget=forms.Select
    )