# Form 1: Name: People; Purpose: Collect basic demographic information;
# Visible Fields: First and Last Name, DOB, Age, Gender
# Hidden Fields: Participant ID

# Form 2: Name: Practice; Purpose: Collect practice trial data;
# Visible Fields: Player 1, Player 2, Behavior
# Hidden Fields: None

# Form 3: Name: Game Round 1; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Answer 1, Answer 2
# Hidden Fields: None

# Form 4: Name: Game Round 2; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 2
# Hidden Fields: None

# Form 5: Name: Game Round 3; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 3
# Hidden Fields: None

# Form 6: Name: Game Round 4; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 4
# Hidden Fields: None

from django.forms import ModelForm, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from polls.models import Person, Observation
from django.core.exceptions import ValidationError

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObservationForm, self).__init__(*args, **kwargs)

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()

        # Make sure that the player 1 and player 2 names aren't the same
        player1 = cleaned_data.get("player1")
        player2 = cleaned_data.get("player2")

        if player1 == player2:
            # Add error on player 2 field
            self.add_error('player2', 'Player 2 cannot match Player 1')

            # Raises error on entire form
            raise ValidationError(
                "Player 1 and Player 2 individuals cannot be the same"
            )


ObservationModelFormSet = modelformset_factory(Observation, form=ObservationForm, extra=0, max_num=1)