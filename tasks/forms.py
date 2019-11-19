from django import forms


class TaskForm2(forms.Form):
    task_name = forms.CharField()
    task_description = forms.CharField(widget=forms.Textarea)
    task_is_done = forms.BooleanField()
    task_due_date = forms.DateTimeField()
    pub_date = forms.DateTimeField()
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")

    def clean(self):
        all_clean_data = super().clean()
        print('all_clean_data')
