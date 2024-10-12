from django import forms
from django.core.exceptions import ValidationError
from .models import RegisteredMember

class RegistrationForm(forms.Form):
    # Registration Type
    registration_type = forms.ChoiceField(
        choices=[('individual', 'Register Individually'), ('team', 'Register as Team')],
        widget=forms.RadioSelect,
        label="Registration Type"
    )
    
    # Fields for the first participant (required in all cases)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    panther_id = forms.IntegerField(required=True)
    degree = forms.ChoiceField(
        choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD')],
        required=True
    )
    major = forms.CharField(max_length=50, required=True)
    csc_1302 = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        required=True,
        label="Have you done CSC 1302?"
    )
    
    # Fields for the second participant (only required if registering as a team)
    team_member_2_first_name = forms.CharField(max_length=30, required=False)
    team_member_2_last_name = forms.CharField(max_length=30, required=False)
    team_member_2_email = forms.EmailField(required=False)
    team_member_2_panther_id = forms.IntegerField(required=False)
    team_member_2_degree = forms.ChoiceField(
        choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD')],
        required=False
    )
    team_member_2_major = forms.CharField(max_length=50, required=False)
    team_member_2_csc_1302 = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        required=False,
        label="Has teammate done CSC 1302?"
    )

    def clean_panther_id(self):
        panther_id = self.cleaned_data.get('panther_id')
        if RegisteredMember.objects.filter(panther_id=panther_id).exists():
            raise ValidationError("This Panther ID is already registered.")
        return panther_id

    def clean_team_member_2_panther_id(self):
        team_member_2_panther_id = self.cleaned_data.get('team_member_2_panther_id')
        if self.cleaned_data.get("registration_type") == "team" and team_member_2_panther_id:
            if RegisteredMember.objects.filter(panther_id=team_member_2_panther_id).exists():
                raise ValidationError("The second team member's Panther ID is already registered.")
        return team_member_2_panther_id

    def clean(self):
        cleaned_data = super().clean()
        reg_type = cleaned_data.get("registration_type")

        # If registering as a team, ensure all team fields are filled
        if reg_type == "team":
            for field in ['team_member_2_first_name', 'team_member_2_last_name', 'team_member_2_email', 
                          'team_member_2_panther_id', 'team_member_2_degree', 'team_member_2_major', 'team_member_2_csc_1302']:
                if not cleaned_data.get(field):
                    self.add_error(field, "This field is required for team registrations.")
        return cleaned_data
