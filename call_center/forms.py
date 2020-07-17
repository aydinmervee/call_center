from django import forms


class DateFilterForm(forms.Form):
    start_date = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
                'placeholder': 'Start Date'
            }
        ))
    end_date = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker2',
                'placeholder': 'End Date'
            }
        ))
