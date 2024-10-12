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



def get_next_team_number():
    # Find the latest team number and increment it
    last_team = RegisteredMember.objects.filter(team_number__isnull=False).order_by('-team_number').first()
    if last_team and last_team.team_number:
        last_number = int(re.search(r'\d+', last_team.team_number).group())
        return f"Team {last_number + 1}"
    return "Team 1"

def register(request):
    total_registered = RegisteredMember.objects.count()
    remaining_spots = MAX_REGISTRATIONS - total_registered

    if remaining_spots <= 0:
        return render(request, 'main/closed.html')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg_type = form.cleaned_data['registration_type']

            # Save the first participant's data
            first_participant = RegisteredMember(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                panther_id=form.cleaned_data['panther_id'],
                degree=form.cleaned_data['degree'],
                major=form.cleaned_data['major'],
                csc_1302=form.cleaned_data['csc_1302'] == 'yes'
            )

            # Assign a team number if it’s a team registration
            if reg_type == 'team':
                team_number = get_next_team_number()
                first_participant.team_number = team_number

                # Save the first participant with team_number
                first_participant.save()

                # Save the second participant with the same team number
                second_participant = RegisteredMember(
                    first_name=form.cleaned_data['team_member_2_first_name'],
                    last_name=form.cleaned_data['team_member_2_last_name'],
                    email=form.cleaned_data['team_member_2_email'],
                    panther_id=form.cleaned_data['team_member_2_panther_id'],
                    degree=form.cleaned_data['team_member_2_degree'],
                    major=form.cleaned_data['team_member_2_major'],
                    csc_1302=form.cleaned_data['team_member_2_csc_1302'] == 'yes',
                    team_number=team_number
                )
                second_participant.save()
            else:
                # Save individual registration without a team number
                first_participant.save()

            return render(request, 'main/thank_you.html')
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form, 'remaining_spots': remaining_spots})

def program(request):
    """
    View for the program page.
    """
    return render(request, 'main/program.html')
