# main/views.py

from django.shortcuts import render
from .models import RegisteredMember
from .forms import RegistrationForm

# Set the maximum number of registrations allowed
MAX_REGISTRATIONS = 20

def landing_page(request):
    """
    View for the landing page. Displays remaining spots.
    """
    total_registered = RegisteredMember.objects.count()
    remaining_spots = MAX_REGISTRATIONS - total_registered
    return render(request, 'main/landing_page.html', {'remaining_spots': remaining_spots})



def register(request):
    total_registered = RegisteredMember.objects.count()
    remaining_spots = MAX_REGISTRATIONS - total_registered

    if remaining_spots <= 0:
        return render(request, 'main/closed.html')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg_type = form.cleaned_data['registration_type']
            
            # Save data for the first participant
            first_participant = RegisteredMember(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                panther_id=form.cleaned_data['panther_id'],
                degree=form.cleaned_data['degree'],
                major=form.cleaned_data['major'],
                csc_1302=form.cleaned_data['csc_1302'] == 'yes'
            )
            first_participant.save()
            
            # If team registration, also save data for the second participant
            if reg_type == 'team':
                second_participant = RegisteredMember(
                    first_name=form.cleaned_data['team_member_2_first_name'],
                    last_name=form.cleaned_data['team_member_2_last_name'],
                    email=form.cleaned_data['team_member_2_email'],
                    panther_id=form.cleaned_data['team_member_2_panther_id'],
                    degree=form.cleaned_data['team_member_2_degree'],
                    major=form.cleaned_data['team_member_2_major'],
                    csc_1302=form.cleaned_data['team_member_2_csc_1302'] == 'yes'
                )
                second_participant.save()
            
            return render(request, 'main/thank_you.html')
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form, 'remaining_spots': remaining_spots})

def program(request):
    """
    View for the program page.
    """
    return render(request, 'main/program.html')
